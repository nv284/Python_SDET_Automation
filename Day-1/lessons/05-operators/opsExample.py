a = input(" enter number for a")
b = input("enter number for b")
c =  input("enter number for c")
addition = ((a+b)+(a+c))
subtraction= (a*b*c)+(a-b)
divison = b/c
power = c**2
modulus = a %c

#comparison /relational operator 
greater = (a>b) = (b<a)
less = a<b
equal = a==b
not_equal = a!=b


#logocal operator 
logical_and = (a>b) and (b>c)
logical_or = (a<b) or (b>c)
logical_not = not(a<b)

#output
print("addition" , addition)
print("substraction" ,subtraction)
print("divison" , divison)
print ("power" , power)
print("Modulus" ,modulus)

print("Greater Then " , greater)
print("Less Then", less)
print("Equal", equal)

#logical operator
print("Logical And " , logical_and)
print("Logical OR" , logical_or)
print("Logical NOT" , logical_not)


