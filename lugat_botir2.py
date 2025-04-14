data_students={
    "talaba1":{
    "fam":"Sadikov",
    "Ism":"Mahmudjon",
    "Kursi":"4",
    'Yonalish':"AX",
    'guruh':'231'   
    },
    "talaba2":{
    "fam":"Ramazonov",
    "Ism":"Aziz",
    "Kursi":"4",
    'Yonalish':"AX",
    'guruh':'231' 
     },
    "talaba3":{
    "fam":"Xudayberdiyev",
    "Ism":"Aziz",
    "Kursi":"4",
    'Yonalish':"AX",
    'guruh':'231' 
     }
    }
search=input("Talabani kiriting : ") # talaba ID sini kiriting
search=search.lower()
natija=data_students.get(search, False)
if natija:
    print(f"{natija['Ism']} haqida ma`lumotlar :  {natija}")
else:
    print(" bunday talaba yo`q yoki to`g`ri ID kiriting ! ")