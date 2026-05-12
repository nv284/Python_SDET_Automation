import csv
import json
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')
logger = logging.getLogger('testdata')

DATA_CSV = 'fixtures.csv'
DATA_JSON = 'fixtures.json'

# create sample fixtures CSV
rows = [['id', 'name', 'value'], ['1', 'alpha', '10'], ['2', 'beta', '20']]
with open(DATA_CSV, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for r in rows:
        writer.writerow(r)
logger.info('Wrote CSV fixtures: %s', DATA_CSV)

# export to JSON
records = []
with open(DATA_CSV, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for r in reader:
        try:
            r['value'] = int(r['value'])
        except Exception:
            r['value'] = 0
        records.append(r)

with open(DATA_JSON, 'w', encoding='utf-8') as f:
    json.dump(records, f, indent=2)
logger.info('Exported fixtures to JSON: %s', DATA_JSON)

# simple loader with exception handling
def load_json(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error('Fixture not found: %s', path)
        return []
    except json.JSONDecodeError:
        logger.error('Invalid JSON in %s', path)
        return []

data = load_json(DATA_JSON)
logger.info('Loaded %d records', len(data))
for r in data:
    logger.info('Record %s -> %s', r.get('id'), r)
