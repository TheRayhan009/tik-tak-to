from tkinter import *
import tkinter
panel=tkinter.Tk()


def press1(event):
    global x
    global turn1
    if clicked1.get():
        if x%2==0:
            turn1.set("X")
        else:
            turn1.set("O")
        x=x+1
        win()
        clicked1.set(False)
    

def press2(event):
    global x
    global turn2
    if clicked2.get():
        if x%2==0:
            turn2.set("X")
        else:
            turn2.set("O")
        x=x+1
        win()
        clicked2.set(False)
    
def press3(event):
    global x
    global turn3
    if clicked3.get():
        if x%2==0:
            turn3.set("X")
        else:
            turn3.set("O")
        x=x+1
        win()
        clicked3.set(False)
    
    
def press4(event):
    global x
    global turn4
    if clicked4.get():
        if x%2==0:
            turn4.set("X")
        else:
            turn4.set("O")
        x=x+1
        win()
        clicked4.set(False)
    
    
def press5(event):
    global x
    global turn5
    if clicked5.get():
        if x%2==0:
            turn5.set("X")
        else:
            turn5.set("O")
        x=x+1
        win()
        clicked5.set(False)
    
    
def press6(event):
    global x
    global turn6
    if clicked6.get():
        if x%2==0:
            turn6.set("X")
        else:
            turn6.set("O")
        x=x+1
        win()
        clicked6.set(False)
    
    
def press7(event):
    global x
    global turn7
    if clicked7.get():
        if x%2==0:
            turn7.set("X")
        else:
            turn7.set("O")
        x=x+1
        win()
        clicked7.set(False)
    
    
def press8(event):
    global x
    global turn8
    if clicked8.get():
        if x%2==0:
            turn8.set("X")
        else:
            turn8.set("O")
        x=x+1
        win()
        clicked8.set(False)
    
    
def press9(event):
    global x
    global turn9
    if clicked9.get():
        if x%2==0:
            turn9.set("X")
        else:
            turn9.set("O")
        x=x+1
        win()
        clicked9.set(False)
    

def win():
    global tf
    
    
    if (turn1.get() == turn2.get() == turn3.get() == "X" or
        turn4.get() == turn5.get() == turn6.get() == "X" or
        turn7.get() == turn8.get() == turn9.get() == "X" or
        turn1.get() == turn4.get() == turn7.get() == "X" or
        turn2.get() == turn5.get() == turn8.get() == "X" or
        turn3.get() == turn6.get() == turn9.get() == "X" or
        turn1.get() == turn5.get() == turn9.get() == "X" or
        turn3.get() == turn5.get() == turn7.get() == "X"):
        win_info.set("X wins!")
        win_box.update()
        tf=False
        
    elif (turn1.get() == turn2.get() == turn3.get() == "O" or
          turn4.get() == turn5.get() == turn6.get() == "O" or
          turn7.get() == turn8.get() == turn9.get() == "O" or
          turn1.get() == turn4.get() == turn7.get() == "O" or
          turn2.get() == turn5.get() == turn8.get() == "O" or
          turn3.get() == turn6.get() == turn9.get() == "O" or
          turn1.get() == turn5.get() == turn9.get() == "O" or
          turn3.get() == turn5.get() == turn7.get() == "O"):
        win_info.set("O wins!")
        win_box.update()
        tf=False
    if tf==True and m.get()>=8:
        win_info.set("DRAW!!")
        win_box.update()
    m.set(m.get()+1)
        
tf = True
x=0
m=IntVar()
m.set(0)
turn1=StringVar()
turn1.set("")
turn2=StringVar()
turn2.set("")
turn3=StringVar()
turn3.set("")
turn4=StringVar()
turn4.set("")
turn5=StringVar()
turn5.set("")
turn6=StringVar()
turn6.set("")
turn7=StringVar()
turn7.set("")
turn8=StringVar()
turn8.set("")
turn9=StringVar()
turn9.set("")

win_info=StringVar()
win_info.set("")

clicked1 = BooleanVar()
clicked1.set(True)
clicked2 = BooleanVar()
clicked2.set(True)
clicked3 = BooleanVar()
clicked3.set(True)
clicked4 = BooleanVar()
clicked4.set(True)
clicked5 = BooleanVar()
clicked5.set(True)
clicked6 = BooleanVar()
clicked6.set(True)
clicked7 = BooleanVar()
clicked7.set(True)
clicked8 = BooleanVar()
clicked8.set(True)
clicked9 = BooleanVar()
clicked9.set(True)



play_box1=Button(panel,width=17,height=7,background="gray",border="2",textvariable=turn1,command=press1)
play_box1.grid(row=1,column=1)
play_box1.bind("<Button-1>",press1)
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
play_box2=Button(panel,width=17,height=7,background="gray",border="2",textvariable=turn2,command=press2)
play_box2.grid(row=1,column=2)
play_box2.bind("<Button-1>",press2)
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
play_box3=Button(panel,width=17,height=7,background="gray",border="2",textvariable=turn3,command=press3)
play_box3.grid(row=1,column=3)
play_box3.bind("<Button-1>",press3)
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
play_box4=Button(panel,width=17,height=7,background="gray",border="2",textvariable=turn4,command=press4)
play_box4.grid(row=2,column=1)
play_box4.bind("<Button-1>",press4)
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
play_box5=Button(panel,width=17,height=7,background="gray",border="2",textvariable=turn5,command=press5)
play_box5.grid(row=2,column=2)
play_box5.bind("<Button-1>",press5)
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
play_box6=Button(panel,width=17,height=7,background="gray",border="2",textvariable=turn6,command=press6)
play_box6.grid(row=2,column=3)
play_box6.bind("<Button-1>",press6)
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
play_box7=Button(panel,width=17,height=7,background="gray",border="2",textvariable=turn7,command=press7)
play_box7.grid(row=3,column=1)
play_box7.bind("<Button-1>",press7)
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
play_box8=Button(panel,width=17,height=7,background="gray",border="2",textvariable=turn8,command=press8)
play_box8.grid(row=3,column=2)
play_box8.bind("<Button-1>",press8)
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
play_box9=Button(panel,width=17,height=7,background="gray",border="2",textvariable=turn9,command=press9)
play_box9.grid(row=3,column=3)
play_box9.bind("<Button-1>",press9)
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/


win_box=Entry(panel,textvar=win_info,width=23,font=("lucida",23),background="gray")
win_box.grid(row=5,column=1,columnspan=14,sticky="n")

panel.title("TOK TAK TO")
panel.geometry("388x387+750+60")
panel.mainloop()