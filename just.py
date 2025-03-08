def data(ism,fam,tyil,manzil):
    malumot={
        'ism':ism,
        'fam':fam,
        'tyil':tyil,
        'manzil':manzil   
        
        }
    return malumot

def data_add():
    " data uchun  ma`lumotlarni kiritish : "
    data_info=[]
    while True:
        print(" quyidagi ma`lumotlarni kiriting ! ")
        ism=input(" ismingizni kiriting : ")
        fam=input(" Fam ni kiriting : ")
        tyil=input(" Tugulgan yilingizni kiriting : ")
        manzil=input(" manzilni kiriting : ")
        data_info.append(data(ism,fam,tyil,manzil))
        takror=input(" Yana qo`shasizmi yes /  no")
        if takror=='no':
            break
    return data_info

def data_print(data):
    print(f"{data['ism'].title()}, {data['fam'].title()}, {data['tyil']}, {data['manzil']} viloyati ")
    
