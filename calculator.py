from tkinter import *
import tkinter.font as font
root = Tk()

p1 = PhotoImage(file = 'image logo\callogonew.png')
root.iconphoto(False, p1)
root.resizable(0,0)

root.configure(background='#0072A0')
#title

root.title("Simple Calculator")

#functions are defined here:

def changeOnHover(button, colorOnHover, colorOnLeave):
  
    # adjusting backgroung of the widget
    # background on entering widget
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover))
  
    # background color on leving widget
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave))


def button_click(n):
    e.insert(END,n)
    
    
def button_add():
    first_num=e.get()
    global f_num
    global math
    math="add"
    f_num=float(first_num)
    e.delete(0,END)

def button_sub():
    first_num=e.get()
    global f_num
    global math
    math="sub"
    f_num=float(first_num)
    e.delete(0,END)

def button_mul():
    first_num=e.get()
    global f_num
    global math
    math="mul"
    f_num=float(first_num)
    e.delete(0,END)

def button_div():
    first_num=e.get()
    global f_num
    global math
    math="div"
    f_num=float(first_num)
    e.delete(0,END)

def button_clear():
    e.delete(0,END)

def button_equal():
    second_num=e.get()
    second_num=int(second_num)
    e.delete(0,END)
    if(math=="add"):
        e.insert(0,f_num+int(second_num))
    elif(math=="sub"):
        e.insert(0,f_num-int(second_num))
    elif(math=="mul"):
        e.insert(0,f_num*int(second_num))
    elif(math=="div"):
        e.insert(0,f_num/int(second_num))
    

#label for input and output

e = Entry(root,width=40, borderwidth=5)
e.grid(row=0,column=0,padx=10,pady=10,columnspan=4)

# define button
buttonFont = font.Font(size=13, weight='bold')


but1 = Button(root,text="1",bg='#CDF0FF',padx=41,pady=20,font=buttonFont,command=lambda:button_click(1))
but2 = Button(root,text="2",bg='#CDF0FF',padx=46,pady=20,font=buttonFont,command=lambda:button_click(2))
but3 = Button(root,text="3",bg='#CDF0FF',padx=42,pady=20,font=buttonFont,command=lambda:button_click(3))
but4 = Button(root,text="4",bg='#CDF0FF',padx=41,pady=20,font=buttonFont,command=lambda:button_click(4))
but5 = Button(root,text="5",bg='#CDF0FF',padx=46,pady=20,font=buttonFont,command=lambda:button_click(5))
but6 = Button(root,text="6",bg='#CDF0FF',padx=42,pady=20,font=buttonFont,command=lambda:button_click(6))
but7 = Button(root,text="7",bg='#CDF0FF',padx=41,pady=20,font=buttonFont,command=lambda:button_click(7))
but8 = Button(root,text="8",bg='#CDF0FF',padx=46,pady=20,font=buttonFont,command=lambda:button_click(8))
but9 = Button(root,text="9",bg='#CDF0FF',padx=42,pady=20,font=buttonFont,command=lambda:button_click(9))
but0 = Button(root,text="0",bg='#CDF0FF',padx=41,pady=20,font=buttonFont,command=lambda:button_click(0))


but_add = Button(root,text="+",bg='#91E0FF',padx=41,pady=20,font=buttonFont,command=button_add)
but_sub = Button(root,text="-",bg='#91E0FF',padx=42,pady=20,font=buttonFont,command=button_sub)
but_mul = Button(root,text="*",bg='#91E0FF',padx=47,pady=20,font=buttonFont,command=button_mul)
but_div = Button(root,text="/",bg='#91E0FF',padx=45,pady=20,font=buttonFont,command=button_div)
but_equal = Button(root,text="=",bg='#55ceff',padx=99,pady=20,font=buttonFont,command=button_equal)
but_clear = Button(root,text="Clear",bg='#55ceff',padx=84,pady=20,font=buttonFont,command=button_clear)

# griding buttons on screen

but1.grid(row=3,column=0)
but2.grid(row=3,column=1)
but3.grid(row=3,column=3)

but4.grid(row=2,column=0)
but5.grid(row=2,column=1)
but6.grid(row=2,column=3)

but7.grid(row=1,column=0)
but8.grid(row=1,column=1)
but9.grid(row=1,column=3)

but0.grid(row=4,column=0)

but_add.grid(row=5,column=0)
but_equal.grid(row=5,column=1,columnspan=3)
but_clear.grid(row=4,column=1,columnspan=3)

but_sub.grid(row=6,column=0)
but_mul.grid(row=6,column=1)
but_div.grid(row=6,column=2,columnspan=2)

#hover

changeOnHover(but0, "#004764", "#CDF0FF")
changeOnHover(but1, "#004764", "#CDF0FF")
changeOnHover(but2, "#004764", "#CDF0FF")
changeOnHover(but3, "#004764", "#CDF0FF")
changeOnHover(but4, "#004764", "#CDF0FF")
changeOnHover(but5, "#004764", "#CDF0FF")
changeOnHover(but6, "#004764", "#CDF0FF")
changeOnHover(but7, "#004764", "#CDF0FF")
changeOnHover(but8, "#004764", "#CDF0FF")
changeOnHover(but9, "#004764", "#CDF0FF")

changeOnHover(but_add, "#004764", "#91E0FF")
changeOnHover(but_sub, "#004764", "#91E0FF")
changeOnHover(but_mul, "#004764", "#91E0FF")
changeOnHover(but_div, "#004764", "#91E0FF")

changeOnHover(but_clear, "#004764", "#55ceff")
changeOnHover(but_equal, "#004764", "#55ceff")
root.mainloop()

