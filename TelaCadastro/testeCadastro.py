from tkinter import *
from tkinter import messagebox
import tkinter as tk
import tkinter as ttk

# TELA DE LOGIN
cad = Tk()
corDeFundo= '#0b2e3b'
cad.title('LOGIN')
cad["bg"] = corDeFundo
cad.geometry("300x300+100+100")
cad.resizable(width=False, height=False)

title = Label(cad, text='Cadastro', bg=corDeFundo, foreground='white', font=20)
title.pack(side=TOP, fill=X)


nomer = Label(cad, text='Nome:', bg=corDeFundo, foreground='white', font=15)
nomer.place(x=46, y=50)
nomeF = Entry(cad)
nomeF.place(x=100, y=50)


user = Label(cad, text='Usuario:', bg=corDeFundo, foreground='white', font=15)
user.place(x=36, y=90)
userF = Entry(cad, show="•")
userF.place(x=100, y=90)

password = Label(cad, text='Senha:', bg=corDeFundo, foreground='white', font=15)
password.place(x=44, y=130)
passwordF = Entry(cad, show="•")
passwordF.place(x=100, y=130)


enter = Button(cad, width='11', text='Criar cadastro')
enter.place(x=115, y=180)
enter = Button(cad, width='11', text='Volta')
enter.place(x=115, y=220)

cad.mainloop()