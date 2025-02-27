# matn=input('Matnni kiriting - > ')
# kerakli_harf=input("qaysi harfni qidirish va sanash kerak - > ")
# takror_harf_soni=matn.count(kerakli_harf)
# print(takror_harf_soni)

#barcha harflarni katta yoki kichik qilish
# matn=input(" Matnni kiriting - >")
# katta=matn.upper()
# kichik=matn.lower()
# print("katta harflar", katta, "kichik", kichik)

#polindromligini tekshirish
# text=input("Matnni kiriting :").replace(' ','').lower()
# if text==text[::-1]:
#     print('BU matn palindrom!')
# else:
#     print("Bu matn palindrom emas!")
    
# keraksiz so`zni almashtirish
# text=input(" Matnni kiriting ")
# kerakli=input('Kerakli so`zni kiriting ')
# keraksiz=input('Keraksiz so`zni kiriting ')
# tayyor=text.replace(keraksiz,kerakli)
# print(tayyor)
text = input("Matn kiriting: ")
letters_only = ''.join(filter(str.isalpha, text))
print("Faqat harflar:", letters_only)


