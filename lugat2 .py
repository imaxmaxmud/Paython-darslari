en_uz={'banana':'banan','apple':'olma','apricot':'o`rik','melon':'qovun'}

n=int(input(" Nechta so`z kiritmochisiz >>> "))
for i in range(n):
    soz=input(f"{i+1} chi so`zni kiriting >>> ")
    topildi=[]
    k=0
    j=0
    for sozlar in en_uz:
        if sozlar==soz:
        
            topildi.append(en_uz[soz])
            j=j+1
        else:
                k=k+1
                if j>0:
                    print(f"{soz} so`zining ma`nosi {topildi}")
                else:
                        print(f" Lug`atda bunday so`z yo`q ")

      