from tkinter import *
import functools

@functools.singledispatch
def transform(arg):
    type_name = type(arg).__name__
    assert False, "Unsupported notation : " + type_name

@transform.register(int)
def _(arg):
    if arg == 0:
        return 'Ноль'
    if arg == 1:
        return 'Один'
    if arg == 2:
        return 'Два'
    if arg == 3:
        return 'Три'
    if arg == 4:
        return 'Четыре'
    if arg == 5:
        return 'Пять'
    if arg == 6:
        return 'Шесть'
    if arg == 7:
        return 'Семь'
    if arg == 8:
        return 'Восемь'
    if arg == 9:
        return 'Девять'


@transform.register(str)
def _(arg):
    return arg[2::]

def button_clicked():
    try:
        dt = digType.get()
        d = int(dig.get())
        if dt == 'int':
            res = transform(d)
        if dt == 'bin':
            res = transform(bin(d))
        if dt == 'oct':
            res = transform(oct(d))
        if dt == 'hex':
            res = transform(hex(d))
        result = Label(root, bg="blue", text=res, width = '200', fg='white')
        result.pack()
    except ValueError as e:
        result = Label(root, bg="blue", text="Введите цифровое значение", width = '200', fg='white')
        result.pack()    


root = Tk()
dig = Entry(root)
dig.pack()
digType = StringVar()
rbutton1=Radiobutton(root,text='int',variable=digType,value='int')
rbutton2=Radiobutton(root,text='bin',variable=digType,value='bin')
rbutton3=Radiobutton(root,text='oct',variable=digType,value='oct')
rbutton4=Radiobutton(root,text='hex',variable=digType,value='hex')
rbutton1.pack()
rbutton2.pack()
rbutton3.pack()
rbutton4.pack()
button = Button(root, bg="red", fg='green', text="Преобразовать", command=button_clicked)
button.pack()
root.geometry('500x400+300+200')
root.mainloop()
