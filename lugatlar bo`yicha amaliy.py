# en_uz={
#        'apple':'olma',
#        'banana':'banan',
#        'apricot':'o`rik',
#        'cherry':'olcha',
#        'watermelon':'tarvuz',
#        'melon':'qovun',
#        'laptop':'noutbuk',
#        'room':'xona',
#        'home':'uy',
#        'father':'ota',
#        'mather':'ona'  ,    
#        'car':'mashina',
#        'key':'kalit',
#        'city':'shahar'
#        }
# bosh={}
# for i in sorted(en_uz):
#     print(f"{i}  >>>  {en_uz[i]}")
davlatlar={
    'Uzbekistan':'Tashkent',
    'GB':"England",
    'USA':"Newyork",
    'Germany':'Berlin',
    'Kanada':'Ottava',
    'Turkemnistan':'Ashgabat',
    'Turkey':'Istanbul',
    'Italy':'Rim',
    'France':'Paris',
    'Spain':'Barcelona',
    'Eron':'Tehron',
    'South Korea':'Seoul',
    'Australia':'Sydney'    
    }
print(" Dunyo davlatlari: ")
for i in sorted(davlatlar):
    print(f" {i}")
print(" Davlatlarning poytaxtlari: ")
for j in davlatlar.values():
    print(f" {j}")
qidir=input(" Qaysi davlatning poytaxtini bilishni xohlaysiz ? ")
poytaxt=davlatlar.get(qidir)
if poytaxt==None:
    print('Bu davlat bizning bazada yo`q')
else:
    print(F"{qidir} ning poytaxti {poytaxt.title()}")
    
