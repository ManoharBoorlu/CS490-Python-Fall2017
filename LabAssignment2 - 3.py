class Student:                                        # creates a class Student
    num=0                                             # initialize the data member value to 0
    def __init__(self,n,i,g):                         # Constructor to initialize details
        self.full_name=n
        self.id_number=i
        self.grades=g

    def count(self):                                  # Function to calculate the number of students
        self.__class__.num += 1

    def display(self):                                # Function to display students details
        print("Name is :", self.full_name)
        print("Id Number is :", str(self.id_number))
        print("Grade is :", self.grades)

class Grade(Student):                                 # a Grade Class inherited from Student Class
    def __init__(self,gr,po,n,i,p):
        self.grade=gr
        self.points=po

class System(Student):                                # A System Class Inherited from Student
    def __init__(self,uid,passcode):
        self.UserID=uid
        self.__password=passcode                      # A private data member

class Faculty(System):
    def __init__(self,fname,fid):
        self.Faculty_Name=fname
        self.Faculty_ID=fid


class TransferStudent(Student):                       # derived class from base class Student
    def __init__(self,n,i,g,d):                       # Instances to derived class
        Student.__init__(self,n,i,g)                  # Super Call
        self.tid=d
    def disp(self):
        print("Id:" , str(self.tid))


a=Student("Manohar",123,"B")                          # Calling their member functions
b=TransferStudent("Nikhil",145,"C",1255)
a.display()
a.count()
print("Number of Students are:"+ str(a.num))
b.display()
b.count()
b.disp()
print("Number of Students are:"+ str(b.num))



