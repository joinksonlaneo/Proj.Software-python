#importando sqlite
import sqlite3 as lite 


# criando conexão
con = lite.connect('dados.db')

lista = ['Pedro Farias', 'Rua 7, Nº02 - Timbó', '1. Tapioca', 'Pix', 5,00 , 'Sem sal']

# inserir informaçoes
def inserir_info(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO formulario (Nome, Endereço, Pedido, F. pagamento, Preço, Descrição) VALUES (?,?,?,?,?)"
        cur.execute(query, i)


# READ - acessar informações
def mostrar_info():
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * from formulario"
        cur.execute(query)
        informacao = cur.fetchall
       
        for i in informacao:
            lista.append(i)
    return lista



lista = ['Aloisio', 1]
# UPDATE - atualizar informações
def atualizar_info(i):
    with con:
        cur = con.cursor()
        query = "UPDATE formulario set nome=?, endereco=?, pedido=?, pg=?, nome=? , preco=?, descricao=?  WHERE id=?"
        cur.execute(query, i)


# DELETE - deletar informações
def deletar_info(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM formulario WHERE id=?"
        cur.execute(query, i)
    

