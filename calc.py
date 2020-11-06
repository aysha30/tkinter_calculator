from tkinter import *
import parser
root = Tk()
root.title('Calculator')

#get user input an place it on screen
i=0
def get_var(num):
    global i
    display.insert(i,num)
    i+=1

def clear_all():
    display.delete(0,END)

def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0,new_string)

def get_op(op):
    global i
    lg = len(op)
    display.insert(i,op)
    i+=lg

def equal():
    entire_string=display.get()
    try:
        a= parser.expr(entire_string).compile()
        res= eval(a)
        clear_all()
        display.insert(0,res)
    except exception:
        clear_all()
        display.insert(0,"ERROR")

def fac():
    res=1
    num= display.get()
    while num:
        res*=num
        num-=1
    res=eval(res)
    clear_all()
    display.insert(0,res)

#input field
display = Entry(root)
display.grid(row=1, columnspan=6, sticky=W+E)

#buttons
Button(root, text=' 1 ', command=lambda : get_var(1)).grid(row=2, column=0)
Button(root, text=' 2 ', command=lambda : get_var(2)).grid(row=2, column=1)
Button(root, text=' 3 ', command=lambda : get_var(3)).grid(row=2, column=2)

Button(root, text=' 4 ', command=lambda : get_var(4)).grid(row=3, column=0)
Button(root, text=' 5 ', command=lambda : get_var(5)).grid(row=3, column=1)
Button(root, text=' 6 ', command=lambda : get_var(6)).grid(row=3, column=2)

Button(root, text=' 7 ', command=lambda : get_var(7)).grid(row=4, column=0)
Button(root, text=' 8 ', command=lambda : get_var(8)).grid(row=4, column=1)
Button(root, text=' 9 ', command=lambda : get_var(9)).grid(row=4, column=2)

Button(root, text=' AC ', command=lambda : clear_all()).grid(row=5, column=0)
Button(root, text=' 0 ', command=lambda : get_var(0)).grid(row=5, column=1)
Button(root, text=' = ', command=lambda : equal()).grid(row=5, column=2)

Button(root, text=' + ', command=lambda : get_op('+')).grid(row=2, column=3)
Button(root, text=' - ', command=lambda : get_op('-')).grid(row=3, column=3)
Button(root, text=' * ', command=lambda : get_op('*')).grid(row=4, column=3)
Button(root, text=' / ', command=lambda : get_op('/')).grid(row=5, column=3)

Button(root, text=' pi ', command=lambda : get_op('*3.14')).grid(row=2, column=4)
Button(root, text=' % ', command=lambda : get_op('%')).grid(row=3, column=4)
Button(root, text=' ( ', command=lambda : get_op('(')).grid(row=4, column=4)
Button(root, text=' exp ', command=lambda : get_op('**')).grid(row=5, column=4)

Button(root, text=' <- ', command=lambda : undo()).grid(row=2, column=5)
Button(root, text=' x! ', command=lambda : fac()).grid(row=3, column=5)
Button(root, text=' ) ', command=lambda : get_op(')')).grid(row=4, column=5)
Button(root, text=' ^2 ', command=lambda : get_op('**2')).grid(row=5, column=5)



root.mainloop()