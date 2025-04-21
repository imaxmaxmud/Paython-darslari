class Talaba:
    " Talaba nomli klass yaratmiz"
    def __init__(self,ism,fam,tyil):
        self.ism=ism
        self.fam=fam
        self.tyil=tyil 
        self.bosqich=1
    def get_name(self):
        return self.ism
    def get_surname(self):
        return self.fam
    def millat(self,millat):
        return self.millat
    def bosqichni_yangilash(self,yangi_bosqich):
        self.bosqich=yangi_bosqich
    def fam_yangilash(self, yangi_fam):
        self.fam=yangi_fam 
    def info_print(self):
        return f"Talaba {self.ism} {self.fam} tugulgan yili {self.tyil} bosqich: {self.bosqich}"
   
class Fan:
    " Fanga oid klass yaratish"
    def __init__(self,nomi):
        self.nomi=nomi
        self.talabalar_soni=0
        self.talabalar=[]
    def add_students(self,talaba):
        self.talabalar.append(talaba)
        self.talabalar_soni+=1
    def get_students(self):
        "Fanga yozilgan talabalar haqida ma`lumot"
        return [ talaba.info_print() for talaba in self.talabalar   ]
    def students_number(self):
        " Fanga yozilgan talabalar sonini ko`rish"
        x=self.talabalar_soni
        return x
    def get_info_students(self):
        return [talaba.info_print() for talaba in self.talabalar]
          
student1=Talaba('Mahmudjon','Sadikov',1991)
# print(student1.info_print())

matematika=Fan("Oliy matematika")
matematika.add_students(student1)
student2=Talaba("Hasan",'Aminboyev',2003)
student3=Talaba('husan','Aminboyev',2003)
matematika.add_students(student2)
matematika.add_students(student3)




