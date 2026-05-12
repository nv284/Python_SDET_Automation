balance = int(input("Enter balance"))

print("======welcome into SBI Bank=======")

while True:
    print("\n1, Check balance ")
    print("2. Deposit Money")
    print("3. Withdraw Money ")
    print("4. Exit")

    choice = input("enter your choice")

    if choice == "1":
        print("Available Balance :" ,balance)

    elif choice == "2":
        deposit = float(input("Enter deposit amount : "))

        if deposit >0 :
            balance += deposit
            print("Amount Deposited successfully")
            print("Updated Balance " , balance)
        else:
            print("invalid deposit amount")

            #withdraw 
    elif choice =="3":
            withdraw = float(input("Enter withdrawal amount :"))
            if withdraw <= balance and withdraw >0:
                 balance -= withdraw
                 print("please collect your cash ")
                 print("Remaning Balance " , balance)
            else:
                 print("Insufficient Balance ")

            # exit 
            

     