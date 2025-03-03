# ism=input(' Ismingizni kiriting ? ')
# savol=f"Salom {ism.title()} yoshingiz nechida ? "
# yosh=input(savol)
# yosh=int(yosh)
# height=input(" Bo`yingiz nechi meter ? ")
# height=float(height)

# ismingiz=input('Ismingizni kiriting - ')
# savol=f"Salom {ismingiz.title()} yoshingiz nechida ? "
# yosh=input(savol)
# yosh=int(yosh)

# son=1
# while son<=5:
#     print(son, end=' ')
#     son=son+1
# print("tsikl tugadi")
    
# print(" Kiritilgan dasturning kvadratini chiqaruvchi dastur ")
# savol=" son kiriting yoki dasturni to`xtatish uchun <exit> so`zini yozing : "
# qiymat=''
# while qiymat!='exit':
#     qiymat=input(savol)
#     if qiymat!='exit':
#         print(f" {float(qiymat)} ning kvadrati"
#               f" {float(qiymat)**2} ga teng")
# print(" \n Dastur tugadi")

# s=0
# print(" Kiritilgan sonning yigindisini hisoblovchi dastur ")
# savol=" son kiriting yoki stop so`zini yozing "
# qiymat=''
# while qiymat!='stop':
#     qiymat=input(savol)
#     if qiymat != 'stop':
#         s=0
#         for i in range(int(qiymat)):
#             s=s+i
#             print(f"{int(i)} sonining sonlar yigindisi {s}")
            
#  Ishora
# print(" sonning kvadratini hisoblovchi dastur ! ")
# savol=' Son kiriting yoki stop so`zini yozing - > '
# ishora=True
# while ishora:
#     qiymat=input(savol)
#     if qiymat=='stop':
#         ishora=False
#     else:
#         print(float(qiymat)**2)
# print(" Dastur to`xtadi ")

# Break
# print(" sonning kvadratini hisoblovchi dastur ! ")
# savol=' son kiriting yoki stop so`zini yozing : '
# while True:
#      qiymat=input(savol)
#      if qiymat=='stop':
#          break
#      else:
#          print(float(qiymat)**2)
# print("dastur tugadi")

# Break for uchun ishlatish
# n=int(input(" son ni kiriitng >>> "))
# for i in range(n):
#     if i==n:
#         break 
#     else:
#         print(f"{i} ning kvadrati {i**2} ga teng")

# Continue ni ishlatish
# n=int(input(" son ni kiriitng >>> "))
# for i in range(n):
#     if i==5:
#         continue 
#     else:
#         print(f"{i} ning kvadrati {i**2} ga teng")

#  Continue while
son=0
print(" toq sonlarni chiqaruvchi dastur ")
while son<10:
    son=son+1
    if son%2!=0:
        continue
    else:
        print(son)




