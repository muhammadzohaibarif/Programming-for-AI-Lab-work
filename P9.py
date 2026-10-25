#pehle aik point class banai gayi ha
#phir 4 fucntions defined hain 
#jin ma self, add, str,aur eq ka function shamil ha
#self funcion
class point:
    def __init__(self,x,y):
        self.point1= x
        self.point2= y

#add fucnion yea points ko add karta ha 
    def __add__(self,other):
        return point(self.point1+other.point1,self.point2+other.point2)

#str fucntion yea aik line ma points ko liktha ha 
    def __str__(self):
       return f"{self.point1,self.point2}"

#eq function campare karta ha points ko
    def __eq__(self,other):
        return (self.point1==other.point1 and self.point2==other.point2)

    #given input

p = point(1, 2) + point(3, 4)
print(p)
print(p == point(4, 6), p == point(0, 0))