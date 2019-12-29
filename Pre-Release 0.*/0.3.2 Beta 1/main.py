from tkinter import *
import random
import time

root = Tk()
root.configure(background="LightSkyBlue")
x=root.winfo_screenwidth()
y=root.winfo_screenheight()
root.title("RandomIt! --by iwtywai")
root.geometry("1024x768")

colors=["red","green","yellow","blue"]
items=[]
selected="Initialized"
st=0
ed=0
steps=1

def settings():
    global x,y,st,ed,steps,items
    def sbmt():
        try:
            st=int(e1.get())
            ed=int(e2.get())
            steps=int(e3.get())
            for i in range(st,ed+1,steps):
                items.append(i)
        except ValueError as e:
            w_error=Tk()
            w_error.configure(background="LightSkyBlue")
            w_error.title("Error")
            w_error.geometry("1024x100")
            errorPrompt="""Error Occured! (Type:ValueError Code:VEiSNi @ 0x3642999H)
            Please Check Your Input and Try Again!"""
            l = Label(w_error, bg="LightSkyBlue", text=errorPrompt,font=('Consolas', 32))
            l.pack(side=TOP)
    w_set=Tk()
    w_set.configure(background="LightSkyBlue")
    w_set.title("Settings")
    Label(w_set, text="Start:",bg="LightSkyBlue",font=('Consolas', 32)).grid(row=0)
    Label(w_set, text="End:",bg="LightSkyBlue",font=('Consolas', 32)).grid(row=1)
    Label(w_set, text="Step:",bg="LightSkyBlue",font=('Consolas', 32)).grid(row=2)
    e1 = Entry(w_set,bg="LightSkyBlue")
    e2 = Entry(w_set,bg="LightSkyBlue")
    e3 = Entry(w_set,bg="LightSkyBlue")
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    Button(w_set, text='Submit Change!',font=('Consolas', 32), command=sbmt,bg="LightSkyBlue",fg="LightSkyBlue").grid(row=3, column=1)
    Label(w_set, text="",bg="LightSkyBlue",font=('Consolas', 10)).grid(row=4)
    Label(w_set, text="",bg="LightSkyBlue",font=('Consolas', 32)).grid(row=3, column=2)
    w_set.mainloop()

def about():
    global x,y
    w_ab=Tk()
    w_ab.configure(background="LightSkyBlue")
    w_ab.title("About")
    aboutMsg="""RandomIt! --by iwtywai
    Version 0.3.2 beta 1 (Dec2917)
    Published with GPL license
    Copyright c 2019-2020 iwtywai All rights reserved"""
    l = Label(w_ab, bg="LightSkyBlue", text=aboutMsg,font=('Consolas', 32))
    l.pack(side=TOP)
    w_ab.mainloop()

def helps():
    global x,y
    w_h=Tk()
    w_h.configure(background="LightSkyBlue")
    w_h.title("Tutorial")
    helpMsg="""RandomIt! --by iwtywai
    Version 0.3.2 beta 1 (Dec2917)

    Step 0: Start this software (Which you have already done.)
            Go to Funcs -> Tutorial and read this ([Done.])

    Step 1: Go to Funcs -> Settings and set the values.

            Make sure to fill all the boxes with DEC numbers.

    Step 2: Click on the Submit! button.

    Step 3: Go back to Main Window and start Randomizing!

    Enjoy!
    """
    l = Label(w_h, bg="LightSkyBlue", text=helpMsg,font=('Consolas', 32))
    l.pack(side=TOP)
    w_h.mainloop()

def select(key=""):
    global items,selected,l
    if len(items)==0:
        selected="None Left"
    else:
        selected=random.choice(items)
        items.remove(selected)
    l.config(text=selected)

menubar = Menu(root)
filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label="Settings",command=settings)
filemenu.add_command(label="Tutorial",command=helps)
filemenu.add_command(label="About",command=about)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=exit)
menubar.add_cascade(label="Funcs",menu=filemenu)
root.config(menu=menubar)
Button(root,text="RandomIt!",font=('Consolas', 24), command=select).pack(side=TOP,fill=X)
l = Label(root, bg="LightSkyBlue", width=x, height=y-400, text=selected,font=('Consolas', 128))
l.pack(side=BOTTOM,fill=Y,expand=YES)
l.bind("<Button-1>",select)
l.bind("<Return>",select)
l.bind("<F9>",select)

mainloop()
