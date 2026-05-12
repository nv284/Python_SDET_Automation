namme = input("Enter  student Name :")
marks = int(input(" Enter marks :"))

#output
print("student Name : " , namme)
print("Student Marks :" , marks)

# write into file
file =open("student.txt" , "w")
file.write("Name : " + namme)
file.write("\n")
file.write("Marks :" + str(marks))
file.close()

#Read from file 
file = open("student.txt" , "r")
data= file.read()

print("\n File Data :")
print(data)
file.close()