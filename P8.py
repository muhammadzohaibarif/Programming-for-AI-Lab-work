#parent class ma sab attributes ko define 
#kyun k parent aur child class ma yearly pay ka faraq ha, islia ham 2 separate functions banate hain


class employee:
    def __init__(self,name,salary):
        self.salary = salary
        self.name = name

    def yearlyPay(self):
     return self.salary*12 

    
#child class ma bonus ki wajah se ham super().__init__ use karte hain


class manager(employee):
    def __init__(self,name,salary,bonus):
        super().__init__ (name,salary)
        self.salary = salary
        self.bonus = bonus

    def yearlyPay(self):
     return (self.salary*12)+ self.bonus
  



#last pe ham input dete hain aur hamare pass last pe yearly pay k saath name bi aa jata ha 

staff = [employee("Sara", 80000), manager("Omar", 150000, 200000)]
for person in staff:
   
    print(person.name, person.yearlyPay())


#instance check karne k lia isinstance ka keyword use karte hain     
print(isinstance(staff[0], employee))
print(isinstance(staff[1], employee))

