def demonstrate_variables():
    name = "Alex"
    age = 30
    balance = 1024.50

    print(f"Name: {name}, Age: {age}, Balance: {balance}")

    # mutability
    lst = [1, 2, 3]
    print("Before:", lst)
    lst.append(4)
    print("After:", lst)

    # scope
    def inner():
        local = "inside"
        print("Local in inner:", local)

    inner()

if __name__ == '__main__':
    demonstrate_variables()
