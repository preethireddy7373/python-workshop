age=int(input("enter your age"))
def vote(age):
    if(age>18):
        print("eligible to vote")
    else:
        print("not eligible")
    vote(age)
