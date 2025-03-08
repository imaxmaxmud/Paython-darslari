
# *args istalgancha argument qabul qiluvchi funksiya
# def summa(son):
#     " summani hisoblovchi funksiya "
#     yigindi=0
#     for i in son:
#         yigindi+=i
#     return yigindi
# print(summa(5))

# def summa(x,y, *sonlar):
#     " Kiritilgan sonlarning yig`indisini hisoblaydigan funksiya "
#     return x+y+sum(sonlar)
# print(summa(1,2,4,5,6))

# talab=[]
# k=1
# while True:
#     ism=input(f"{k} - talabani kiriting : ")
#     talab.append(ism)
#     takror=input(" Yana ism qo`shasizmi : yes / no ")
#     k+=1
#     if takror=='no':
#         break
# def baholash(ism,**ismlar):
#     " Kiritilgan talabalarning ismlarini baholash : "
#     yangi=[]
#     for ism in ismlar:
#         yangi.append(ism)
#         baho=input(f"{ism} ning bahosini tushing : ")
#         yangi[ism]=int(baho)
#     return yangi
# print(baholash(talab))


# def avto_info(kompaniya,model, **malumotlar):
#     "kwards ni ihsga tushurish uchun "
#     malumotlar['komaniya']=kompaniya
#     malumotlar['model']=model
#     return malumotlar
# avto1=avto_info("GM", 'lacetti', rangi='oq',yili=2020)
# print(avto1)










