def data_student(ism,fam,kurs,field,manzil):
    talaba={
        'ism':ism,
        'fam':fam,
        'kurs':kurs,
        'field':field,
        'manzil':manzil
  
        }
    return talaba
def talaba_add():
    talabani_kirit=[]
    while True:
            ism=input(" Ism : ")
            fam=input(" Fam : ")
            kurs=input(" Kurs : ")
            field=input(" field : ")
            manzil=input(" Manzil : ")
            talabani_kirit.append(data_student(ism, fam, kurs, field, manzil))
            takror=input(" yes / no : ")
            if takror=='no':
                break
    return talabani_kirit
print(talaba_add())



