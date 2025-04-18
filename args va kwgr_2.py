#  bugungi darsda *args bilan ishlaymiz

# def summa(*sonlar):
#     " Istalgancha sonlarning yigindisini chiqarish funksiyasi ! "
#     yigindi=0
#     for son in sonlar:
#         yigindi+=son
#     return yigindi
# i=range(10)
# m=summa(i)
# print(m)

#  ** kwgrs ni ishlatish

def avto_info(komponiya,model,**malumotlar):
    " Avto haqida ma`lumot chiqaruvchi funksiya" 
    malumotlar['komponiya']=komponiya
    malumotlar['model']=model
    return malumotlar
avto1=avto_info('GM', 'Gentra',rangi='Qora',uzatma='AT',probeg=20000,narhi=15000)
print(avto1)