# yosh=int(input(" Yoshingizni kiriting : "))
# if yosh<=4:
#     print(" Sizga kirish tekin")
# elif yosh<=12:
#     print(" Sizga kirish 5000 so`m ")
# else:
#     print(" Sizga kirish 10000 so`m ")
    
# yosh=int(input(" Yoshingizni kiriting : "))
# if yosh<=5:
#     narh=0
# elif yosh<=10:
#     narh=5000
# elif yosh<=15:
#     narh=7000
# elif yosh<=18:
#     narh=10000
# else:
#     narh =20000
# print(f" \n Sizga kirish narhi {narh} so`m ") 

# kun=input(" Bugun nima kun ? >>> ")
# if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#     print(" Bugun dam olish kuni ")
# else:
#     print(" Bugun ish kuni")

# kun=input(" Bugun nima kun ? >>> ")
# if kun.lower()=='shanba' and kun.lower()=='yakshanba':
#     print(" Bugun dam olish kuni")
# else:
#     print(" Bugun ish kuni")
kun=input(" bugun nima kun ? ")
harorat=float(input("Harorat nechi bugun? "))
if (kun.lower()=='dushanba' or kun.lower()=='seshanba' or kun.lower()=='chorshanba' or
kun.lower()=='payshanba' or kun.lower()=='juma' ) and harorat<=30:
    print(" Bugun ish kuni ! ")
else:
    print(" Bugun dam olish kuni")

    
    
    
    
    