print("hello calculator")
def addd(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b  
def div(a,b):
    return a/b
def menu():
    print("1. add")
    print("2. sub")
    print("3. mul")
    print("4. div")
    print("5. exit")
menu()
choice=int(input("enter your choice"))
a=int(input("enter first number"))
b=int(input("enter second number"))
if choice==1:
    print("addition is",addd(a,b))
elif choice==2:
    print("subtraction is",sub(a,b))
elif choice==3:
    print("multiplication is",mul(a,b))
elif choice==4:
    print("division is",div(a,b))
    if a==0 or b==0:
        print("division by zero is not allowed")
elif choice==5:
    print("thank you for using calculator")
    break
else:
    print("invalid choice")

