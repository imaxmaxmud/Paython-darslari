# print(" Mijozlarning orderlarini qabul qilish")
# ishora=True
# zakazlar=[]
# n=1
# while ishora:
#   qiymat=input(f"{n} - ovqatni kiriting :")
#   zakazlar.append(qiymat)
#   javob=input(" Yana ovqat kiritasizmi yes / no : ")
#   n+=1
#   if javob=='no':
#     ishora=False
# print(zakazlar)

# print('e-bozor ning mahsulotlar va narhlari : ')
# e_mah=[]
# n=1
# ishora=True
# while ishora:
#     mah=input(f"{n} - chi mahsulotni kiriting : ")
#     e_mah.append(mah)
#     takror=input(" Yana mahsulot kirititasizmi yes / no : ")
#     n+=1
#     if takror=='no':
#         ishora=False
# print(f"{e_mah}")    

# print(" Endi Mahsulotning narhlari bilan tanishamiz : ")
# j=1
# narh=[]
# umumiy={}
# while e_mah:
#     mahsulot=e_mah.pop()
#     narh=input(f"{mahsulot } uchun narh kiriting : ")
#     umumiy[mahsulot]=int(narh)
# bozorlik=['olma','banan']
# for mah, narh in umumiy.items():
#     if mah in bozorlik:
#         print(f"{mah} ning narhi {umumiy[mah]} ga teng")
#     else:
#         print(f" {mah} mahsuloti hozirda yo`q ")
        
buyurtmalar = ['olma','anjir','uzum','qovun']
mahsulotlar = {'olma':20000,
               'shaftoli':25000,
               'tarvuz':18000,
               'uzum':22000}

while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narh = mahsulotlar[buyurtma]
        print(f"{buyurtma.title()} - {narh} so'm")
    else:
        print(f"Bizda {buyurtma} yo'q")

    
