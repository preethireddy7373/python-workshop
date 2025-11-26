def userInput():
    first_input=int(input("Enter the first number:"))
    second_input=int(input("Enter the second number:"))
    return first_input,second_input
def add(a=0,b=0):
    return a+b
def sub(a=0,b=0):
    return a-b
def mul(a=0,b=0):
    return a*b
print("Welcome to Call")
while True:
    print("Select the choose:\n 1:Add\n 2:sub\n 3:mul\n 4:stop ")
    choose=int(input("Enter the choose:"))

    if choose==1:
        x,y=userInput()
        print(f"Addition of two number:{add(x,y)}")
    elif choose==2:
        x,y=userInput()
        print(f"Sub of two number:{sub(x,y)}")
    elif choose==3:
        x,y=userInput()
        print(f"Multiplication of two number:{mul(x,y)}")
    elif choose==4:
        print("Thank you for using calculator")
        break
