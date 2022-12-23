from tkinter import *
import tkinter.messagebox as tmsg
import os
import time
from math import *
def getvals(event):
    value = event.widget.cget('text')
    if value=='Clr':
        sc_variable.set('')
    elif value=='=':
        try:
            sc_variable.set(eval(screen.get()))
            screen.update()
        except Exception as e:
            sc_variable.set('Error')
            screen.update()
            status_var.set('Preparing...')
            screen.update()
            time.sleep(2)
            sc_variable.set('')
            screen.update()
            status_var.set('Ready..')
            screen.update()
    else:
        sc_variable.set(f'{sc_variable.get()}{value}')
def Scientific():
    root.geometry("865x523+0+0")
def Standard():
    root.geometry("515x523+0+0")
def info():
    tmsg.showinfo("Information",'This calculator can perform basic operations, trignometric operations , exponential operations and logarithmic operations only')
def feedback():
    ans=tmsg.askquestion("We'd love to hear your feedback","Was your experience good ? ")
    if ans=='yes':
        tmsg.showinfo('Feedback','Thank you for your feedback')
    else:
        tmsg.showinfo('Feedback','We appologise and will improve our service quality, Thank you')
def help():
    tmsg.showinfo("Errors", ' Errors can occur due to improper syntax. Please check whether you have put parentheses at the places required')  
    
    
root = Tk()
root.title("Scientific calculator")

root.geometry("515x523+0+0")
my_menu=Menu(root)
m0=Menu(my_menu,fg='black')
m0.add_command(label='Standard',command=Standard)
m0.add_separator()
m0.add_command(label='Scientific',command=Scientific)
m1=Menu(my_menu,tearoff=0,fg='black')
m1.add_command(label='Information',command=info)
m1.add_command(label='Feedback',command=feedback)
root.config(menu=my_menu)
my_menu.add_cascade(label=' File ',menu=m0)
my_menu.add_cascade(label=' About ',menu=m1)
my_menu.add_command(label='Help',command=help)
my_menu.add_command(label='Exit',command=quit)
sc_variable=StringVar()
screen=Entry(root,textvariable=sc_variable,font='lucida 35 bold',fg='black',bg='silver',borderwidth=10,width=32)
screen.pack(pady=5)
f=Frame(root)
f.pack()
b1=Button(f,text='Clr',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='lightskyblue',width=3)
b2=Button(f,text='%',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='lightskyblue',width=3)
b3=Button(f,text='(',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='lightskyblue',width=3)
b4=Button(f,text=')',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='lightskyblue',width=3)
b5=Button(f,text='sin',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='lightskyblue',width=3)
b6=Button(f,text='sinh',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='lightskyblue',width=3)
b7=Button(f,text='asin',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='lightskyblue',width=3)
b8=Button(f,text='e',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='lightskyblue',width=3)
b9=Button(f,text='comb',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='lightskyblue',width=3)
b10=Button(f,text='fmod',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='lightskyblue',width=3)
b1.bind('<Button-1>',getvals)
b2.bind('<Button-1>',getvals)
b3.bind('<Button-1>',getvals)
b4.bind('<Button-1>',getvals)
b5.bind('<Button-1>',getvals)
b6.bind('<Button-1>',getvals)
b7.bind('<Button-1>',getvals)
b8.bind('<Button-1>',getvals)
b9.bind('<Button-1>',getvals)
b10.bind('<Button-1>',getvals)
buttons=[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10]
count=0
for i in range(10):
        buttons[count].grid(row=1,column=i)
        count += 1
f=Frame(root)
f.pack()
b1=Button(f,text='+',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='lightskyblue',width=3)
b2=Button(f,text='7',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='white',width=3)
b3=Button(f,text='8',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='white',width=3)
b4=Button(f,text='9',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='white',width=3)
b5=Button(f,text='cos',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='lightskyblue',width=3)
b6=Button(f,text='cosh',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='lightskyblue',width=3)
b7=Button(f,text='acos',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='lightskyblue',width=3)
b8=Button(f,text='lcm',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='lightskyblue',width=3)
b9=Button(f,text='frexp',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='lightskyblue',width=3)
b10=Button(f,text='ldexp',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='lightskyblue',width=3)
b1.bind('<Button-1>',getvals)
b2.bind('<Button-1>',getvals)
b3.bind('<Button-1>',getvals)
b4.bind('<Button-1>',getvals)
b5.bind('<Button-1>',getvals)
b6.bind('<Button-1>',getvals)
b7.bind('<Button-1>',getvals)
b8.bind('<Button-1>',getvals)
b9.bind('<Button-1>',getvals)
b10.bind('<Button-1>',getvals)
buttons=[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10]
count=0
for i in range(10):
    buttons[count].grid(row=2,column=i)
    count += 1
f=Frame(root)
f.pack()
b1=Button(f,text='-',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='lightskyblue',width=3)
b2=Button(f,text='4',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='white',width=3)
b3=Button(f,text='5',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='white',width=3)
b4=Button(f,text='6',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='white',width=3)
b5=Button(f,text='tan',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='lightskyblue',width=3)
b6=Button(f,text='tanh',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='lightskyblue',width=3)
b7=Button(f,text='atan',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='lightskyblue',width=3)
b8=Button(f,text='gcd',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='lightskyblue',width=3)
b9=Button(f,text='floor',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='lightskyblue',width=3)
b10=Button(f,text='fabs',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='lightskyblue',width=3)
b1.bind('<Button-1>',getvals)
b2.bind('<Button-1>',getvals)
b3.bind('<Button-1>',getvals)
b4.bind('<Button-1>',getvals)
b5.bind('<Button-1>',getvals)
b6.bind('<Button-1>',getvals)
b7.bind('<Button-1>',getvals)
b8.bind('<Button-1>',getvals)
b9.bind('<Button-1>',getvals)
b10.bind('<Button-1>',getvals)
buttons=[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10]
count=0
for i in range(10):
    buttons[count].grid(row=3,column=i)
    count += 1
f=Frame(root)
f.pack()
b1=Button(f,text='*',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='lightskyblue',width=3)
b2=Button(f,text='1',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='white',width=3)
b3=Button(f,text='2',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='white',width=3)
b4=Button(f,text='3',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='white',width=3)
b5=Button(f,text='pi',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='lightskyblue',width=3)
b6=Button(f,text='log',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='lightskyblue',width=3)
b7=Button(f,text='sqrt',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='lightskyblue',width=3)
b8=Button(f,text='factorial',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='lightskyblue',width=3)
b9=Button(f,text='radians',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='lightskyblue',width=3)
b10=Button(f,text='exp',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='lightskyblue',width=3)
b1.bind('<Button-1>',getvals)
b2.bind('<Button-1>',getvals)
b3.bind('<Button-1>',getvals)
b4.bind('<Button-1>',getvals)
b5.bind('<Button-1>',getvals)
b6.bind('<Button-1>',getvals)
b7.bind('<Button-1>',getvals)
b8.bind('<Button-1>',getvals)
b9.bind('<Button-1>',getvals)
b10.bind('<Button-1>',getvals)
buttons=[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10]
count=0
for i in range(10):
    buttons[count].grid(row=4,column=i)
    count += 1
f=Frame(root)
f.pack()
b1=Button(f,text='/',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='lightskyblue',width=3)
b2=Button(f,text='.',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='lightskyblue',width=3)
b3=Button(f,text='0',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='white',width=3)
b4=Button(f,text=',',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='lightskyblue',width=3)
b5=Button(f,text='log10',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='lightskyblue',width=3)
b6=Button(f,text='=',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='lightskyblue',width=3)
b7=Button(f,text='ceil',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='lightskyblue',width=3)
b8=Button(f,text='pow',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='lightskyblue',width=3)
b9=Button(f,text='degrees',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='lightskyblue',width=3)
b10=Button(f,text='dis',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='lightskyblue',width=3)
b1.bind('<Button-1>',getvals)
b2.bind('<Button-1>',getvals)
b3.bind('<Button-1>',getvals)
b4.bind('<Button-1>',getvals)
b5.bind('<Button-1>',getvals)
b6.bind('<Button-1>',getvals)
b7.bind('<Button-1>',getvals)
b8.bind('<Button-1>',getvals)
b9.bind('<Button-1>',getvals)
b10.bind('<Button-1>',getvals)
buttons=[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10]
count=0
for i in range(10):
    buttons[count].grid(row=5,column=i)
    count += 1
status_var=StringVar()
status_var.set('Ready..')
Label(root,textvariable=status_var,relief=SUNKEN,anchor='w',borderwidth=3,bg='silver',fg='black').pack(side=BOTTOM,fill=X)
root.mainloop()
