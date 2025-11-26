class adhaar:
    def __init__(self,name,adhaar_number,dob,finger_print,retina):
        self.name=name
        self.adhaar_number=adhaar_number
        self.dob=dob
        self._finger_print=finger_print
        self.__retina=retina

    def display_userData(self):
        print(f"Retena:{self.__retina},Adhaar_Number:{self.adhaar_number}")

    def getRetena(self):
        return self.__retina

var=adhaar("pree",455447,"8-apr-2003","fdjnkmjsk","kjhkjghfffff")
var.display_userData()
retena_var=var.getRetena()
print(retena_var)