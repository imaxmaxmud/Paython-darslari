from datetime import datetime
bugun=datetime.today()
print(bugun.year) 

 
# # yosh=input("Yoshingizni kiriting : ")
# # yosh=int(yosh)


# ism=input(" Ismingizni kiriting : ")
# fam=input(f"Hurmatli {ism} familiyangizni kiriting : ")
# tyil=input(f"Hurmatli {ism} {fam} tug`ulgan yilingizni kiriting : ")

# telefon=input(f"Hurmatli {ism} {fam} siz {tyil} da tug`ilgan ekansiz tel ni kiriting :")


yosh=input(" Yoshingizni kiriting : ")
try:
    yosh=int(yosh)
except:
    print(" Siz butun son kiritmadingiz : ")
else:
    print(f" Siz {bugun.year-(int(yosh))} da tug`ilgansiz ")