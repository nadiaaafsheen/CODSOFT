def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
        print("CANNOT BE DIVIDED BY ZERO")
    return x/y
print("welcome to a simple calculator!")
print("following operations can be performed:")
print("1.ADD")
print("2.SUBTRACT")
print("3.MULTIPLY")
print("4. DIVIDE")

choice= input("ENTER YOUR CHOICE (1/2/3/4): ")

n1= float(input("enter your first number: "))
n2= float(input("enter your second number: "))

result =0
if choice == '1':
    result= add(n1,n2)
elif choice=='2':
    result= subtract(n1,n2)
elif choice == '3':
    result= multiply(n1,n2)
elif choice == '4':
    result= divide(n1,n2)
else:
    print("THE CHOICE YOU HAVE ENTERED IS INVALID")

if type(result) == float:
    print(f"{result:.2f}")
else:
    print(result)




