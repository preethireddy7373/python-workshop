balance=10000
amount=int(input("Enter a amount"))
if(amount>balance):
    print("You have insufficient balance")
else:
    print("Your amount has been debited")
    balance-=amount
    print(f"your new balance{balance}")


