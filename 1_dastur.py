from datetime import datetime 


# def yoshni_chiqar(yil):
#     " Tuglgan yilni kiritsa yoshni hisoblovchi dastur ! "
#     bugun=datetime.today()
#     natija=bugun.year-int(yil)
#     print(f"Siz {natija} yoshdasiz")
    
# t_yil=input(" Tugulgan yilingizni kiriting : ")
# natija=yoshni_chiqar(t_yil)

from tkinter import *
oyna=Tk()
oyna.title("Mening birinchi dasturim : ")
oyna.geometry("500x400")
yil=Entry()
yil.place(x=75,y=50,width=150,height=30)
def yoshni_chiqar():
    bugun=datetime.today()
    natija.config(text=bugun.year-int(yil.get()))
    return natija

    


tugma=Button(text="Hisoblash", command=yoshni_chiqar)
tugma.place(x=90,y=90,width=120, height=40)
natija=Label(text="Natija",bg="white",font='red')
natija.place(x=90,y=135,width=120,height=40)



oyna.mainloop()


