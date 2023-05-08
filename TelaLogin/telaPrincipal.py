from tkinter import *
from tkinter import messagebox
import banco as banco
import tkinter as tk
from tkinter import ttk

def bt_Sair():
    login.destroy()
    
def retornar_login():
    # Retorna o necessario
    user.place(x=50, y=50)
    userF.place(x=100, y=50)
    password.place(x=50, y=75)
    passwordF.place(x=100, y=75)
    retornar.place(x=500)
    enter.place(x=50, y=150)

    # Remover o desnecessario
    nameF.place(x=500)
    name.place(x=500)
    estadoF.place(x=500)
    estado.place(x=500)
    register1.place(x=500)

def registrar_Cadastro():
    # Pegar informações para o Banco
    NameBanco = nameF.get()
    EmailBanco = userF.get()
    PasswordBanco = passwordF.get()
    EstadoBanco = estadoF.get()

    if(NameBanco == "" and EmailBanco == "" and PasswordBanco == "" and EstadoBanco == ""):
        messagebox.showerror(title="Erro de Registro", message="Preencha todos os Campos")
    else:
        # Inserir no Banco
        banco.cursor.execute("""
        INSERT INTO Users(Name, Email, Password, Estado) VALUES(?, ?, ?, ?)
        """,(NameBanco, EmailBanco, PasswordBanco, EstadoBanco))
        banco.conn.commit()
        messagebox.showinfo(title="Conta criada", message="Cadastrado(a) com sucesso!")

def acessando_Login():
    EmailLogin = userF.get()
    PasswordLogin = passwordF.get()

    banco.cursor.execute("""
    SELECT * FROM Users
    WHERE Email = ? AND Password = ?
    """,(EmailLogin, PasswordLogin))
    VerificarLogin = banco.cursor.fetchone()
    try:
        if(EmailLogin in VerificarLogin and PasswordLogin in VerificarLogin):
            messagebox.showinfo(title="Login", message="Seja Bem-vindo!")

            login.destroy()

#   ~~~~~~~~~~~~~~ TELA DE MENU ~~~~~~~~~~~~
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

            btn_cadastrar = ttk.Button(master=button_frame, text="Cadastrar", command=cadastrarUsers, style='Custom.TButton', compound='left', width=13) #image=img_tk2
            btn_cadastrar.pack(side=tk.LEFT, padx=10)

            btn_voltar = ttk.Button(master=button_frame, text="Voltar", command=voltar, style='Custom.TButton', compound='left', width=13) #image=img_tk3
            btn_voltar.pack(side=tk.LEFT, padx=10)

            btn_sair = ttk.Button(master=button_frame, width=10, text='SAIR', style='Custom.TButton', command=exit)
            btn_sair.pack(side=tk.LEFT, padx=10)

    except:
             messagebox.showerror(title="Conta não encontrada", message="Certifique-se que já está cadastrado! ")

             def cadastrar():
                 btn_cadastrar = btn_cadastrar

                 try:
                     root.destroy()

    mainloop()
    
# TELA DE LOGIN
login = Tk()
corDeFundo= 'orange'
login.title('LOGIN')
login["bg"] = corDeFundo
login.geometry("300x300+100+100")
login.resizable(width=False, height=False)
# login.iconbitmap(default="recursos/icone.ico")

# image = PhotoImage(file="recursos/imagelogin.png")
# img = Label(login, image=image, bg='#0d1e24')
# img.place(x=110, y=205)

title = Label(login, text='LOGIN', bg=corDeFundo, foreground='white')
title.pack(side=TOP, fill=X)

user = Label(login, text='Usuario:', bg=corDeFundo, foreground='white')
user.place(x=46, y=90)
userF = Entry(login)
userF.place(x=100, y=90)

password = Label(login, text='Senha:', bg=corDeFundo, foreground='white')
password.place(x=50, y=130)
passwordF = Entry(login, show="•")
passwordF.place(x=100, y=130)


enter = ttk.Button(login, width='10', text='ENTRAR', style='Custom.TButton', command=acessando_Login)
enter.place(x=115, y=180)


register1 = Button(login, width='15', text='CRIAR CADASTRO', command=registrar_Cadastro)
retornar = Button(login, width='15', text='VOLTAR', command=retornar_login)
estado = Label(login, text='Estado:', bg='orange', foreground='white')
name = Label(login, text='Nome:', bg='orange', foreground='white')
estadoF = Entry(login)
nameF = Entry(login)




login.mainloop()