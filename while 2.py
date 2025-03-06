# print(" Yaqin do`stlaringizni ro`yhatini tuzamiz ! ")
# ismlar=[]
# n=1
# while True:
#     savol=f"{n}- do`stingizni kiriting : "
#     ism=input(savol)
#     ismlar.append(ism)
#     takrorlash=input(" Tsiklni davom qilish uchun yes / no  tanla : ")
#     n+=1
#     if takrorlash=='ha':
#         break
# print(" \n Do`stlaringiz : ")
# for ism in ismlar:
#     print(f"\n {ism}")
    
# data=[]
# print(" savol-javob : ")
# savol=input(" Ismingni nima ? ")
# data.append(savol)
# yosh=input(f'Yoshingiz nechida {savol.title()} ? ')
# data.append(yosh)
# fam=input(f'Familiyangiz nima {savol.title()} ')
# data.append(fam)
# kurs=input(f'Kursingiz nechi {savol.title()} ? ')
# data.append(kurs)

# print(data)

# dostlar={}
# ishora=True
# while ishora:
#     ism=input(" Ismingizni kiriting : ")
#     yosh=input(" Yoshingizni kiriting : ")
#     dostlar[ism]=int(yosh)
#     javob=input(" yana ism qo`shasizmi yes / no ")
#     if javob=='no':
#         ishora=False
# for ism,yosh in dostlar.items():
#     print(f"{ism} ning yoshi {yosh} da ")        

# en_uz={}
# ishora=True
# while ishora:
#     eng=input(" Inglizcha so`z kiriting : ")
#     uz=input("O`zbekcha so`z kiriting : ")
#     en_uz[eng]=uz
#     javob=input("Yana so`z kiritasizmi yoki yo`q yes / no ")
#     if javob=='no':
#         ishora=False
# for eng,uz in en_uz.items():
#     print(f"{eng} ning ma`nosi {uz} bo`ladi ")

# cars=['nexia','lacetti','tico','nexia','damas','nexia','cobalt','Gentra']
# while 'nexia' in cars:
#     cars.remove('nexia')
    
# print('Mashinalar ro`yhatini tuzamiz !  ')
# cars=[]
# ishora=True
# # savol=input(" Mashina kiriting : ")
# n=1
# while ishora:
#     qiymat=input(f"{n} - Mashinani kiriting : ")
#     cars.append(qiymat)
#     takrorlash=input(" Yana mashina kiritasizmi yes / no : ")
#     n+=1
#     if takrorlash=='no':
#         ishora=False
# print(cars)
# ochir=input(" Keraksiz mashinani yoz o`chirish uchun : ")
# while ochir in cars:
#     cars.remove(ochir)
# print(cars)

# talabalar=['ALi','Vali','Husan','Hasan','Mahmud']
# baholangan_talabalar={}
# while talabalar:
#     talaba=talabalar.pop()
#     baho=input(f"{talaba.title()} ga baho qo`ying : ")
#     print(f"{talaba.title()} ning bahosi {baho}")
#     baholangan_talabalar[talaba]=int(baho)
    
# eng=['apple','banana','laptop','car']
# en_uz={}
# while eng:
#     en=eng.pop()
#     mano=input(f"{en} so`zining mano`sini yozing ")
#     en_uz[en]=mano
    
    
    

    
    
    