balance=1000
while True:
    type=input("Enter the type credit/debit/stop:")
    if(type=="stop"):
        break
    elif(type=="credit"):
        credit_amount=int(input("Enter the credit amount:"))
        balance=balance+credit_amount;
        print(f"the current balance is {balance}")
    elif (type == "debit"):
        debit_amount = int(input("Enter the debit amount:"))
        if (balance > debit_amount):
            balance = balance - debit_amount
            print(f"amount debited and the current balance is {balance}")
        else:
            print("insufficient balance")
    else:
        print(f"balance:{balance}")M