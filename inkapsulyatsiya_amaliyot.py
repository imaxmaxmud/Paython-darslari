from uuid import uuid4 

class Shaxs:
    " Shaxslarga tegishli klass"
    odamlar_soni=0
    def __init__(self,ism,fam,tyil,uy,kocha,tuman,vil,telefon):
        self.ism=ism 
        self.fam=fam 
        self.tyil=tyil 
        self.uy=uy 
        self.kocha=kocha 
        self.tuman=tuman 
        self.vil=vil 
        self.telefon=telefon 
        Shaxs.odamlar_soni+=1
    def get_info(self):
        " Shaxsga tegishli ma`lumotlarni print qiish "
        info=f"Ismi : {self.ism}, familiya : {self.fam}, tugulgan yili : {self.tyil},"
        info+=f"Uy : {self.uy}, Ko`cha : {self.kocha}, Tuman : {self.tuman},"
        info+=f" Viloyat : {self.vil}, Telefon : {self.telefon }"
        return info 
    def get_odamlar_soni(self):
        return self.odamlar_soni
class Talaba(Shaxs):
    " Talabaga tegishli funskiya "
    __talabalar_soni=0
    def __init__(self,ism,fam,tyil,uy,kocha,tuman,vil,telefon):
        "Talaba xususiyatlari "
        super().__init__(ism, fam, tyil, uy, kocha, tuman, vil, telefon)
        self.idraqam=uuid4()
        self.bosqich=1
        Talaba.__talabalar_soni+=1
    def get_id(self):
        return  self.idraqam
   
        
    def get_infos(self):
        " Talabaga tegishli ma`lumotlarni print qiish "
        info=f"Ismi : {self.ism}, familiya : {self.fam}, tugulgan yili : {self.tyil},"
        info+=f"Uy : {self.uy}, Ko`cha : {self.kocha}, Tuman : {self.tuman},"
        info+=f" Viloyat : {self.vil}, Telefon : {self.telefon}, ID : {self.idraqam}, Bosqich : {self.bosqich} "
        return info 
        
    @classmethod
    def get_talabalar_soni(cls):
        return cls.__talabalar_soni
        
    
    
student1=Talaba('mahmudjon','Sadikov',1991,12,'Qibla','Yanigbozor','Xorazm',4048822)
        