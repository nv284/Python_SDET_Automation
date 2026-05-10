# Loops: for, while, break, continue
names = ['Anna', 'Bob', 'Charlie', 'Dana']
for name in names:
    if name == 'Charlie':
        print('Skipping', name)
        continue
    print('Hello', name)

count = 0
while count < 5:
    print('count is', count)
    count += 1
    if count == 3:
        print('Early stop at 3')
        break
