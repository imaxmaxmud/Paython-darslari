# narh=15000
# choy=int(input("choyni kiriting "))
# salat=int(input("salatni kiriting ")) 
# non=int(input("noni kiriting ")) 
# kompot=int(input("kompotni kiriting " ))
# assorti=int(input("assortini kiriting "))
# print("\n Mijoz bergan zakazlar \n")
# if choy:
#     print(" choy oldi")
#     narh=narh+3000
# if salat:
#     print(" salat oldi")
#     narh=narh+3000
# if non:
#     print(" non oldi")
#     narh=narh+3000
# if kompot:
#     print(" kompot oldi")
#     narh=narh+3000
# if assorti:
#     print(" assorti oldi")
#     narh=narh+3000
# print(f"Jami summa {narh}")

# menu=['osh','qazonkabob','shashlik','somsa','norin']
# ovqat=input('Nima ovqat yeysiz ? >>> ')
# if ovqat.lower() in menu:
#     print(" Buyurtma qabul qilindi ")
# else:
#     print(" Afsuski bizda bu ovqat hozir tugagan ")
# if ovqat.lower() not in menu:
#     print(" yo`q ")
# else:
#     print(" Bor")
# menu=['osh','shashlik','somsa','barak','norin']
# buyurtmalar=['osh','somsa','manti','shashlik']
# for taom in buyurtmalar:
#     if taom in menu:
#         print(f" Menuda {taom} bor")
#     else:
#         print(f" Kechirasiz, menuda {taom} yo`q")
    

restaran_alibaba=['somsa','manti','osh','palov','barak','shashlik']
zakaz=[]
for order in range(3):
    zakaz.append(input(" Zakaz ovqatlarini kiriting >>> "))
print(f"\n")
if zakaz:
    for ovqat in zakaz:
        if ovqat in restaran_alibaba:
            print(f" Buyurt uchun {ovqat}  qabul qilindi ")
        else:
            print(f" Kechirasiz menuda {ovqat} yo`q ")
        




