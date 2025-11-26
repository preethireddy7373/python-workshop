class Application:
    def __init__(self,application_name,category,company,app_size,no_of_users,ratings):
        self.application_name=application_name
        self.category=category
        self.company=company
        self.app_size=app_size
        self.no_of_users=no_of_users
        self.ratings=ratings

    def signup(self):
        print(f"signup done ,{self.application_name}")
    def login(self):
         print(f"Welcome to {self.application_name}")
    def logout(self):
        print("thank you for using")

    def display_details(self):
        print("\n---- Application Details ----")
        print(f"Application Name : {self.application_name}")
        print(f"Category         : {self.category}")
        print(f"Company          : {self.company}")
        print(f"App Size (MB)    : {self.app_size}")
        print(f"No. of Users     : {self.no_of_users}")
        print(f"Ratings          : {self.ratings}")
        print("------------------------------")


app1=Application("Instagram","social Media","meta",42.47,1000,5)
app2=Application("Facebook","social Media","meta",47.21,2000,6)
app3=Application("Whatsapp","social Media","meta",45.47,5000,8)

app1.signup()
app1.login()
app1.display_details()
app1.logout()

app2.signup()
app2.login()
app2.display_details()
app2.logout()

app3.signup()
app3.login()
app3.display_details()
app3.logout()




