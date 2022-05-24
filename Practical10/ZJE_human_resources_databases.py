class Staff:#Defining a class Staff
    def __init__(self,firstname,lastname,location,role):#Giving attributes here.
        self.firstname=firstname
        self.lastname=lastname
        self.location=location
        self.role=role
    def inf(self):#Defining a function that prints the name, location and role of a stuff.
        print(f'The stuff member\'s name is {self.firstname} {self.lastname}, location is {self.location}, role is {self.role}.')

#An example given here.
Wanlu=Staff('Liu','Wanlu','International Campus','faculty')
Wanlu.inf()