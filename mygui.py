#!/usr/bin/python
# -*- coding:UTF-8 -*-

from functools import partial
import tkinter

if __name__ == '__main__':
    root = tkinter.Tk()
    MyButton = partial(tkinter.Button, root, fg='white', bg='blue')
    b1 = MyButton(text='Button 1')
    b2 = MyButton(text='Button 1')
    qb = MyButton(text='QUIT', bg='red', command=root.quit)
    b1.pack()
    b2.pack()
    qb.pack(fill=tkinter.X, expand=True)
    root.title('PFAs!')
    root.mainloop()
