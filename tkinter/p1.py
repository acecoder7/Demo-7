import tkinter as tk
from tkinter import *
root=Tk(className='MyFirstTkinterProgram')
root.geometry('450x550')
root.title('FIRST PROGRAM')
l=Label(root, text='DANKE').grid(row=0,column=0)
def wel():
    lab='welcome to our page'+e1.get()
    l.configure(text=lab)
l1=Label(root, text='ENTER NAME:').grid(row=1,column=0)
e1=Entry(root, bg='white', fg='red', font='times 100', show='*').grid(row=1,column=1)
but=Button(root, text='submit', width=10, height=2, command=wel).grid(row=7, column=1)
root.mainloop()

