filenomi='C:/data.txt'
with open(filenomi,'a') as file :
   ism=input('Ismingizni kiriting : ')
   fam=input('Familiyangizni kiriting : ')
   manzil=input(" Manzilingizni kiriting : ")
   telefon=input(" Telfon raqamingizni kiriting : ")
   tyil=input(' Tug`ulgan yilingizni kiriting : ')
   file.write(ism+' '+fam+' '+manzil+' '+telefon+' '+tyil+'\n')
   
   