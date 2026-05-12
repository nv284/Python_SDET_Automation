from module_a import multiply, info
from module_b import greet

print('Module info:', info())
print('multiply(6,7)=', multiply(6, 7))
print(greet('RJP'))

if __name__ == '__main__':
    print('Runner executed directly')
