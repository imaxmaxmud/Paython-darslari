# ismlar=[]
# j=0
# soni=input("n ni kiriting : ")
# for i in range(int(soni)):
#     ismlar.append(input('Salom do`stim - '))
#     j=i+1
# print(f"\n {ismlar}")
# print(f"\n {j} marta takrorlandi")

# a=input("a ni kiriting : ")
# b=input("b ni kiriting : ")
# toq=[]
# kub=[]
# for i in range(int(a),int(b),2):
#     # if i%2!=0:
#         toq.append(i)
#         kub.append(i**3)
# print(toq)
# print(kub)

kinolar=[]
kinolar_soni=input("Kinolar soni : ")
for i in range(int(kinolar_soni)):
    kinolar.append(input(f"{i+1} chi kinongizni kiriting : "))
    
print(kinolar)

suhbatlar_soni=input(" bugun suhbatlashganlar soni : ")
kimlar=[]
for i in range(int(suhbatlar_soni)):
    kimlar.append(input(f"{i+1} chi suhbatim : "))
    
print(kimlar)