laptop={}
laptop['Hp']=750
laptop['MacBook']=1500
laptop['Acer']=550
laptop['Dell']=800
laptop['Asus']=600
Narh=0
Noutbuk=[]
# soz=input(' Noutbook ni  kiriting >>> ')
# qidir=laptop.get(soz)
# if qidir==None:
#     print(" Bunday Noutbook yo`q yoki out of store ")
# else:
#     print(f"{soz} ning narhi {laptop['Hp']} ga teng")
zaproslar=int(input('Nechta zapros kiritmoqchisiz >>> '))
for i in range(zaproslar):
        soz=input(f"{i+1}-chi noutbook ni kiriting >>> ")
        qidir=laptop.get(soz)
        if qidir==None:
            print(" Bunday nouttook yo`q ")
        else:
            print(f"{soz} ning narhi {qidir}")
            Noutbuk.append(soz)
            Narh=Narh+qidir
              
if Narh>0:
    print(f"\n {Noutbuk} Noutbuklarining umumiy narhi {Narh} $ ga teng")



