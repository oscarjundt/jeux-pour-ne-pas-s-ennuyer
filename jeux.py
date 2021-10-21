from tkinter import*
from random import*
ar=0
m=0
hel=0
vien=0
f=Tk()
reinitialiser=Button(f,text="reinitialiser")
reinitialiser.pack()
quitter=Button(f,text="quitter", command=f.quit)
quitter.pack()
a=Canvas(f,width=500,height=500)
a.pack()
a.configure(bg="white")
fond=PhotoImage(file="photo/mdr.png")
personnage=PhotoImage(file="photo/hel.png")
boule=PhotoImage(file="photo/herr.gif")
photo=PhotoImage(file="photo/png.png")
fond2=a.create_image(500/2,500/2,image=fond)
personnage1=a.create_image(100,400,image=personnage)
boule1=a.create_image(100,100,image=boule)
personnage2=a.create_image(100,100,image=personnage)
def avancer(event):
    global ar
    global m
    if(ar<3):
        a.move(personnage2,100,0)
        a.move(boule1,100,0)
        ar=ar+1
    else:
        for i in range(0,3):
            a.move(personnage2,-100,0)
            a.move(boule1,-100,0)
            ar=ar-1
    if(m==3):
        for loop in range(0,3):
            a.move(boule1,0,-100)
            m=m-1
f.bind("<space>",avancer)
def lancer(event):
    global m
    for mdr in range(0,3):
        m=m+1
        a.move(boule1,0,100)
    if(a.coords(boule1)==a.coords(personnage1)):
        print("gagner")
        def eu():
            position1=a.coords(personnage1)
            if(position1[0]<100):
                a.move(personnage1,-100,0)
            if(position1[0]==200):
                a.move(personnage1,-100,0)
            if(position1[0]==300):
                a.move(personnage1,-200,0)
            if(position1[0]>=400):
                a.move(personnage1,-300,0)
            oscar=randint(1,3)
            a.move(personnage1,100*oscar,0)
            position2=a.coords(personnage1)
            if(position1[0]==position2[0]):
                if(position1[0]>=200):
                    a.move(personnage1,-100,0)
                if(position1[0]<200):
                    a.move(personnage1,100,0)
        f.after(1000,eu)
    else:
        a.pack_forget()
        games_over=Canvas(f,height=500,width=500)
        games_over.pack()
        games_over.create_image(500/2,500/2,image=photo)
        def sortie_games_over(event):
            games_over.pack_forget()
            a.pack()
        games_over.bind("<Button-1>",sortie_games_over)
f.bind("<Return>",lancer)
def hello(event):
    global vien
    if(vien<3):
        a.move(personnage1,100,0)
        vien=vien+1
    else:
        for chien in range(0,3):
            a.move(personnage1,-100,0)
        vien=0
a.bind("<Expose>",hello)
def reinitialiser2(event):
    a.move(personnage1,-250,0)
reinitialiser.bind("<Button-1>",reinitialiser2)
f.mainloop()