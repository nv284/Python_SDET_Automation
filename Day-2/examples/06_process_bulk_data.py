# Process bulk test data: simulate CSV rows in a list and aggregate results
rows = [
    'alice,85,passed',
    'bob,58,failed',
    'carol,92,passed',
    'dave,74,passed',
    'eve,58,failed'
]

passed = []
failed = []
for r in rows:
    parts = r.split(',')
    name = parts[0]
    score = int(parts[1])
    status = parts[2]
    if status == 'passed':
        passed.append((name, score))
    else:
        failed.append((name, score))

print('Passed students:', passed)
print('Failed students:', failed)

# build summary dict
summary = {}
summary['total'] = len(rows)
summary['passed'] = len(passed)
summary['failed'] = len(failed)
print('Summary:', summary)
