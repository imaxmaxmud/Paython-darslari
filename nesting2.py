# car0={
#       'model':'Gentra',
#       'rangi':'qora',
#       'yili':2024,
#       'probeg':19000,
#       'karobka':'AT',
#       'narhi':15000
#             }
# car1={
#       'model':'Cobalt',
#       'rangi':'GK2',
#       'yili':2020,
#       'probeg':60000,
#       'karobka':'M',
#       'narhi':11000
#             }
# car2={
#       'model':'Spark',
#       'rangi':'oq',
#       'yili':2027,
#       'probeg':72000,
#       'karobka':'M',
#       'narhi':7000
#             }
# i=0
# cars=[car0,car1,car2]
# for car in cars:
#     i=i+1
#     print(f" {i} - {car['model']}"
#       f" {car['rangi']}"
#       f" {car['yili']}"
#       f" {car['karobka']}"
#       f" {car['narhi']}"
#             )
malibus=[]
for i in range(10):
    new_car={
        'model':'malibu',
        'rang':'None',
        'yil':2020,
        'narh':None,
        'km':0,
        'karobka':'AT'  
        }
    malibus.append(new_car)

for malibu in malibus[:5]:
    malibu['rang']='qizil'
for malibu in malibus[5:]:
    malibu['rang']='qora'   
for malibu in malibus[:5]:
     malibu['karobka']='M' 

    
for malibu in malibus:
    if malibu['karobka']=='AT':
        malibu['narh']=40000 
    else:
        malibu['narh']=25000 
for malibu in malibus:
    print(malibu)









