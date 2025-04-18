ismlar=[]
i=1
while True:
    ism=input(f"{i} chi talabani kiriting : ")
    ismlar.append(ism)
    takror=input(" Yana ism kiritasizmi yes or no : ")
    i+=1
    if takror=='no':
        break
def bahola(ismlar):
    " Talabalarning bahosini tushish funksiyasi ! "
    baholar={}
    while ismlar:
        ism=ismlar.pop()
        baho=input(f"Talaba {ism.title()} ning bahosini kiriting : ")
        baholar[ism]=int(baho)
    return baholar
scores=bahola(ismlar[:])  # [:] bu belgi orqali biz ismlar degan dan nusha ko`chiramiz
print(scores)

talabalar=ismlar[:]
