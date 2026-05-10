import json
from pathlib import Path

DB = Path('budget.json')

def load():
    if DB.exists():
        return json.loads(DB.read_text(encoding='utf-8'))
    return {'entries': []}

def save(data):
    DB.write_text(json.dumps(data, indent=2), encoding='utf-8')

def add_entry(kind, amount, note=''):
    data = load()
    data['entries'].append({'kind': kind, 'amount': float(amount), 'note': note})
    save(data)

def summary():
    data = load()
    total = sum(e['amount'] if e['kind']=='income' else -e['amount'] for e in data['entries'])
    print(f"Balance: {total:.2f}")

if __name__ == '__main__':
    print('Budget CLI starter')
    add_entry('income', 1000, 'salary')
    add_entry('expense', 123.45, 'groceries')
    summary()
