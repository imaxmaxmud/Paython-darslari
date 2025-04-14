# davlat1=dict({'davlat':'Uzbekistan','poytaxt':'Toshkent','tili':'uzbek'})
# davlat1['dini']='islom'
# print(davlat1['dini'])

# Endi davlat haqida dict tayyorlab ko`ramiz
dv=input(" Davlat kiriting : ") # davlatni kiriting qidirish u/n
davlatlar_bazasi={
    "UZ":{
        'name':'uzbekistan',
        'poytaxt':'Toshkent',
        'til':['uzbek','rus','ingliz','qozoq'],
        'aholi':'38 mln'
        },
    "RU":{
        'name':'Rassiya',
        'poytaxt':'Moskva',
        'til':['rus'],
        'aholi':'150 mln'
        
        },
    "USA":{
        'name':'Amerika',
        'poytaxt':'Washington',
        'til':['Eng','Spain'],
        'aholi':'250 mln'       
        }
    }
dv=dv.upper()
capital=davlatlar_bazasi.get(dv,False)
if capital:
    print(f"{dv} haqidagi ma`lumotlar : {capital}")
    print(f"{dv} ning poytaxti : {capital['poytaxt']}")
else:
    print(" Bunday data yo`q ! ")
    
    
    
    