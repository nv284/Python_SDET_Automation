# CSV read/write example
import csv

data = [
    ['id', 'name', 'score'],
    ['1', 'Alice', '85'],
    ['2', 'Bob', '78'],
]

path = 'data.csv'
with open(path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)

print('CSV written to', path)

with open(path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for r in reader:
        print('Row:', r)
