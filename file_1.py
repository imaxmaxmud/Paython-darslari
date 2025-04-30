# filename='C:/Talabalar.txt'
# j=1

# talabalar=[]
# with open(filename) as file :
#     for i in file:
            
#             i=i.replace('1.','')
#             i=i.replace('2.','')
#             i=i.replace('3.','')
#             i=i.replace('4.','')
#             i=i.replace('5.','')
#             i=i.replace('6.','')
#             i=i.replace('7.','')
#             i=i.replace('8.','')
#             i=i.replace('9.','')
#             i=i.replace('0.','')
            
#             i=i.rstrip()
#             i=i.lstrip()
#             talabalar.append(i)
            
            
#             # print(f'{j} chi talaba - > {i} ')
#             # j+=1
# data_students={}        
# t=1
# for m in talabalar:
#        data_students[t]=m
#        t+=1

filename='C:/Talabalar.txt'
with open(filename) as file :
        talabalar=file.readlines()

talabalar=[talaba.rstrip() for talaba in talabalar]
    
print(talabalar)  
    
    
    
    
    
    
    
    
    
    
    
    
    