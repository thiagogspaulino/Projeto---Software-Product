import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Lili0710',
    database='bdprojetoimpacta',
)
cursor = conexao.cursor()

recuperandas = tk.StringVar
cnpj = tk.StringVar
exposicao = tk.StringVar
dataagc = tk.StringVar
rjextinta = tk.StringVar
administradorjudicial = tk.StringVar
siteadm = tk.StringVar
contatoadm = tk.StringVar


TelaInicial = tk.Tk()

#def ResetarCampos():
    #nomerec.delete()

def ConsultarRec():

    #ConsultaRec = f'SELECT recuperandas, cnpj, exposicao, dataagc, rjextinta FROM dados_rj'
    #cursor.execute(ConsultaRec)
    #resultado = cursor.fetchall()
    relrec.insert("1.0", "AINDA NÃO DISPONÍVEL")
    #for linhas in cursor.fetchall():
        #resultado = f'RECUPERANDAS: {linhas.recuperandas}\n CNPJ: {linhas.cnpj}\n EXPOSIÇAO: {linhas.exposicao}\n DATA AGC: {linhas.dataagc}\n RJ EXTINTA: {linhas.rejextinta}'
        #relrec.insert("1.0", resultado)

def ConsultarAj():
    #ConsultaAj = f'SELECT administradorjudicial, siteadm, contatoadm FROM admjud'
    #cursor.execute(ConsultaAj)
    #resultado2 = cursor.fetchall()
    relaj.insert("1.0", "AINDA NÃO DISPONÍVEL")

def CADASTRARRec():
    recuperandas = nomerec.get()
    cnpj = cnpjrec.get()
    exposicao = exp.get()
    dataagc = data.get()
    rjextinta = fim.get()
    if recuperandas is None or recuperandas == '':
        tkinter.messagebox.showinfo(title="AVISO",
        message="Os campos RECUPERANDAS, CNPJ, EXPOSIÇÃO e RJ Encerrada precisam ser preenchidos")
        return
    elif cnpj is None or cnpj == '' or exposicao is None or exposicao == '' or rjextinta is None or rjextinta == '':
        tkinter.messagebox.showinfo(title="AVISO",
        message="Os campos RECUPERANDAS, CNPJ, EXPOSIÇÃO e RJ Encerrada precisam ser preenchidos")
        return
    IncluiRecBD = f'INSERT INTO dados_rj (recuperandas, cnpj, exposicao, dataagc, rjextinta) VALUES ("{recuperandas}", "{cnpj}", {exposicao}, "{dataagc}", "{rjextinta}")'
    cursor.execute(IncluiRecBD)
    conexao.commit()
    tkinter.messagebox.showinfo(title= "INCLUSÃO CONFIRMADA", message= "Inclusão da Recuperanda Realizada com Sucesso")
    nomerec.delete(0,tk.END)
    cnpjrec.delete(0, tk.END)
    exp.delete(0, tk.END)
    data.delete(0, tk.END)
    fim.delete(0, tk.END)
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
relrec = tk.Text()
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
botaoincrec = tk.Button(text= "CONFIRMAR INCLUSÃO RECUPERANDA", command=CADASTRARRec)

menuaj = tk.Label(text= "MENU ADMINISTRADOR JUDICIAL")
titmenuaj = tk.Label(text= "VISUALIZE O ADMINISTRADOR JUDICIAL")
relaj = tk.Text()
botaoconsaj = tk.Button(text= "Consultar Adm Jud", command = ConsultarAj)
titmenuincaj = tk.Label(text= "DIGITE OS DADOS PARA INCLUSÃO DO ADMINISTRADOR JUDICIAL")
titnomeaj = tk.Label(text= "ADMINISTRADOR JUDICIAL")
nomeaj = tk.Entry()
titsiteaj = tk.Label(text= "SITE DO AJ")
siteaj = tk.Entry()
titcontatoaj = tk.Label(text= "CONTATO DO AJ")
contatoaj = tk.Entry()
botaoincaj = tk.Button(text= "CONFIRMAR INCLUSÃO DO AJ", command=CADASTRARAdmJud)

menurec.grid(row = 1, column = 1, rowspan = 2, columnspan = 9)
titmenurec.grid(row = 4, column = 1, columnspan = 9)
relrec.grid(row = 7, column = 1, rowspan = 5, columnspan = 9)
botaoconsrec.grid(row = 12, column =4, columnspan = 3)
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

menuaj.grid(row = 1, column = 12, rowspan = 2, columnspan = 9)#, color =  Red)
titmenuaj.grid(row = 4, column = 12, columnspan = 9)
relaj.grid(row = 7, column = 12, rowspan = 5, columnspan = 9)
botaoconsaj.grid(row = 12, column =15, columnspan = 3)
titmenuincaj.grid(row = 13, column = 12, columnspan = 9)
titnomeaj.grid(row = 15, column = 12, columnspan = 5)
nomeaj.grid(row = 16, column = 12, columnspan = 5)
titsiteaj.grid(row = 15, column = 18, columnspan = 3)
siteaj.grid(row = 16, column = 18, columnspan = 3)
titcontatoaj.grid(row = 18, column = 12, columnspan = 4)
contatoaj.grid(row = 19, column = 12, columnspan = 4)
botaoincaj.grid(row = 18, column = 17, columnspan = 4, rowspan = 2)

TelaInicial.mainloop()


cursor.close()
conexao.close