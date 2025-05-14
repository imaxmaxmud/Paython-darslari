# filename='C:/Data.txt'

# try:
#    with open (filename) as f:
#        ochish=f.read()
# except FileNotFoundError:
#     print('Bunday file yo`q')
# else:
#     print(ochish)
       
import json 
talaba1={
    'ism':'Sadikov Mahmud',
    'kurs':'4-kurs'
    }
talaba2={
    'ism':'Ali Vali',
    'kurs':'2-kurs'
    }
talaba4={
    'ism':'Akmuratov Ibrohim',
    'kurs':'2-oy boqcha tarbiyalanuvchisi'
    }

talabalar=[talaba1,talaba2,talaba4]
for talaba in talabalar:
    talabalar_json=json.dumps(talaba)
    print(talabalar_json)
for talaba in talabalar_json:
        
        print(talaba['ism'])




