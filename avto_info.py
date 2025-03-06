# def oraliq(min,max):
#     sonlar=[]
#     while min<max:
#         sonlar.append(min)
#         min+=1
#     return sonlar
# print(oraliq(0,20,2))
# print(list(range(0,20,2)))

# def kattasi(a,b):
#     if a>b:
#         eng=a
#     else:
#         eng=b
#     return eng

# a=int(input(" birinchi sonni kiriting : "))
# b=int(input(" Ikkinchi sonni kiriting : "))
# print(f"Katta son {kattasi(a,b)}")

def avto_info(kompaniya,model,rangi,korobka,yili,narhi=None):
    avto={
        'kompaniya':kompaniya,
        'model':model,
        'rangi':rangi,
        'korobka':korobka,
        'yili':yili,
        'narhi':narhi
        }
    return avto
print(" Saytimizdagi avtolar ro`yhatini shakllantiramiz ! ")
avtolar=[]
while True:
    print(" \n Quyidagi ma`lumotlarni kiriting",end='')
    kompaniya=input(" Ishlab chiqaruvchi :")
    model=input(" Model : ")
    rangi=input(' Rangi : ')
    korobka=input('korobka : ')
    yili=input(' yili : ')
    narhi=input(' narhi : ')
    avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili,narhi))
    javob=input(" Yana mashina kiritasizmi yes / no ")
    if javob=='no':
        break 
print(" salonimizdagi avtolar : ")
for avto in avtolar:
    if avto['narhi']:
        narhi=avto['narhi']
    else:
        narhi='noma`lum'
print(f"{avto[kompaniya]} {avto[model]} {avto[rangi]} {avto[korobka]} {avto[yili]} {avto[narhi]}")
