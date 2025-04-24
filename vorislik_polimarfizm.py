class Shaxs:
    " Shaxslar haqida ma`lumot"
    def __init__(self,ism,fam,passport,tyil):
        self.ism=ism
        self.fam=fam
        self.passport=passport 
        self.tyil=tyil 
        
    def get_info(self):
        "SHaxs haqida ma`lumot chiqaruvchi metod"
        info=f"{self.ism.title()}  {self.fam.title()}  "
        info+=f"Passport:{self.passport.upper()} {self.tyil} yilda tug`ilgan"
        return info 
    def get_age(self,yil):
        " Shaxsning yoshini chiqaruvchi metod"
        yosh=yil-self.tyil
        return f"Yoshi {yosh} da "
    
class Talaba(Shaxs):
    " talaba nomli super class Shaxs classidan ma`lumot oladi"
    def __init__(self,ism,fam,passport,tyil,idraqam,manzil):
        super().__init__(ism, fam, passport, tyil)
        self.idraqam=idraqam
        self.bosqich=1
        self.manzil=manzil
    def get_id(self):
        " talabaning id raqamini ko`rsat"
        return self.idraqam
    def get_bosqich(self):
        return self.bosqich
    def get_info(self):
        "SHaxs haqida ma`lumot chiqaruvchi metod"
        info=f"{self.ism.title()}  {self.fam.title()}  "
        info+=f"Passport : {self.passport.upper()} {self.tyil} yilda tug`ilgan,"
        info+=f" Talaba id raqami: {self.idraqam}"
        return info 
class Manzil:
    " Talabaning manziliga tegishli class"
    def __init__(self,uy,kocha,tuman,viloyat):
        self.uy=uy 
        self.kocha=kocha 
        self.tuman=tuman 
        self.viloyat=viloyat
    def get_manzil(self):
        "manzil ko`rish"
        manzil=f"Uy raqami:{self.uy}, Ko`chasi:{self.kocha}, tumani:{self.tuman}"
        manzil+=f" Viloyati:{self.viloyat}"
        return manzil 
    
        
        
talaba1_manzil=Manzil(12,'Qibla','Yangibozor','Xorazm')       
        
talaba1=Talaba('Mahmudjon','Sadikov','AA5822294',1991,'ID23111',talaba1_manzil)
