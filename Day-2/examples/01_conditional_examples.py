# Conditional examples: access levels and threshold checks
user_role = 'guest'  # try 'admin', 'editor', 'guest'
if user_role == 'admin':
    print('Full access granted')
elif user_role == 'editor':
    print('Edit access granted')
else:
    print('Read-only access')

score = 72
if score >= 90:
    grade = 'A'
elif score >= 75:
    grade = 'B'
elif score >= 60:
    grade = 'C'
else:
    grade = 'F'
print('Score', score, '=> Grade', grade)
