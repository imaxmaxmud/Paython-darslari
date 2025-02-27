ism='Mahmudjon'
fam='Sadikov'
ism_fam=f"{ism}{fam}"
katta_hafrlar=ism_fam.upper()
kichkina_hafrlar=ism_fam.lower()
title_ish=f'{ism.title()} {fam.title()}'
print(katta_hafrlar)
print(kichkina_hafrlar)
print(title_ish)

meva='    olma    '
print(meva)
print("men "+ meva.lstrip() + " yaxshi ko`raman")
 
text="""O'quv faoliyati bilimlarni qurishni talab qiladimi?
Bilimni qurishni talab qiladigan tadbirlar o'quvchilardan ma'lumot yoki g'oyalarni sharhlash, tahlil qilish, sintez qilish yoki baholashni so'raydi.
•	Interpretatsiya to‘g‘ridan-to‘g‘ri ma’nodan tashqari xulosalar chiqarish demakdir. Misol uchun, o'quvchilar tarixiy davr tavsifini o'qib, o'sha paytda yashagan odamlar nima uchun o'zlarini shunday tutganliklarini xulosa qilishlari mumkin.
•	Tahlil deganda bir butunning qismlarini va ularning bir-biriga munosabatini aniqlash tushuniladi. Misol uchun, o'quvchilar ko'chib yuruvchi qushlarga qaysi biri eng ko'p ta'sir qilishini aniqlash uchun mahalliy atrof-muhit omillarini o'rganishlari mumkin.
"""
print(text.replace(" ","" ))

