
class Talaba:
    def __init__(self,ism,fam,tyil):
        self.ism=ism 
        self.fam=fam 
        self.tyil=tyil
    def tanishtir(self):
        return (f"Mening ismim {self.ism} va familiyam {self.fam}")
    def get_name(self):
        return self.ism
    def get_age(self):
        from datetime import datetime
        bugun=datetime.now()
        yosh=bugun.year-int(self.tyil)
        return yosh
    def get_yosh(self,yil):
        yoshi=yil-self.tyil
        return yoshi  
    def otasining_ismi(self,otasi_ismi):
        ota=self.ism+'  ' +otasi_ismi
        return ota        
talaba1=Talaba('Mahmudjon','Sadikov',1991)

print(talaba1.tanishtir())