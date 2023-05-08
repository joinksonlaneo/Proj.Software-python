from tkinter import *
from tkinter import messagebox
import banco as banco
import tkinter as tk
from tkinter import ttk 

# TELA DE MENU

root = tk.Tk()
            root.geometry("775x400")
            root.minsize(775, 400)
            root.maxsize(775, 400)
            root.title("Menu")
            root.configure(background='orange')

            # Funções dos botões
            def voltar():
                print("Botão 'Voltar' foi clicado.")

            def fazer_pedido():
                print("Botão 'Fazer Pedido' foi clicado.")

            def cadastrarUsers():
                print("Botão 'Cadastrar' foi clicado.")

            def sair():
                print("Botão 'sair' foi clicado.")
                
            # Configurar os widgets

            # Criar um frame para os botões
            button_frame = tk.Frame(root)
            button_frame.pack(side=tk.BOTTOM, pady=20)
            button_frame.configure(background='orange')


            bold_font = ("Helvetica", 12, "bold")

            # Adicionando a imagem ao botão "Fazer Pedido"
            style = ttk.Style()
            style.configure('Custom.TButton', font=bold_font, background='white', foreground='black')


            btn_fazer_pedido = ttk.Button(master=button_frame, text="Fazer Pedido", command=fazer_pedido, style='Custom.TButton', compound='left', width=13) #image=img_tk1
            btn_fazer_pedido.pack(side=tk.LEFT, padx=10)

            # btn_cadastrar = ttk.Button(master=button_frame, text="Cadastrar", command=criar_Cadastro, style='Custom.TButton', compound='left', width=13) #image=img_tk2
            # btn_cadastrar.pack(side=tk.LEFT, padx=10)

            btn_voltar = ttk.Button(master=button_frame, text="Voltar", command=voltar, style='Custom.TButton', compound='left', width=13) #image=img_tk3
            btn_voltar.pack(side=tk.LEFT, padx=10)

            btn_sair = ttk.Button(master=button_frame, width=10, text='SAIR', style='Custom.TButton', command=exit)
            btn_sair.pack(side=tk.LEFT, padx=10)

        