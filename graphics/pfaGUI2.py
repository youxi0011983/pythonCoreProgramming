#!/usr/bin/python
# -*- coding:UTF-8 -*-

from functools import partial as pto
from tkinter import Tk, Button, X
from tkinter.messagebox import showinfo, showwarning, showerror

WARN = 'warn'
CRIT = 'crit'
REGU = 'regu'

SIGNS = {
    'do not enter': CRIT,
    'railroad crossing': WARN,
    '55\nspeed limit': CRIT,
    'wrong way': CRIT,
    'merging traffic': WARN,
    'one way': REGU
}

critCB = lambda: showerror('Error', 'Error Button Pressed!')
warnCB = lambda: showwarning('Warning', 'Warning Button Pressed!')
infcCb = lambda: showinfo('Info', 'Inof Button Pressed!')

top = Tk()
top.title('Road Signs')
Button(top, text='QUIT', command=top.quit, bg='red', fg='white').pack()
MyButton = pto(Button, top)

CritButton = pto(MyButton, command=critCB, bg='white', fg='red')
WarnButton = pto(MyButton, command=warnCB, bg='goldenrod', )
ReguButton = pto(MyButton, command=infcCb, bg='white', )

for eachSign in SIGNS:
    signType = SIGNS[eachSign]
    # print(signType)
    cmd = '%sButton(text=%r%s).pack(fill=X,expand=True)' % (
    signType.title(), eachSign, '.upper()' if signType == CRIT else '.title()')
    print(cmd)
    eval(cmd)

top.mainloop()
