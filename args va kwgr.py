# def kopaytma(*sonlar):
#     " Sonlarning ko`paytmasini hisoblovchi dastur"
#     m=1
#     for i in sonlar:
#         m*=i
#     return m
# print(kopaytma(11,2,3))

def data_talaba(ism,fam,**info):
    " Talabalar haqida ma`lumot beruvchi funksiya"
    info['ism']=ism
    info['fam']=fam
    return info
talabalar=data_talaba('Mahmud','Sadikov',kurs=4,yili=1991)
print(talabalar)

    