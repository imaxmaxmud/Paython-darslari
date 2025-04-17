# # Lugatlar bilan ishlash
# # talaba_1={}
# # talaba_1['ism']="Sadikov Mahmudjon"
# # talaba_1['kurs']=4
# # talaba_1['yonalish']="AX"
# # talaba_1['t_yil']=1991
# # del talaba_1['ism']
# talaba={
#         'mahmud':'iphone',
#         'sarvar':'samsung a25',
#         'ali':'redmi',
#         'vali':'huwai',
#         'hasan':['iphone','samsung']
#         }
# # natija=talaba.get('mahmud',False)
# # if natija:
# #     print(f"{natija}")
# # else:
# #     print("Bunday shahs yo`q")
# for kalit,qiymat in talaba.items():
#     if qiymat==1:
#         print(f"{kalit} ning telefoni {qiymat}")
#     else:
#         print(f"{kalit} ning telefonlari {qiymat}")

bozorlik={'olma':5000,'anor':4000,'nok':3000,'anjir':1000,'behi':6000}
spiska=['banan','behi','nok']
for mahsulot in spiska:
    if mahsulot in bozorlik:
        print(f"{mahsulot} bor va uning narhi {bozorlik[mahsulot]} ")
    else:
        print(f"{mahsulot} ni ham olib keling")


