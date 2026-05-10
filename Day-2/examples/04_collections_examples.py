# Collections: lists, tuples, sets, dictionaries

# Lists - CRUD
fruits = ['apple', 'banana', 'cherry']
print('Original', fruits)
fruits.append('date')
fruits[1] = 'blueberry'  # update
del fruits[0]
print('Updated', fruits)

# Tuples - immutability
coords = (10, 20)
print('Tuple:', coords)

# Sets - uniqueness
ids = [1,2,2,3,4,4]
unique_ids = set(ids)
print('Unique IDs:', unique_ids)

# Dictionaries - key-value
user = {'id': 101, 'name': 'Sam'}
print('User name:', user['name'])
user['email'] = 'sam@example.com'
print('User keys:', list(user.keys()))
