# def bahola(ismlar):
#     " Talabalarni baholash funksiyasi ! "
#     baholar={}
#     m=len(ismlar)
#     for ism in ismlar:
#         baho=int(input(f"{m}. {ism.title()} - ning bahosini qo`ying : "))
#         baholar[ism]=baho
#         m-=1
#     return baholar

# print(" Talabalarni kiriting ")
# talabalar=[]
# ishora=True
# k=1
# while ishora:
#     ism=input(f"{k} - talabani kiriting : ")
#     talabalar.append(ism.title())
#     takrorla=input(" Yana kiritasizmi yes/ no : ")
#     k+=1
#     if takrorla=='no':
#         ishora=False
    
# asl=[]
# for i in talabalar:
#     asl.append(i)

# baholar=bahola(talabalar)

#  1- Amaliyot 

# def katta_qil(ismlar):
#     " Ismlarning faqat bosh harflarini katta qiluvchi funskiya"
#     katta=[]
#     while ismlar:
#         ism=ismlar.pop()
#         katta.append(ism.title())
#     return katta
        
# data=[]
# k=1
# while True:
#     ism=input(f"{k} - ismni kiriting : ")
#     data.append(ism)
#     k+=1
#     takrorla=input(" Yana ism  qo`shasizmi : yes or no : ")
#     if takrorla=='no':
#         break
# print(f" Asl ismlar : {data}")
# print(f" katta bo`lgani {katta_qil(data)} ") 