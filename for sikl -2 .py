# mehmonlar=['Mahmudjon','Jasur','Ali','Vali','Ibrohim','Imona']
# # for mehmon in mehmonlar:
# #     print("Salom", mehmon)

# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon}, sizni to`yga taklif qilamiz")
#     print("Hurmat bilan, Sadikovlar oilasi \n")
    
# sonlarning kvadratini chiqarish
# a=input(" birinchi sonni kiriting : ")
# b=input(" Ikkinchi sonni kiriting : ")
# sonlar=list(range(int(a),int(b)))
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2} ga teng ")

# n=input("n ni kiriting : ")
# sonlar_kvadrati=[]
# sonlar=list(range(int(n)))
# for son in sonlar:
#     sonlar_kvadrati.append(son**2)
    
# print(sonlar_kvadrati)

dostlar=[]
dostlar_soni=input("Do`stlaringiz sonini kiriting : ")
for soni in range(int(dostlar_soni)):
    dostlar.append(input(f"{soni+1} do`stingizni kiriting - > "))

print(f"\n {dostlar}")