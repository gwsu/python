class pepole:
    name = ''
    age = 0
    __weight = 0
    
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    
    def speak (self):
        print ("%s is speaking : i am %d years old" %(self.name,self.age))


p = pepole('tom',10,30)
p.speak()


class student(pepole):
    grade = ''
    
    def __init__(self,n,a,w,g):
        pepole.__init__(self,n,a,w)
        self.grade = g

    def speak(self):
        print ("%s is speaking : i am %d yeas old,and i am in grade %d" %(self.name,self.age,self.grade))


s= student('ken',20,60,3)
s.speak()

