# Functions basics: parameters and return values
def add(a, b):
    return a + b

def greet(name='Guest'):
    return 'Hello ' + name

result = add(4, 5)
print('add(4,5)=', result)
print(greet('Nishi'))
print(greet())
