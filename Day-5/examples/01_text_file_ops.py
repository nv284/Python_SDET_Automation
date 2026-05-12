# Text file operations: write and read using context managers
path = 'sample.txt'
with open(path, 'w', encoding='utf-8') as f:
    f.write('line1\n')
    f.write('line2\n')

print('Wrote', path)

with open(path, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f, start=1):
        print('Line', i, ':', line.strip())
