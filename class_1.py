class Talaba:
    " Bu klassda talabalar haqida ma`lumotlar kiritladi !"
    def __init__(self,ism,fam,tyil):
        self.name=ism
        self.surname=fam
        self.year=tyil
    def tanishtir(self):
        print(f" talaba: {self.name} familiyam {self.surname} tug yilim {self.year}")
    def get_name(self):
        return self.name
    def get_age(self,yil):
        return yil-self.year 
    def get_surname(self):
        return self.surname
        
        
talaba1=Talaba('Mahmud','Sadikov',1991)
talaba2=Talaba('Husan', "Aminov", 2003)
talaba3=Talaba("Hasan",'Aminov',2003)
talabalar=[talaba1,talaba2,talaba3]

print(talaba1.get_name())

# users=[]    
# while True:
#     ism=input(" Ismingiz  : ")
#     fam=input(" Fam : ")
#     tyil=input(" Year : ")
#     users.append(Talaba(ism, fam, tyil))    
#     takror=input(" yanami yoki stop yes or no : ")
#     if takror=='no':
#         break
# k=1
# for talaba in users:
#         print(f"{k} - ",end='')
#         f" {k} -- talaba  {talaba.tanishtir()} "
#         k+=1    


