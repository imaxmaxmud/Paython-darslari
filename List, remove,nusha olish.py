# cars=['bmw','mers','audio','jeep']
# print(cars)
# cars.reverse()
# soni=len(cars)
# print('Mashinalar ',cars, soni,' ta mashina bor')

# Range() VA MAX VA MIN DAN FOYDALANISH
# sonlar=list(range(1,10))
# numbers=range(1,10)
# raqami=len(sonlar)
# print(sonlar)
# print(numbers)
# print(raqami)
# toq_sonlar=list(range(1,20,2))
# juft_sonlar=list(range(0,22,2))
# print(toq_sonlar)
# print(juft_sonlar)
# umumiy_yigindi=sum(sonlar)
# print('umumiy yig`i`ndi - > ', umumiy_yigindi, ' ga teng')
# print('maksimal toq son  - >' ,max(toq_sonlar))
# print('minimal juft son - > ',min(juft_sonlar) )
# narhlar=[19287,3487,2346,5678,124,456,123445]
# qimmat=max(narhlar)
# arzon=min(narhlar)
# umumiy=sum(narhlar)
# print('Eng qimmat narh - >', qimmat, ' eng arzon narh - >' ,arzon,' umumiysi - >', umumiy)

# Ro`yhatni kesish olish va nusha olish
# cars=['bmw','jeep','shevrolet','audio','mers','ford']
# #yangi_mashinalar=cars[0:2]
# print(yangi_mashinalar)
# print(cars[0:])
# print(cars[:3])
# print(cars[3:])
# my_cars=cars
# my_cars.remove('jeep')
# print('mening mashinalarim ',my_cars)

#  agar ro`yhatni to`liq kesib olmoqchi bo`lsak 
# my_cars=cars[3:]
# cars.insert(0,'mitsubishi')
# print(cars)
# print(my_cars)

# Tuple bu o`zgarmas ro`yhat
toys=('dino','lizard','snake','bear','car')
# print(toys)
# print(toys[3:])
# print(toys[:3])
# toys.append('allo')
# print(toys)
# print(toys[2:3])
toys=list(toys)
toys.append('laptop')
print(toys)
toys=tuple(toys)
print(toys)







