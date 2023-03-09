from tkinter import *
k=0
def klikker(event):
    global k
    k+=1
    btn.configure(text=k)
def klikkermaha(event):
    global k
    k-=1
    btn.configure(text=k)
def sada_plus(event):
    global k
    k+=100
    btn.configure(text=k)
def tekst_to_lbl(event):
    t=ent.get()
    lbl.configure(text=t)
    ent.delete(0,END)#2,7

aken=Tk()
aken.geometry("400x500")
aken.title("minu esimene aken")
lbl=Label(aken,text="Elemendid",bg="silver",fg="#AA4A44",font="Arial 20",height=5,width=15)
btn=Button(aken,text="vajutage nuppu",font="Arial 24",relief=GROOVE)#SUNKEN, RAISED
ent=Entry(aken,fg="blue",bg="lightblue",width=15, font="Arial 20",justify=CENTER)


btn.bind("<Button-1>",klikker)#left click mouse
btn.bind("<Button-3>",klikkermaha)#left click mouse
btn.bind("<Button-2>",sada_plus)#left click mouse
ent.bind("<Return>", tekst_to_lbl)#
lbl.pack()
btn.pack()
ent.pack()
aken.mainloop()
