from tkinter import *
from tkinter import messagebox
import banco as banco
import tkinter as tk
from tkinter import ttk
from view import *

################ cores ###############
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # sky blue

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
            app = tk.Tk()
            app.geometry("500x300")
            app.title("Menu")
            app.configure(background='#0b2e3b')

            # Criação dos comandos das opções do menu
            def fazer_pedido():
                                
                janela = Tk()
                janela.title("")
                janela.geometry("1043x453")
                janela.configure(background="#e9edf5")
                janela.resizable(width=FALSE, height=FALSE)

                ############## dividindo a janela ############
                frame_cima = Frame(janela, width=310, height=50, bg=co2, relief='flat')
                frame_cima.grid(row=0, column=0)

                frame_baixo = Frame(janela, width=310, height=403, bg=co1, relief='flat')
                frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

                frame_direita = Frame(janela, width=588, height=403, bg=co1, relief='flat')
                frame_direita.grid(row=0, column=1, rowspan=2, sticky=NSEW, padx=1, pady=0)

                ############### label cima ##################
                app_nome = Label(frame_cima, text="Faça seu pedido:", anchor=NW, font=('Ivy 13 bold'), bg=co2, fg=co1, relief='flat')
                app_nome.place(x=10, y=20)

                # variavel tree global
                global tree

                # função inserir
                def inserir():
                        nome = e_nome.get()
                        endereco = e_endereco.get()
                        pedido = e_pedido.get()
                        pg = e_pg.get()
                        preco = e_preco.get()
                        descricao = e_descricao.get()

                        lista = [nome, endereco, pedido, pg, preco, descricao]

                        if nome == '':
                                messagebox.showerror('Nome não pode ficar vazio!')
                        else:
                                atualizar_info(lista)
                                messagebox.showinfo('Os dados foram inseridos com sucesso!')

                                e_nome.delete(0, 'end')
                                e_endereco.delete(0, 'end')
                                e_pedido.delete(0, 'end')
                                e_pg.delete(0, 'end')
                                e_preco.delete(0, 'end')
                                e_descricao.delete(0, 'end')

                # função atualizar
                def atualizar():
                        try:
                                treev_dados = tree.focus()
                                treev_dicionario = tree.item(treev_dados)
                                tree_lista = treev_dicionario['values']

                                valor_id = [tree_lista[0]]

                                e_nome.delete(0, 'end')
                                e_endereco.delete(0, 'end')
                                e_pedido.delete(0, 'end')
                                e_pg.delete(0, 'end')
                                e_preco.delete(0, 'end')
                                e_descricao.delete(0, 'end')

                                e_nome.insert(0, tree_lista[1])
                                e_endereco.insert(0, tree_lista[2])
                                e_pedido.insert(0, tree_lista[3])
                                e_pg.insert(0, tree_lista[4])
                                e_preco.insert(0, tree_lista[5])
                                e_descricao.insert(0, tree_lista[6])

                        except IndexError:
                            messagebox.showerror('Selecione um dos dados da tabela!')
                # função update
                def update():
                        nome = e_nome.get()
                        endereco = e_endereco.get()
                        pedido = e_pedido.get()
                        pg = e_pg.get()
                        preco = e_preco.get()
                        descricao = e_descricao.get()

                        valor_id = ""

                        lista = [nome, endereco, pedido, pg, preco, descricao, valor_id]

                        if nome == '':
                                messagebox.showerror('Nome não pode ficar vazio!')
                        else:
                                atualizar_info(lista)
                                messagebox.showinfo('Os dados foram atualizados com sucesso!')

                                e_nome.delete(0, 'end')
                                e_endereco.delete(0, 'end')
                                e_pedido.delete(0, 'end')
                                e_pg.delete(0, 'end')
                                e_preco.delete(0, 'end')
                                e_descricao.delete(0, 'end')

                        for widget in frame_direita.winfo_children():
                                widget.destroy()

                                mostrar()

                                # Botao Atualizar
                                b_confirmar = Button(frame_baixo, command=update, text='Confirmar', width=10, anchor=NW, font=('Ivy 10 bold'), bg=co2, fg=co1, relief='raised', overrelief='ridge')
                                b_confirmar.place(x=110, y=340)
                            
                    


                # função delete
                def deletar():
                        try:
                                treev_dados = tree.focus()
                                treev_dicionario = tree.item(treev_dados)
                                tree_lista = treev_dicionario['values']

                                valor_id = tree_lista[0]

                                deletar_info(valor_id)
                                messagebox.showerror('Os dados foram deletados com sucesso!')

                                for widget in frame_direita.winfo_children():
                                    widget.destroy()

                                mostrar()

                        except IndexError:
                                messagebox.showerror('Selecione um dos dados da tabela!') 
                
                        
                ############### Configurando o frame baixo ##################

                # Nome
                l_nome = Label(frame_baixo, text='Nome *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
                l_nome.place(x=10, y=10)
                e_nome = Entry(frame_baixo, width=45, justify='left', relief='solid')
                e_nome.place(x=15, y=40)

                # Endereço
                l_endereco = Label(frame_baixo, text='Endereço *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
                l_endereco.place(x=10, y=70)
                e_endereco = Entry(frame_baixo, width=45, justify='left', relief='solid')
                e_endereco.place(x=15, y=100)

                # Pedido
                l_pedido = Label(frame_baixo, text='Pedido *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
                l_pedido.place(x=10, y=130)
                e_pedido = Entry(frame_baixo, width=45, justify='left', relief='solid')
                e_pedido.place(x=15, y=160)

                # Forma de de pagamento 
                l_pg = Label(frame_baixo, text='F. de Pagamento *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
                l_pg.place(x=10, y=190)
                e_pg = Entry(frame_baixo, width=17, justify='left', relief='solid')
                e_pg.place(x=15, y=220)

                # Preço
                l_preco = Label(frame_baixo, text='Preço *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
                l_preco.place(x=160, y=190)
                e_preco = Entry(frame_baixo, width=20, justify='left', relief='solid')
                e_preco.place(x=160, y=220)

                # Descrição
                l_descricao = Label(frame_baixo, text='Descrição do pedido *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
                l_descricao.place(x=10, y=260)
                e_descricao = Entry(frame_baixo, width=45, justify='left', relief='solid')
                e_descricao.place(x=15, y=290)



                ########### BOTÕES ###########
                # Botao inserir
                b_inserir = Button(frame_baixo, command=inserir, text='Inserir', width=10, anchor=NW, font=('Ivy 10 bold'), bg=co6, fg=co1, relief='raised', overrelief='ridge')
                b_inserir.place(x=15, y=340)

                # Botao Atualizar
                b_inserir = Button(frame_baixo, command=atualizar, text='Atualizar', width=10, anchor=NW, font=('Ivy 10 bold'), bg=co2, fg=co1, relief='raised', overrelief='ridge')
                b_inserir.place(x=110, y=340)

                # Botao Deletar
                b_inserir = Button(frame_baixo, command=deletar, text='Deletar', width=10, anchor=NW, font=('Ivy 10 bold'), bg=co7, fg=co1, relief='raised', overrelief='ridge')
                b_inserir.place(x=205, y=340)

                ################# Frame direita ################3

                def mostrar():

                        global tree
                                    
                        # Lista para cabeçalho 
                        tabela_head = ['ID', 'Nome', 'Endereço', 'Pedido', 'F. pagamento', 'Preço', 'Descrição']

                        # Criando a tabela
                        tree = ttk.Treeview(frame_direita, selectmode="extended", columns=tabela_head, show="headings")

                        # Vertical scrollbar
                        vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)

                        # Horizontal scrollbar
                        hsb = ttk.Scrollbar(frame_direita, orient="horizontal", command=tree.xview)

                        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
                        tree.grid(column=0, row=0, sticky='nsew')
                        vsb.grid(column=1, row=0, sticky='ns')
                        hsb.grid(column=0, row=1, sticky='ew')
                        frame_direita.grid_rowconfigure(0, weight=12)

                        hd=["nw", "nw", "nw", "nw", "nw", "center", "center"]
                        h=[30, 170, 140, 100, 120, 50, 100]
                        n=0

                        for col in tabela_head:
                                tree.heading(col, text=col.title(), anchor=CENTER)
                        # adjust the column's width to the header string 
                        tree.column(col, width=h[n], anchor=hd[n])

                        n+=1

                        for item in lista:
                                tree.insert('', 'end', values=item)


                        mostrar()


                # Botão para fechar o programa
                    # btn_fechar = tk.Button(menu_screen, text='Fechar Programa', command=menu_screen.destroy)
                    # btn_fechar.pack(pady=10)

                    
                janela.mainloop()

            def cadastrarUsers():
                # TELA DE CADASTRO
                cad = Tk()
                corDeFundo= '#0b2e3b'
                cad.title('cadastro')
                cad["bg"] = corDeFundo
                cad.geometry("300x300+100+100")
                cad.resizable(width=False, height=False)

                title = Label(cad, text='Cadastro', bg=corDeFundo, foreground='white', font=20)
                title.pack(side=TOP, fill=X)


                nomer = Label(cad, text='Nome:', bg=corDeFundo, foreground='white')
                nomer.place(x=46, y=50)
                nomeF = Entry(cad)
                nomeF.place(x=90, y=50)


                user = Label(cad, text='Usuario:', bg=corDeFundo, foreground='white')
                user.place(x=36, y=90)
                userF = Entry(cad, show="•")
                userF.place(x=90, y=90)

                password = Label(cad, text='Senha:', bg=corDeFundo, foreground='white')
                password.place(x=44, y=130)
                passwordF = Entry(cad, show="•")
                passwordF.place(x=90, y=130)


                enter = Button(cad, width='11', text='Cadastrar')
                enter.place(x=115, y=180)
                enter = Button(cad, width='11', text='Volta')
                enter.place(x=115, y=220)

                cad.mainloop()
                

            # Criação do menu
            barraDeMenus = Menu(app)
            menuContatos = Menu(barraDeMenus, tearoff=0)
            menuContatos.add_command(label="Fazer pedido", command=fazer_pedido)
            menuContatos.add_command(label="Cadastrar", command=cadastrarUsers)
            menuContatos.add_separator()
            
            menuContatos.add_command(label="Sair", command=exit)
            barraDeMenus.add_cascade(label="Menu", menu=menuContatos)
            app.config(menu=barraDeMenus)



    except:
             messagebox.showerror(title="Conta não encontrada", message="Certifique-se que já está cadastrado! ")

    mainloop()
    
# TELA DE LOGIN
login = Tk()
corDeFundo= '#0b2e3b'
login.title('LOGIN')
login["bg"] = corDeFundo
login.geometry("300x300+100+100")
login.resizable(width=False, height=False)


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