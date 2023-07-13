from tkinter import *
from tkinter import ttk,messagebox
from PIL import ImageTk,Image
import time
player='x'
window=Tk()
window.title('XO Battle')
window.wm_attributes("-transparentcolor",'grey')
window.geometry('1000x600')
rimage=Image.open('p4.jpg').resize((1000,600))
test = ImageTk.PhotoImage(rimage)
ximage = Image.open('x2.png').resize((70, 70))
xtest = ImageTk.PhotoImage(ximage)
losei = Image.open('lose.png').resize((66, 40))
lose = ImageTk.PhotoImage(losei)
wini = Image.open('win.png').resize((66, 40))
win = ImageTk.PhotoImage(wini)
tiei = Image.open('tie.png').resize((66, 40))
tie = ImageTk.PhotoImage(tiei)
oimage = Image.open('o2.png').resize((70, 70))
otest = ImageTk.PhotoImage(oimage)
xonamei = Image.open('xo.png').resize((250,60))
xoname = ImageTk.PhotoImage(xonamei)
lab1=Label(window,image=test).place(x=0,y=0)
f1=Frame(window)
f1.pack(padx=10,pady=10)
window.resizable(False,False)
xo=Label(window,image=xoname,relief=FLAT)
xo.place(x=400,y=125)
xlabel = Label(lab1, text='Player x name    :', foreground="#FDEBF7", bg='#000000', font=("garamond", 15))
xlabel.place(x=350, y=250)
namex = StringVar()
namexentry = Entry(window, textvariable=namex)
namexentry.place(x=500, y=250)
olabel = Label(window, text='Player o name   :', foreground="#FDEBF7", bg='#000000', font=("garamond", 15))
olabel.place(x=350, y=300)
nameo = StringVar()
nameoentry = Entry(window, textvariable=nameo)
nameoentry.place(x=500, y=300)
numberlabel = Label(window, text='number of games:', foreground="#FDEBF7", bg='#000000', font=("garamond", 15))
numberlabel.place(x=350, y=350)
number = IntVar()
number_cb = ttk.Combobox(window, textvariable=number)
number_cb.place(x=500, y=350)
number_cb['values']=(1,3,5,7)
number.set(1)
gamenumber=1
scorex=0
scoreo=0
placey=200
def wincheck(board,window,labels,buttons):
    if board[0]==board[1]==board[2]=='x' or board[3]==board[4]==board[5]=='x' or board[6]==board[7]==board[8]=='x' or board[0]==board[3]==board[6]=='x' or board[1]==board[4]==board[7]=='x' or board[2]==board[5]==board[8]=='x' or board[2]==board[4]==board[6]=='x' or board[0]==board[4]==board[8]=='x':
        global gamenumber,scorex,placey,scoreo
        scorex+=1
        Label(window,image=win).place(x=200, y=placey)
        Label(window, image=lose).place(x=750, y=placey)
        placey+=50
        for i in labels:
            i.destroy()
        for j in buttons:
            j.destroy()
        if gamenumber<number.get():
            gamenumber+=1
            game()
        else:
            if scoreo>scorex:
                messagebox.showinfo("Game over",f"{nameo.get()} Wins")

                Label(window,text='Player '+nameo.get()+' Wins',width=62,height=18,foreground="#FDEBF7",bg='#000000',font=("garamond",15)).place(x=150, y=100)
            elif scoreo<scorex:
                messagebox.showinfo("Game over",f"{namex.get()} Wins")
                Label(window,text='Player '+namex.get()+' Wins',width=62,height=18,foreground="#FDEBF7",bg='#000000',font=("garamond",15)).place(x=150, y=100)
            else:
                messagebox.showinfo("Game over","game is Tie")
                Label(window,text='game is a tie',width=62,height=18,foreground="#FDEBF7",bg='#000000',font=("garamond",15)).place(x=150, y=100)
    elif board[0]==board[1]==board[2]=='o' or board[3]==board[4]==board[5]=='o' or board[6]==board[7]==board[8]=='o' or board[0]==board[3]==board[6]=='o' or board[1]==board[4]==board[7]=='o' or board[2]==board[5]==board[8]=='o' or board[2]==board[4]==board[6]=='o' or board[0]==board[4]==board[8]=='o':
        scoreo+=1
        Label(window,image=lose).place(x=200, y=placey)
        Label(window, image=win).place(x=750, y=placey)
        placey+=50
        for i in labels:
            i.destroy()
        for j in buttons:
            j.destroy()
        if gamenumber<number.get():
            gamenumber+=1
            game()
        else:
            if scoreo>scorex:
                messagebox.showinfo("Game over",f"{nameo.get()} Wins")

                Label(window,text='Player '+nameo.get()+' Wins',width=62,height=18,foreground="#FDEBF7",bg='#000000',font=("garamond",15)).place(x=150, y=100)
            elif scoreo<scorex:
                messagebox.showinfo("Game over",f"{namex.get()} Wins")
                Label(window,text='Player '+nameo.get()+' Wins',width=62,height=18,foreground="#FDEBF7",bg='#000000',font=("garamond",15)).place(x=150, y=100)
            else:
                messagebox.showinfo("Game over","game is Tie")
                Label(window,text='game is a tie',width=62,height=18,foreground="#FDEBF7",bg='#000000',font=("garamond",15)).place(x=150, y=100)
    elif '' not in board:
        Label(window,image=tie).place(x=200, y=placey)
        Label(window, image=tie).place(x=750, y=placey)
        placey+=50
        for i in labels:
            i.destroy()
        for j in buttons:
            j.destroy()
        if gamenumber<number.get():
            gamenumber+=1
            game()
        else:
            if scoreo>scorex:
                messagebox.showinfo("Game over",f"{nameo.get()} Wins")

                Label(window,text='Player '+nameo.get()+' Wins',width=62,height=18,foreground="#FDEBF7",bg='#000000',font=("garamond",15)).place(x=150, y=100)
            elif scoreo<scorex:
                messagebox.showinfo("Game over",f"{namex.get()} Wins")
                Label(window,text='Player '+nameo.get()+' Wins',width=62,height=18,foreground="#FDEBF7",bg='#000000',font=("garamond",15)).place(x=150, y=100)
            else:
                messagebox.showinfo("Game over","game is Tie")
                Label(window,text='game is a tie',width=62,height=18,foreground="#FDEBF7",bg='#000000',font=("garamond",15)).place(x=150, y=100)
def game():
    board=['','','','','','','','','']
    bw=(250//3)-5
    pl=250//3+10
    player='x'
    labels=[]
    buttons=[]
    def b(x1,y1,w,h,bu,i):
        global player,turnlabel
        if player=='x':
            l=Label(window,image=xtest,relief=FLAT)
            l.place(x=x1,y=y1,width=w,height=h)
            turnlabel=Label(window,text=f'player {nameo.get()} turn', foreground="#FDEBF7", bg='#000000', font=("garamond", 25))
            turnlabel.place(x=370,y=105)
            player='o'
            board[i]='x'
            labels.append(l)
            buttons.remove(bu)
            bu.destroy()
        else:
            l=Label(window,image=otest,relief=FLAT)
            l.place(x=x1,y=y1,width=w,height=h)
            turnlabel=Label(window,text=f'player {namex.get()} turn', foreground="#FDEBF7", bg='#000000', font=("garamond", 25))
            turnlabel.place(x=370,y=105)
            player='x'
            board[i]='o'
            labels.append(l)
            buttons.remove(bu)
            bu.destroy()
        wincheck(board,window,labels,buttons)
    def b1():b(350, 150, bw, bw, b1, 0)

    def b2():b(pl + 350, 150, bw, bw, b2, 1)

    def b3():b(2 * (pl) + 350, 150, bw, bw, b3, 2)

    def b4():b(350, pl + 150, bw, bw, b4, 3)

    def b5():b(pl + 350, pl + 150, bw, bw, b5, 4)

    def b6():b(2 * (pl) + 350, pl + 150, bw, bw, b6, 5)

    def b7():b(350, 2 * (pl) + 150, bw, bw, b7, 6)

    def b8():b(pl + 350, 2 * (pl) + 150, bw, bw, b8, 7)

    def b9():b(2 * (pl) + 350, 2 * (pl) + 150, bw, bw, b9, 8)

    b1 = Button(window, text=board[0], command=b1,bg="black")
    b1.place(x=350, y=150, width=bw, height=bw)
    buttons.append(b1)
    b2 = Button(window, text=board[1], command=b2,bg="black")
    b2.place(x=pl + 350, y=150, width=bw, height=bw)
    buttons.append(b2)
    b3 = Button(window, text=board[2], command=b3,bg="black")
    b3.place(x=2 * (pl) + 350, y=150, width=bw, height=bw)
    buttons.append(b3)
    b4 = Button(window, text=board[3], command=b4,bg="black")
    b4.place(x=350, y=pl + 150, width=bw, height=bw)
    buttons.append(b4)
    b5 = Button(window, text=board[4], command=b5,bg="black")
    b5.place(x=pl + 350, y=pl + 150, width=bw, height=bw)
    buttons.append(b5)
    b6 = Button(window, text=board[5], command=b6,bg="black")
    b6.place(x=2 * (pl) + 350, y=pl + 150, width=bw, height=bw)
    buttons.append(b6)
    b7 = Button(window, text=board[6], command=b7,bg="black")
    b7.place(x=350, y=2 * (pl) + 150, width=bw, height=bw)
    buttons.append(b7)
    b8 = Button(window, text=board[7], command=b8,bg="black")
    b8.place(x=pl + 350, y=2 * (pl) + 150, width=bw, height=bw)
    buttons.append(b8)
    b9 = Button(window, text=board[8], command=b9,bg="black")
    b9.place(x=2 * (pl) + 350, y=2 * (pl) + 150, width=bw, height=bw)
    buttons.append(b9)

def st():

    if namexentry.get().isalpha():
        if nameoentry.get().isalpha():
            if namexentry.get()!=nameoentry.get():
                xlabel.destroy()
                namexentry.destroy()
                olabel.destroy()
                nameoentry.destroy()
                number_cb.destroy()
                numberlabel.destroy()
                xo.destroy()
                start.destroy()
                turnlabel=Label(window,text=f'player {namex.get()} turn', foreground="#FDEBF7", bg='#000000', font=("garamond", 25))
                turnlabel.place(x=370,y=105)
                xl = Label(window, text=namex.get(), foreground="#FDEBF7", bg='#000000', font=("garamond", 25))
                xl.place(x=200, y=150)
                ol = Label(window, text=nameo.get(), foreground="#FDEBF7", bg='#000000', font=("garamond", 25))
                ol.place(x=750, y=150)

                game()
            else:
                messagebox.showwarning(" ","Players names cannot be same")
        else:
            messagebox.showwarning(" ","players name should only contain alphabets")
    else:
        messagebox.showwarning(" ","players name should only contain alphabets")

        
start=Button(window,text='Start',command=st,bg='#33B5E5',relief=FLAT,width=20,height=1)
start.place(x=420, y=400)
window.mainloop()
