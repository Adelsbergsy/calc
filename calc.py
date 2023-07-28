from tkinter import *
from tkinter import messagebox
import keyboard
from decimal import Decimal
import re


def button_typing(op):
    string.set(string.get() + op)
    print('fuck you')
    keyboard.press_and_release('End')


def clear():
    string.set('')


def result():
    try:
        if enter_field.get() == '':
            raise Exception
        res = eval(enter_field.get())
        if isinstance(res, float) and res.is_integer():
            res = int(res)
        string.set(str(res))
        print(res)
        keyboard.press_and_release('End')
    # except SyntaxError:
    #     text = 'Idiot! Look what you wrote!'
    #     error_message(text)
        # string.set('')
    # except NameError:
    #     text = 'Idiot! Look what you wrote!'
    #     error_message(text)
        # string.set('')
    except ArithmeticError:
        text = 'Idiot! Learn the math!'
        # error_message(text)
    # except Exception:
    #     text = 'Write something!'
    #     error_message(text)


def error_message(text):
    messagebox.showinfo('Sudden error', text)


root = Tk()
root.title('Calculator')
# root.geometry('300x300+1000+100')
icon = PhotoImage(file='calc.png')
root.iconphoto(False, icon)
root['bg'] = '#fff'
root.resizable(False, False)
btns = []
num = 0
ops = ('7', '8', '9', '/', '4', '5', '6', '*',
       '1', '2', '3', '-', '0', '.', '=', '+')
string = StringVar()
enter_field = Entry(font='Arial 10',  width=28,
                    relief=FLAT, textvariable=string)

for op in ops:
    btns.append(Button(font='Arial 10 bold',
                       cursor='hand2',
                       activeforeground='#f00',
                       activebackground='#dbdbdb',
                       text=op,
                       height=4,
                       width=8,
                       command=lambda op=op: button_typing(op)
                       )
                )
btns.append(Button(text='C',
                   cursor='hand2',
                   activeforeground='#f00',
                   activebackground='#dbdbdb',
                   command=clear,
                   height=4,
                   width=8)
            )

enter_field.grid(row=0, column=0, columnspan=3)
enter_field.focus()
for i in range(4):
    for j in range(4):
        btns[num].grid(row=i+1, column=j, sticky=N+S+W+E)
        num += 1
btns[-1].grid(row=0, column=3, sticky=N+S+W+E)
btns[-3].config(command=result)
keyboard.add_hotkey('enter', result)

root.mainloop()
