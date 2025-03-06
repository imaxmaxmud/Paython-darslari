# print("Yaxshi ko`rgan kitoblaringiz ro`yhatini kiriting ! ")
# savol=" Kitob kiriting yoki stop yozing : "
# kitoblar=[]
# while True:
#     qiymat=input(savol)
#     if qiymat=='stop':
#         break
#     else:
#         kitoblar.append(qiymat)
# print(f"\n Shu kitoblarni yaxshi ko`rasizmi : {kitoblar}")

# 2- Misol Muzey
# print(" Muzeyga kirish narhlari ! ")
# savol=" Yoshingiz kiriting yoki dasturni to`xtatish uchun stop yozing >>> "
# while True:
#     qiymat=input(savol)
#     if qiymat!='stop':
#         if int(qiymat)<=7:
#             print("7 yoshdan kichiklar uchun kirish narhi - 2000 so`m")
#         elif int(qiymat)>7 and int(qiymat)<=18:
#             print("7-18 yoshlar uchun kirish narhi - 3000 so`m")
#         elif int(qiymat)>18 and int(qiymat) <= 65:
#             print("18 - 65 yoshlar uchun kirish narhi - 10000 so`m")
#         elif int(qiymat)>65:
#             print("65 dan kattalar uchun bepul")
#     else:
#         break

# print(" Muzeyga kirish narhlari ! ")
# savol=" Yoshingiz kiriting yoki dasturni to`xtatish uchun stop yozing >>> "
# while True:
#     qiymat=input(savol)
#     if qiymat!='stop':
#         if int(qiymat)<=7:
#            narh=2000
#         elif int(qiymat)>7 and int(qiymat)<=18:
#             narh=3000
#         elif int(qiymat)>18 and int(qiymat) <= 65:
#             narh=10000
#         elif int(qiymat)>65:
#             narh=0
#     else:
#         break
# if narh==0:
#     print(" sizga chipta be`pul ")
# else:
#     print(f" Sizga chipta narhi {narh} so`m ")

# savol = "Yoshingizni kiriting: "

# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit' or qiymat == 'quit':
#         break
#     yosh = int(qiymat)
    
#     if yosh<7:
#         narh = 2000
#     elif 7<=yosh<18:
#         narh = 3000
#     elif 18<=yosh<65:
#         narh = 10000
#     else: narh = 0
    
#     if narh==0:
#         print("Sizga chipta bepul")
#     else:
#         print(f"Chipta {narh} so'm")

# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if int(qiymat)<0 and qiymat=='Exit':
#         break
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")
        
savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat=='exit':
        break
    elif float(qiymat)<0:
        continue # agar foydalanuvchi manfiy son kiritsa tsiklni takrorlaymiz
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")