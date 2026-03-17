import re
import os

BASE = "C:/Users/smrTu/OneDrive/Documents/GithubC/usgin/geochemBuildingBlocks/_sources/adaProperties"

# JSON Schema keywords that should NOT be prefixed
SCHEMA_KEYWORDS = {
    'type', 'description', 'const', 'enum', 'items', 'anyOf', 'oneOf', 'allOf',
    'required', 'properties', 'minItems', 'maxItems', 'default', 'format',
    'minContains', 'contains', 'minLength',
}

# Prefixes that indicate already-namespaced properties
EXISTING_PREFIXES = ('schema:', 'ada:', 'csvw:', 'prov:', 'cdi:', 'nxs:', '@', '$', 'cdifd:', 'sh:', 'rdf:', 'rdfs:', 'xsd:')

def needs_prefix(prop_name):
    """Check if a YAML property key needs ada: prefix."""
    if prop_name in SCHEMA_KEYWORDS:
        return False
    for p in EXISTING_PREFIXES:
        if prop_name.startswith(p):
            return False
    if prop_name.startswith('_'):
        return False
    # Must be a plain identifier (camelCase, etc.) - no colons, no special chars
    if not re.match(r'^[a-zA-Z][a-zA-Z0-9_]*$', prop_name):
        return False
    return True


def extract_yaml_key(stripped_line):
    """Extract the full YAML key from a line.
    Returns (key_name, quote_char, full_key_text, rest_of_line) or None.

    Examples:
      propName: value        -> ('propName', '', 'propName', ': value')
      'ada:pixelUnits': ...  -> ('ada:pixelUnits', "'", "'ada:pixelUnits'", ': ...')
      "schema:name": ...     -> ('schema:name', '"', '"schema:name"', ': ...')
      schema:additionalType: -> ('schema:additionalType', '', 'schema:additionalType', ':')
    """
    # Quoted with single quotes: 'key': rest
    m = re.match(r"^'([^']+)'(\s*:.*)$", stripped_line)
    if m:
        return m.group(1), "'", "'" + m.group(1) + "'", m.group(2)

    # Quoted with double quotes: "key": rest
    m = re.match(r'^"([^"]+)"(\s*:.*)$', stripped_line)
    if m:
        return m.group(1), '"', '"' + m.group(1) + '"', m.group(2)

    # Unquoted: key may contain colons (like schema:name)
    # YAML key ends at ": " or ":\n" or ":" at end of line
    # Match everything up to the LAST ": " or ":" at end
    m = re.match(r'^([^\s][^:]*(?::[^\s:][^:]*)*)(:\s*.*)$', stripped_line)
    if m:
        key = m.group(1)
        rest = m.group(2)
        return key, '', key, rest

    # Simple unquoted key
    m = re.match(r'^([a-zA-Z_][a-zA-Z0-9_:]*)(\s*:.*)$', stripped_line)
    if m:
        return m.group(1), '', m.group(1), m.group(2)

    return None


def fix_schema_yaml(filepath):
    """Fix property names in schema.yaml files."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    fixed_props = set()

    lines = content.split('\n')
    new_lines = []

    # Track properties: blocks. Each entry is the indent of 'properties:' keyword
    props_indents = []
    req_indents = []

    for i, line in enumerate(lines):
        stripped = line.lstrip()
        indent = len(line) - len(stripped)

        if not stripped:
            new_lines.append(line)
            continue

        # Clean stacks: remove entries at indent >= current (we've exited those blocks)
        props_indents = [x for x in props_indents if x < indent]
        req_indents = [x for x in req_indents if x < indent]

        # Detect properties: keyword
        if stripped == 'properties:' or stripped == 'properties: {}':
            props_indents.append(indent)
            new_lines.append(line)
            continue

        # Detect required: keyword
        if stripped.startswith('required:'):
            req_indents.append(indent)
            new_lines.append(line)
            continue

        # Check if this line is a direct child property of a properties: block
        is_prop_child = any(indent == pi + 2 for pi in props_indents)

        # Check if inside a required: block
        is_req_child = any(indent > ri for ri in req_indents)

        if is_prop_child:
            result = extract_yaml_key(stripped)
            if result:
                key_name, quote_char, full_key_text, rest = result
                if needs_prefix(key_name):
                    fixed_props.add(key_name)
                    new_key = "'ada:" + key_name + "'"
                    new_line = ' ' * indent + new_key + rest
                    new_lines.append(new_line)
                    continue

        if is_req_child and stripped.startswith('- '):
            item_part = stripped[2:].strip()
            # Extract the value
            if item_part.startswith("'") and item_part.endswith("'"):
                val = item_part[1:-1]
            elif item_part.startswith('"') and item_part.endswith('"'):
                val = item_part[1:-1]
            else:
                val = item_part

            if needs_prefix(val):
                fixed_props.add(val)
                new_line = ' ' * indent + "- 'ada:" + val + "'"
                new_lines.append(new_line)
                continue

        new_lines.append(line)

    content = '\n'.join(new_lines)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    return sorted(fixed_props)


def fix_examples_yaml(filepath, props_to_fix):
    """Fix property names in examples.yaml files."""
    if not os.path.exists(filepath):
        return []

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    fixed = []

    for prop in props_to_fix:
        old = '"' + prop + '":'
        new = '"ada:' + prop + '":'
        if old in content:
            content = content.replace(old, new)
            fixed.append(prop)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    return sorted(fixed)


def fix_example_json(filepath, props_to_fix):
    """Fix property names in example*.json files."""
    if not os.path.exists(filepath):
        return []

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    fixed = []

    for prop in props_to_fix:
        old = '"' + prop + '":'
        new = '"ada:' + prop + '":'
        if old in content:
            content = content.replace(old, new)
            fixed.append(prop)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    return sorted(fixed)


def check_shacl(filepath, props_to_fix):
    """Check SHACL already uses ada: prefixed paths."""
    if not os.path.exists(filepath):
        return True, []

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    issues = []
    for prop in props_to_fix:
        if 'ada:' + prop not in content:
            issues.append(prop)

    return len(issues) == 0, issues


detail_dirs = [
    'detailARGT', 'detailBasemap', 'detailDSC', 'detailEAIRMS', 'detailEMPA',
    'detailICPOES', 'detailL2MS', 'detailLAF', 'detailNanoIR', 'detailNanoSIMS',
    'detailPSFD', 'detailQRIS', 'detailSLS', 'detailVNMIR', 'detailXCT', 'detailXRD'
]

non_detail_dirs = [
    'collection', 'creativeWork', 'dataCube', 'document', 'files',
    'image', 'imageMap', 'instrument', 'laboratory', 'otherFile',
    'spatialRegistration', 'stringArray', 'supDocImage', 'tabularData'
]

all_dirs = detail_dirs + non_detail_dirs
results = {}

for d in all_dirs:
    dir_path = os.path.join(BASE, d)
    if not os.path.isdir(dir_path):
        results[d] = {'error': 'directory not found'}
        continue

    schema_path = os.path.join(dir_path, 'schema.yaml')
    examples_path = os.path.join(dir_path, 'examples.yaml')
    rules_path = os.path.join(dir_path, 'rules.shacl')

    schema_fixed = []
    if os.path.exists(schema_path):
        schema_fixed = fix_schema_yaml(schema_path)

    examples_fixed = []
    if schema_fixed and os.path.exists(examples_path):
        examples_fixed = fix_examples_yaml(examples_path, schema_fixed)

    json_fixed = []
    for f in os.listdir(dir_path):
        if f.startswith('example') and f.endswith('.json'):
            jf = fix_example_json(os.path.join(dir_path, f), schema_fixed)
            json_fixed.extend(jf)

    shacl_ok = True
    shacl_issues = []
    if os.path.exists(rules_path) and schema_fixed:
        shacl_ok, shacl_issues = check_shacl(rules_path, schema_fixed)

    results[d] = {
        'schema_fixed': schema_fixed,
        'examples_fixed': examples_fixed,
        'json_fixed': json_fixed,
        'shacl_ok': shacl_ok,
        'shacl_issues': shacl_issues,
        'count': len(schema_fixed)
    }

total = 0
for d in all_dirs:
    r = results[d]
    if 'error' in r:
        print(f"  {d}: ERROR - {r['error']}")
        continue
    count = r['count']
    total += count
    if count > 0:
        print(f"  {d}: {count} properties fixed: {', '.join(r['schema_fixed'])}")
        if r['examples_fixed']:
            print(f"    examples.yaml: fixed {', '.join(r['examples_fixed'])}")
        if r['json_fixed']:
            print(f"    example*.json: fixed {', '.join(r['json_fixed'])}")
        if not r['shacl_ok']:
            print(f"    SHACL ISSUES (not all props in SHACL): {r['shacl_issues']}")
        elif os.path.exists(os.path.join(BASE, d, 'rules.shacl')):
            print(f"    rules.shacl: OK (already uses ada: prefix)")
    else:
        print(f"  {d}: 0 properties needed fixing")

print(f"\nTotal: {total} properties fixed across all directories")
