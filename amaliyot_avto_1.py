class Avto:
    " Avomobilllar haqida class"
    def __init__(self, model,rang,korobka,narh,probeg):
        self.model=model
        self.rang=rang
        self.korobka=korobka
        self.narh=narh
        self.probeg=0
    def get_info(self):
        return f"Model: {self.model} rangi:{self.rang} korobka {self.korobka} narhi:{self.narh} probeg {self.probeg}"
    def update_probeg(self,yangi_yurgani):
        self.probeg=yangi_yurgani

class Avtosalon:
    " Avto salon haqida class"
    def __init__(self,salon_nomi,manzili,sotuvdagi_avtolar):
        self.salon_nomi=salon_nomi 
        self.manzili=manzili 
        self.sotuvdagi_avtolar=[]
    def add_infos(self,mashina):
        self.sotuvdagi_avtolar.append(mashina)
    def print_infos(self):
        return [ mashina.get_info()   for mashina in self.sotuvdagi_avtolar  ]
        
Urganch_avto=Avtosalon('Urganchavto tex', 'urgach shahar', 'Malibu, cobalt')

car1=Avto('Gentra','qora','AT','15000 $ ',21000)
car2=Avto('Malibu','oq','AT','25000 $',15000)

Urganch_avto.add_infos(car1)
Urganch_avto.add_infos(car2)




        
