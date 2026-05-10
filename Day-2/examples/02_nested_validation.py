# Nested validation: simulate signup data validation
input_name = 'Alice'
input_age = 17
input_email = 'alice@example.com'

if input_name:
    if '@' in input_email:
        if input_age >= 18:
            print('User accepted:', input_name)
        else:
            print('Underage user; parental consent required')
    else:
        print('Invalid email address')
else:
    print('Name is required')
