class Avto:
    " Avtolarga tegishli class"
    number_cars=0 
    def __init__(self, company,model,color,year,cost,mileage):
        self.company=company 
        self.model=model 
        self.color=color 
        self.year=year 
        self.cost=cost
        self.mileage=mileage 
        Avto.number_cars+=1 
   
    def __repr__(self):
          printga=f"Company : {self.company}, Model : {self.model}, Color : {self.color}, "
          printga+=f"Year : {self.year}, Cost : {self.cost}, Mileage : {self.mileage} "
          return printga   
       
class Avtosalon:
    "Avtosalonga tegishli klass"
    
    def __init__(self,name):
        self.name=name 
        self.avtolar=[] 
    def __repr__(self):
        return f"{self.name} avtosalon "
    def add_car(self,*qiymat):
        for avto in qiymat:
            if isinstance(avto, Avto):
               self.avtolar.append(avto)
            else:
                print("Avto kiriting ")
    def __getitem__(self,index):
        return self.avtolar[index]
    def __setitem__(self,index,qiymat):
         self.avtolar[index]=qiymat


salon1=Avtosalon('Urganchavtotexxizmat')
car1=Avto('GM','Gentra','black',2024,'15000$','21000 km')
car2=Avto('BMW','X6','black',2025,'35000$','5 km')
car3=Avto('MERS','E205','white',2025,'40000$','6 km')
cars=[car1,car2,car3]




salon1.add_car(car1,car2,car3)
                    
       







