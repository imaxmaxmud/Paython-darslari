class Talaba:
    " Talaba nomli klass yaratmiz"
    def __init__(self,ism,fam,tyil):
        self.ism=ism
        self.fam=fam
        self.tyil=tyil 
        self.bosqich=1
    def talaba_info(self):
        return f"Ismi {self.ism} familiyasi {self.fam} t yili {self.tyil}"
    def get_name(self):
        return self.ism
    def get_surname(self):
        return self.fam
    def millat(self,millat):
        return self.millat
    
talaba1=Talaba('Mahmudjon','Sadikov',1991)
print(talaba1.talaba_info())