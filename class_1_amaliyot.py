class User:
    " Foydalanuvchining ma`lumotlarini chiqaruvchi class ! "
    def __init__(self,ism,fam,email,manzil):
        self.ism=ism
        self.fam=fam
        self.email=email
        self.manzil=manzil
    def get_name(self):
        return self.ism
    def get_surname(self):
        return self.fame
    def  info(self):
        return f" foydalanuvchi {self.ism} fam: {self.fam} email: {self.email} manzil: {self.manzil}"
    
users=[]


while True:
    ism=input(" Ism : ")
    fam=input(" Fam : ")
    email=input(" email : ")
    manzil=input("manzil : ")
    users.append(User(ism, fam, email, manzil))
    takror=input(" yanami yoki yo`q yes or no ")
    if takror=='no':
        break

asl=[]
for i in users:
    asl.append(i)

k=1
for user in users:
    print(f"{k} - {user.info()}")
    k+=1    