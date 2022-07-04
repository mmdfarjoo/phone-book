from tkinter import *



datas=[]
def add ():
    global datas
    datas.append([name.get(),number.get(),address.get(1.0,'end-1c')])
    update_book()
def view ():
    name.set(datas[int(select.curselection()[0])][0])
    number.set(datas[int(select.curselection()[0])][1])
    address.delete(1.0,"end")
    address.insert(1.0, datas[int(select.curselection()[0])][2])
    
def delete():
    del datas[int(select.curselection()[0])]
    update_book()
def reset ():
    name.set('')
    number.set('')
    address.delete(1.0,'end')
    
def update_book ():
    select.delete(0,END)
    
    for n,p,a in datas:
        select.insert(END , n)


win=Tk(className='phone book GUI')




win.geometry('600x500')


win['background']='gray'


name=StringVar()
number= StringVar()

frame = Frame(win,background='green')
frame.pack(pady=10)

frame1 = Frame(win,background="green")
frame1.pack(pady=10)

frame2 = Frame(win)
frame2.pack(pady=10)

Label(frame, text= 'Name', font='arial 15 bold').pack(side=LEFT)
Entry(frame, textvariable= name ,width=54 ).pack()

Label(frame1,text= 'Phone', font= 'arial 15 bold').pack(side=LEFT)
Entry(frame1, textvariable= number , width=54).pack()

Label(frame2, text= 'Address', font= 'arial 15 bold').pack(side=LEFT)
address= Text(frame2,width=60,height=8)
address.pack()

Button(win,text='Add', font= 'arial 15 bold',width=20,command=add).place(x=50,y=270)
Button(win,text='View', font= 'arial 15 bold',width=20,command=view).place(x=50,y=310)
Button(win,text='delete', font= 'arial 15 bold',width=20,command=delete).place(x=50,y=350)
Button(win,text='Reset', font= 'arial 15 bold',width=20,command=reset).place(x=50,y=390)

Scroll_bar=Scrollbar(win,orient=VERTICAL)
select = Listbox(win,yscrollcommand=Scroll_bar.set,width=30,height=9)
Scroll_bar.config(command=select.yview)
Scroll_bar.pack(side=RIGHT , fill=Y)
select.place(x=300,y=273)


win.resizable(False,False)
win.mainloop()