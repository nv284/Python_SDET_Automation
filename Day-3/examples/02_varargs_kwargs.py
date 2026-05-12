# Demonstrate *args and **kwargs
def concat(*parts, sep=' '):
    result = ''
    first = True
    for p in parts:
        if not first:
            result += sep
        result += str(p)
        first = False
    return result

def show_info(**info):
    for k, v in info.items():
        print(k + ':', v)

print(concat('This', 'is', 'joined', sep='-'))
show_info(name='Asha', age=29, role='student')
