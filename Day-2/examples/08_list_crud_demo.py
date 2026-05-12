student = []
while  True:
    print("\n ===== Studnt management System========")
    print("1. Add student ")
    print("2. View Student")
    print("3. Update Student")
    print("4.Delete Student")
    print("5. Exit")


    choice = input("Enter choice :")

#chreate
    if choice =="1":
        name = input("Enter Student name:")
        student.append(name)
        print("Student added successfully !")

    #read
    elif choice=="2":
         print("\nStudent List")
    for s in student:
          print(s)

    #update
    elif choice=="3":
    old_name = input("Enter old name : ")
    new_name = input("Enter new Name :")
    index = student.index(old_name)
    student[index] = new_name

    print("Student infor updated successfully !")

    # Delete

    #Exit
elif choice == "5":
    print("program Ended ")
  
else:
    print("Invalid choice")