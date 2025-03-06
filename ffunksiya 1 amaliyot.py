# def salom_ber(a):
#     " Salom beruvchi funksiya"
#     print(f" Assalomu alaykum {a.title()} aka ")
    
# salom_ber('Mahmudjon')

# def kvadrat(a):
#     "Sonning kvadratini hisoblovchi funksiya "
#     print(f"{a} ning  kvadrati {a**2} ga teng ")

# kvadrat(10)

# def summa(a):
#     """ Berilgan sonning summasini hisoblovchi dastur """
#     yig=0
#     for i in range(a+1):
#         yig=yig+i
#     print(f"{a} ning umumiy yigindisi {yig} ga teng")
# summa(10)
# summa(10000)

# def toliq_ism_fam(ism,fam):
#     "To`liq ismingz va familiyaingizni chiqaruvchi dastur"
#     print(f"Foydalanuvchi {ism.title()}")
#     print(f"Foydalanuvchi {fam.title()}")

# toliq_ism_fam('Mahmudjon','Sadikov')
# toliq_ism_fam(fam='Sadikov',ism="Mahmudjdf")

# def juft_toq(a):
#     " sonning juft yoki toqligini tekshirish"
#     if a%2==0:
#         print(f"{a} - juft son")
#     else:
#         print(f"{a} -  toq son")
        
        
# juft_toq(11)
# n=1
# while n:
#     son=int(input(" son kiriting : "))
#     juft_toq(son)
#     takror=input(" Yana son kiritasizmi ?  yes / no : ")
#     if takror=='no':
#         n=0

# def katta_kichik(a,b):
#     " Kiritilgan sonnig katta kichikligini hisoblovchi dastur "
#     if a==b:
#        print(" sonlar teng ")
#     else:
#        katta=max(a,b)
#        kichik=min(a,b)
#        print("katta",katta)
#        print("kichik",kichik)
            
# katta_kichik(12,12)

def bolish(a):
    " Sonning 2 dan 10 gacha bo`lgan oraliqda bo`linishini tekshirish "
    for i in range(2,11):
        if a%i==0:
            print(i)
bolish(100)


