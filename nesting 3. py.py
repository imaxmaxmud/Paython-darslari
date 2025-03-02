# dasturchilar={
#     'Mahmudjon':['python','c++','hp'],
#     'Gavhar':['java','delphi','dell'],
#     'Ibrohim':['php','laravel','Apple'],
#     'Imona':['html','ccs','Acer']  
    
#     }
# i=0
# for ism,tillar in dasturchilar.items():
#     i=i+1
#     print(f"\n{i} - {ism.upper()} dasturlash tillarini biladi:  ", end='')
#     for til in tillar:
#             print(f"{til.title()} ",end='')

hamkasblar={
    'ali': {'familiya':'valiyev',
           'tyil':1991,
           'malumot':'oliy',
           'tillar':['php','python']
            },
    'vali': {'familiya':'sadikov',
           'tyil':2001,
           'malumot':'orta',
           'tillar':['laravel','dango']
            }
    }
for ism, info in hamkasblar.items():
    print(f" \n {ism.title()} {info['familiya']} {info['tyil']} {info['malumot']}"
          f" \n Quyidagi dasturlash tilllarini biladi  ")
    
    for til in info['tillar']:
        print(f"{til}")
    