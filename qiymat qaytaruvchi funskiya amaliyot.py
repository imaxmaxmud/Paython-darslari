# def foydalanuvchi(ism,fam,tyil,tjoy,telefon,email=None):
#     foydalan={
#         "ism":ism,
#         "fam":fam,
#         "tyil":tyil,
#         "tjoy":tjoy,
#         "telefon":telefon,
#         "email":email   
#           }
#     return foydalan
# # user1=foydalanuvchi('Mahmud','Sadikov',1991,'Xorazm',4048822,'imaxmaxmud@gmail.com')
# # user2=foydalanuvchi("Ilyos", "Abdullayev", "1991", "Xorazm", 1122525)
# # users=[user1,user2]
# data=[]
# while True:
#     print("\n Quyidagi ma`lumotlarni kiriting :")
#     ism=input(" Ismingniz :")
#     fam=input(" familiyangiz : ")
#     tyil=input(" tugulgan yil : ")
#     tjoy=input(" tugulgan joy : ")
#     telefon=input("telefon : ")
#     email=input(" email : ")
#     data.append(foydalanuvchi(ism, fam, tyil, tjoy, telefon,email))
#     takrorla=input(" Yana ma`lumot kiritasizmi ? yes / no ")
#     if takrorla=='no':
#         break
# for user in data:
#         if user['email']:
#             user['email']=user['email']
#         else:
#             user['email']='mijoz emailini kiritmagan '
#         print(f"{user['ism']} {user['fam']} {user['tyil']} {user['tjoy']} {user['telefon']} {user['email']}")      
  
# def tub_sonlar_top(min, max):
#     tub_sonlar = []
#     for n in range(min, max + 1):
#         tub = True
#         if n == 1:
#             tub = False
#         elif n == 2:
#             tub = True
#         else:
#             for x in range(2, n):
#                 if n % x == 0:
#                     tub = False
#         if tub:
#             tub_sonlar.append(n)

#     return tub_sonlar
    
# print(tub_sonlar_top(8,100))  
    
# print(" Fibanachi ketma-ketligini topish : ")
# def fibonachi(a):
#     sonlar=[]
#     for i in range(a):
#         if i==0 or i==1:
#             sonlar.append(1)
#         else:
#             sonlar.append(sonlar[i-1]+sonlar[i-2])
#     return sonlar
# print(fibonachi(20))
            

    
    
    
    
    
    
    
    
    