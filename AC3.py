import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
import mysql.connector

#Criando a conexão com o MySql
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Lili0710',
    database='bdprojetoimpacta',
)
cursor = conexao.cursor()

#Criando as variáveis do código
#Variáveis do Cadastro das Recuperandas e Adms Juds
recuperandas = tk.StringVar
cnpj = tk.StringVar
exposicao = tk.StringVar
dataagc = tk.StringVar
rjextinta = tk.StringVar
administradorjudicial = tk.StringVar
siteadm = tk.StringVar
contatoadm = tk.StringVar
id_rec_var = tk.StringVar


#Criando a Janela principal do sistema
TelaInicial = tk.Tk()

def DadosRec():
    global id_rec_var
    nomerec.delete(0, tk.END)
    cnpjrec.delete(0, tk.END)
    exp.delete(0, tk.END)
    data.delete(0, tk.END)
    fim.delete(0, tk.END)
    dados_rec_selecionados = relrec.focus()
    rec_selecionada = relrec.item(dados_rec_selecionados)
    nome_rec = rec_selecionada['values'][0]
    cnpj_rec = rec_selecionada['values'][1]
    exp_rec = rec_selecionada['values'][2]
    data_rec = rec_selecionada['values'][3]
    ext_rec = rec_selecionada['values'][4]
    id_rec = rec_selecionada['values'][5]
    nomerec.insert(0,nome_rec)
    cnpjrec.insert(0, cnpj_rec)
    exp.insert(0,exp_rec)
    data.insert(0,data_rec)
    fim.insert(0, ext_rec)
    id_rec_var = id_rec

#Função que consulta os dados das recuperandas
def ConsultarRec():
    relrec.delete(*relrec.get_children())
    ConsultaRec = "SELECT recuperandas, cnpj, exposicao, dataagc, rjextinta, iddados_rj FROM dados_rj"
    cursor.execute(ConsultaRec)
    resultados = cursor.fetchall()
    for resultado in resultados:
        relrec.insert(parent= "", index= "end", values= resultado)

def ConsultarAj():
    relaj.delete(*relaj.get_children())
    ConsultaAj = f'SELECT administradorjudicial, siteadm, contatoadm FROM admjud'
    cursor.execute(ConsultaAj)
    resultados2 = cursor.fetchall()
    for resultado2 in resultados2:
        relaj.insert("", index = "end", values = resultado2)

def AlterarRec():
    global id_rec_var
    recuperandas = nomerec.get()
    cnpj = cnpjrec.get()
    exposicao = exp.get()
    dataagc = data.get()
    rjextinta = fim.get()
    AlteraRecBD = f'UPDATE dados_rj SET recuperandas = "{recuperandas}", cnpj = "{cnpj}", exposicao = "{exposicao}", dataagc = "{dataagc}", rjextinta = "{rjextinta}" WHERE iddados_rj = {id_rec_var}'
    cursor.execute(AlteraRecBD)
    conexao.commit()
    tkinter.messagebox.showinfo(title="ALTERAÇÃO CONFIRMADA", message="Alteração da Recuperanda Realizada com Sucesso")
    nomerec.delete(0, tk.END)
    cnpjrec.delete(0, tk.END)
    exp.delete(0, tk.END)
    data.delete(0, tk.END)
    fim.delete(0, tk.END)
    ConsultarRec()

def CADASTRARRec():
    recuperandas = nomerec.get()
    cnpj = cnpjrec.get()
    exposicao = exp.get()
    dataagc = data.get()
    rjextinta = fim.get()
    IncluiRecBD = f'INSERT INTO dados_rj (recuperandas, cnpj, exposicao, dataagc, rjextinta) VALUES ("{recuperandas}", "{cnpj}", {exposicao}, "{dataagc}", "{rjextinta}")'
    cursor.execute(IncluiRecBD)
    conexao.commit()
    tkinter.messagebox.showinfo(title= "INCLUSÃO CONFIRMADA", message= "Inclusão da Recuperanda Realizada com Sucesso")
    nomerec.delete(0,tk.END)
    cnpjrec.delete(0, tk.END)
    exp.delete(0, tk.END)
    data.delete(0, tk.END)
    fim.delete(0, tk.END)
    ConsultarRec()
def CADASTRARAdmJud():
    administradorjudicial = nomeaj.get()
    siteadm = siteaj.get()
    contatoadm = contatoaj.get()
    if administradorjudicial is None or administradorjudicial == '' or siteadm is None or siteadm == '' or contatoadm is None or contatoadm == '':
        tkinter.messagebox.showinfo(title="AVISO",
        message="Todos os campos devem ser preenchidos.")
        return
    IncluirAdm = f'INSERT INTO admjud (administradorjudicial, siteadm, contatoadm) VALUES ("{administradorjudicial}", "{siteadm}", "{contatoadm}")'
    cursor.execute(IncluirAdm)
    conexao.commit()
    tkinter.messagebox.showinfo(title="INCLUSÃO CONFIRMADA", message="Inclusão do AJ Realizado com Sucesso")
    nomeaj.delete(0, tk.END)
    siteaj.delete(0, tk.END)
    contatoaj.delete(0, tk.END)

def Verificar():
    recuperandas = nomerec.get()
    cnpj = cnpjrec.get()
    exposicao = exp.get()
    dataagc = data.get()
    rjextinta = fim.get()
    if recuperandas is None or recuperandas == '' or cnpj is None or cnpj == '' or exposicao is None or exposicao == '' or rjextinta is None or rjextinta == '':
        tkinter.messagebox.showinfo(title="AVISO",
        message="Os campos RECUPERANDAS, CNPJ, EXPOSIÇÃO e RJ Encerrada precisam ser preenchidos")
        return
    sejaexiste1 = f'SELECT EXISTS (SELECT * FROM dados_rj WHERE cnpj = "{cnpj}")'
    cursor.execute(sejaexiste1)
    resultado = cursor.fetchone()
    sejaexiste2 = f'SELECT EXISTS (SELECT * FROM dados_rj WHERE recuperandas = "{recuperandas}")'
    cursor.execute(sejaexiste2)
    resultado2 = cursor.fetchone()
    if resultado[0] or resultado2[0]:
        AlterarRec()
    else:
        CADASTRARRec()

TelaInicial.state("zoomed")
TelaInicial.rowconfigure([3,5,12,14,17,20],weight = 1)
TelaInicial.columnconfigure([10,11],weight = 1)
TelaInicial.title("GESTÃO DE RECUPERAÇÃO JUDICIAL")
divmeio = tk.Label(text= " ")
divmeio.grid(row = 1, column = 10, rowspan = 28, columnspan = 2)
linhacima = tk.Label(text= " ")
linhacima.grid(row = 0, column = 0, columnspan = 22)
linhadir = tk.Label(text= " ")
linhadir.grid(row= 0, column = 21, rowspan = 28)
linhaesq = tk.Label(text= " ")
linhaesq.grid(row= 0, column = 0, rowspan = 28)
linhabai = tk.Label(text= " ")
linhabai.grid(row = 28, column = 0, columnspan = 22)

menurec = tk.Label(text= "MENU RECUPERANDAS")
titmenurec = tk.Label(text= "VISUALIZE AS RECUPERANDAS")
relrec = ttk.Treeview(columns= ("coluna 1", "coluna 2", "coluna 3", "coluna 4", "coluna 5","coluna 6"))
botaoconsrec = tk.Button(text= "Consultar Recuperandos", command = ConsultarRec)
titmenuincrec = tk.Label(text= "DIGITE OS DADOS PARA INCLUSÃO DA RECUPERANDA")
titnomerec = tk.Label(text= " NOME DA RECUPERANDA")
nomerec = tk.Entry()
titcnpj = tk.Label(text= "CNPJ - Use o padrão xx.xxx.xxx/xxxx-x")
cnpjrec = tk.Entry()
titexp = tk.Label(text = "EXPOSIÇÃO (em R$)")
exp = tk.Entry()
titdata = tk.Label(text= "DATA AGC - Se houver")
data = tk.Entry()
titfim = tk.Label(text = "RJ ENCERRADA - Sim/Não")
fim = tk.Entry()
botaoincrec = tk.Button(text= "CONFIRMAR INCLUSÃO/ALTERAÇÃO RECUPERANDA", command = Verificar)

menuaj = tk.Label(text= "MENU ADMINISTRADOR JUDICIAL")
titmenuaj = tk.Label(text= "VISUALIZE O ADMINISTRADOR JUDICIAL")
relaj = ttk.Treeview(columns= ("coluna 1", "coluna 2", "coluna 3"))
botaoconsaj = tk.Button(text= "Consultar Adm Jud", command = ConsultarAj)
titmenuincaj = tk.Label(text= "DIGITE OS DADOS PARA INCLUSÃO DO ADMINISTRADOR JUDICIAL")
titnomeaj = tk.Label(text= "ADMINISTRADOR JUDICIAL")
nomeaj = tk.Entry()
titsiteaj = tk.Label(text= "SITE DO AJ")
siteaj = tk.Entry()
titcontatoaj = tk.Label(text= "CONTATO DO AJ")
contatoaj = tk.Entry()
botaoincaj = tk.Button(text= "CONFIRMAR INCLUSÃO/ALTERAÇÃO DO AJ", command=CADASTRARAdmJud)

menurec.grid(row = 1, column = 1, rowspan = 2, columnspan = 9)
titmenurec.grid(row = 4, column = 1, columnspan = 9)
relrec.grid(row = 7, column = 1, rowspan = 5, columnspan = 9)
relrec.column("#0", width = 0, stretch= 'NO')
relrec.column("coluna 1", width = 150)
relrec.column("coluna 2", width = 120)
relrec.column("coluna 3", width = 120)
relrec.column("coluna 4", width = 90)
relrec.column("coluna 5", width= 90)
relrec.column("coluna 6", width= 0, stretch = "NO")
relrec.heading("#0", text= "")
relrec.heading("coluna 1", text= "Recuperandas")
relrec.heading("coluna 2", text= "CNPJ")
relrec.heading("coluna 3", text= "Exposição (em R$)")
relrec.heading("coluna 4", text= "Data AGC")
relrec.heading("coluna 5", text= "RJ Extinta?")
botaoconsrec.grid(row = 12, column = 1, columnspan = 3)
titmenuincrec.grid(row = 13, column = 1, columnspan = 9)
titnomerec.grid(row = 15, column = 1, columnspan = 5)
nomerec.grid(row = 16, column = 1, columnspan = 5)
titcnpj.grid(row = 15, column = 7, columnspan = 3)
cnpjrec.grid(row = 16, column = 7, columnspan = 3)
titexp.grid(row = 18, column = 1, columnspan = 3)
exp.grid(row = 19, column = 1, columnspan = 3)
titdata.grid(row = 18, column = 5, columnspan = 2)
data.grid(row = 19, column = 5, columnspan = 2)
titfim.grid(row = 18, column = 8, columnspan = 2)
fim.grid(row = 19, column = 8, columnspan = 2)
botaoincrec.grid(row = 21, column = 2, rowspan = 2, columnspan = 7)

menuaj.grid(row = 1, column = 12, rowspan = 2, columnspan = 9)
titmenuaj.grid(row = 4, column = 12, columnspan = 9)
relaj.grid(row = 7, column = 12, rowspan = 5, columnspan = 9)
relaj.column("#0", width = 0, stretch= 'NO')
relaj.column("coluna 1", width = 200)
relaj.column("coluna 2", width = 200)
relaj.column("coluna 3", width = 200)
relaj.heading("#0", text= "")
relaj.heading("coluna 1", text= "Adm Judicial")
relaj.heading("coluna 2", text= "Site Adm")
relaj.heading("coluna 3", text= "Contato Adm")

botaoconsaj.grid(row = 12, column =12, columnspan = 3)

titmenuincaj.grid(row = 13, column = 12, columnspan = 9)
titnomeaj.grid(row = 15, column = 12, columnspan = 5)
nomeaj.grid(row = 16, column = 12, columnspan = 5)
titsiteaj.grid(row = 15, column = 18, columnspan = 3)
siteaj.grid(row = 16, column = 18, columnspan = 3)
titcontatoaj.grid(row = 18, column = 12, columnspan = 4)
contatoaj.grid(row = 19, column = 12, columnspan = 4)
botaoincaj.grid(row = 18, column = 17, columnspan = 4, rowspan = 2)

botaoteste = tk.Button(TelaInicial, text = "ALTERAR/DELETAR", command= DadosRec)
botaoteste.grid(row = 12, column = 8, columnspan = 2)
botaotesteAj = tk.Button(TelaInicial, text = "ALTERAR/DELETAR")
botaotesteAj.grid(row = 12, column = 19, columnspan = 2)

TelaInicial.mainloop()

cursor.close()
conexao.close