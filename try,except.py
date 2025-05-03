from datetime import datetime
bugun=datetime.today()
print(bugun.year) 

 
# # yosh=input("Yoshingizni kiriting : ")
# # yosh=int(yosh)


# ism=input(" Ismingizni kiriting : ")
# fam=input(f"Hurmatli {ism} familiyangizni kiriting : ")
# tyil=input(f"Hurmatli {ism} {fam} tug`ulgan yilingizni kiriting : ")

# telefon=input(f"Hurmatli {ism} {fam} siz {tyil} da tug`ilgan ekansiz tel ni kiriting :")


# yosh=input(" Yoshingizni kiriting : ")
# try:
#     yosh=int(yosh)
# except:
#     print(" Siz butun son kiritmadingiz : ")
# else:
#     print(f" Siz {bugun.year-(int(yosh))} da tug`ilgansiz ")
    
# mevalar=['olma','anor','anjir','uzum','gilos']
# try:
#     print(mevalar[4])
# except IndexError:
#     print(f" Ro`yhatda {len(mevalar)} ta meva bor xolos")

# user={
      
#       'username':'SadikovMaxmudjon',
#       'status':'PhD student',
#       'email':'imaxmaxmud@gmail.com',
#       'phone':'+998944048822'
      
#       }
# key=input(" kalit so`zni kiriting Masalan: username, status, email, phone : ")

# try:
#     print(f" Foydalanuvchi : {user[key]}")
    
# excep KeyError:
    
yosh=input(" Yoshingizni kiriting : ")
try:
    yosh=int(yosh)
    
except ValueError:
    print(" Butun son kiriting ! ")
else:
    print(f"Siz {bugun.year-yosh} da tug`ilgansiz")








  