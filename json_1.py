import requests
import json
import googlemaps 

wikiurl=" https://uz.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles=Python"

wikiurl_json=json.dumps(wikiurl)
response=requests.get(wikiurl)
print(json.dumps(response.json()))



# talaba={
#         'ism':"Sadikov mahmudjon",
#         'manzil':'Xorazm viloyati Yangibozor tumani',
#         'telefoni':'+998944048822',
#         'tyil':' Tug`ulgan yili',
#         'Dasturlash tillari':['C++','Java','Python']     
        
#         }

# talaba_json=json.dumps(talaba)
# talaba2=json.loads(talaba_json)









# talaba_json=json.dumps(talaba)


# with open('C:/fff.txt','a') as f:
#     json.dump(talaba,f)
   
    





# talaba2=json.loads(talaba_json)

# numbers=[]
# i=0
# while i<=10:
#         numbers.append(i)
#         i+=1
        

# print(numbers)

# numbers_json=json.dumps(numbers)


# numbers_2_json=json.loads(numbers_json)






















