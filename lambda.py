# son1=lambda x: x+1
# natija=son1(10)
# print(natija)

# son2=lambda x,y: (x**2) + (y**2)
# natija=(son2(3,4))
# print(int(pow(natija,0.5)))


# for i in range(11):
#     print(i**2)
    


def kvadrat(n):
    " 0 dan n gacha bo`lgan sonlarning kvadratini hisoblovchi dastur"
    n=int(input(" n ni kiriting : "))
    kvadrat=list(map(lambda i: i**2, range(n)))
    print(kvadrat)
kvadrat(11)
    

