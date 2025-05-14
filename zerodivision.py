n=input(" Butun son kiriting : ")
try:
    n=int(n)
    x=20/n
except ValueError:
    print("Faqat butun son kiriting ! ")
except ZeroDivisionError:
    print(f'butun sonni ni 0 ga bo`lib bo`lmaydi ! ')
else:
    print(f"Natija {x} ga teng")