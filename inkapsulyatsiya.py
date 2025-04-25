from uuid import uuid4 
class Avto:
    "Avtomobil klassi"
    __avto__soni=0
    def __init__(self,make,model,rang,yil,narh,km=0):
        "Avtomobil xususiyatlari "
        self.make=make 
        self.model=model 
        self.rang=rang 
        self.yil=yil 
        self.narh=narh 
        self.__km=km 
        self.__id=uuid4()
        Avto.__avto__soni+=1
        
    def get_km(self):
        return self.__km 
    def get_id(self):
        return self.__id
    def add_km(self,km):
        "Mashinaga km qo`shish"
        if km>=0:
            self.__km+=km
        else:
            print("mashinaning km ni kamaytirib bo`lmaydi")
    @classmethod
    def get_num_avto(cls):
        return cls.__avto__soni 
    def get_km(cls):
        return cls.__km
    def get_idnumber(cls):
        return cls.__id 
        
        
avto1=Avto('GM','Gentra','qora',2024,'15000$',1101)
avto2=Avto('GM','Kobalt','gk2',2020,'11000$',1101)
avto3=Avto('GM','Damas','oq',2025,'8000$',1101)
