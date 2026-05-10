def safe_int(s, default=None):
    try:
        return int(s)
    except (ValueError, TypeError):
        return default

if __name__ == '__main__':
    print(safe_int('42'))
    print(safe_int('abc', default=0))
