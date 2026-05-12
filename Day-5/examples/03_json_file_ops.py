import json

records = [
    {'id': 1, 'name': 'alice'},
    {'id': 2, 'name': 'bob'},
]

path = 'records.json'
with open(path, 'w', encoding='utf-8') as f:
    json.dump(records, f, indent=2)

print('Wrote JSON to', path)

with open(path, 'r', encoding='utf-8') as f:
    loaded = json.load(f)
    print('Loaded JSON:', loaded)
