def avto_info(komponiya,model,rangi,uzatma,yili,narhi=None):
    "Mashinalarning ma`lumotlarini beruvchi funksiya"
    avto={
        'komponiya':komponiya,
        'model':model,
        'rangi':rangi,
        'uzatma':uzatma,
        'yili':yili,
        'narhi':narhi
        }
    return avto
cars=[]
while True:
    print(" Quyidagi ma`lumotlarni kiriting : ")
    komponiya=input(" Ishlab chiqaruvchi kompaniyani kiriting : ")
    model=input(" Modelini kiriting : ")
    rangi=input(" Rangini kiriting : ")
    uzatma=input(" Uzatmani kiriting AT yoki Mehanika : ")
    yili=input(" Ishlab chiqarilgan yilini kiriting : ")
    narhi=input(" Narhini kiriting : ")
    cars.append(avto_info(komponiya, model, rangi, uzatma, yili))
    takror=input(" Yana ma`lumot kiritasizmi yes or no : ")
    if takror=='no':
        break

avtolar=cars
for i in avtolar:
    print(f"{i['komponiya']}")
    