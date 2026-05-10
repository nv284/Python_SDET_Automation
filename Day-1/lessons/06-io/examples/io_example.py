def demo_io():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    print(f"Hello {name}, you are {age} years old.")

    # file write/read
    with open('sample.txt', 'w', encoding='utf-8') as f:
        f.write(f"{name},{age}\n")

    with open('sample.txt', 'r', encoding='utf-8') as f:
        print('File contents:', f.read())

if __name__ == '__main__':
    demo_io()
