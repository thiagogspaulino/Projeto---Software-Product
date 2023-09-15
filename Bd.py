from mysql.connector import connect

def conectarMysql(host, user, passwd, database=None):
    conectar = connect(
        host = host,
        user = user,
        passwd = passwd,
        database = database
    )
    return conectar

conectar = conectarMysql('localhost', 'root', 'XXXXXX')

banco = '''
    CREATE DATABASE IF NOT EXISTS bdprojetoimpacta
'''
cursor = conectar.cursor()
cursor.execute(banco)
conectar.close()

conectar = conectarMysql('localhost', 'root', 'XXXXXX', 'bdprojetoimpacta')

criartabeladados_rj = """
CREATE TABLE IF NOT EXISTS dados_rj (
    iddados_rj INT AUTO_INCREMENT PRIMARY KEY,
    recuperandas VARCHAR(45) NOT NULL,
    cnpj VARCHAR(18) NOT NULL,
    exposicao DECIMAL(15, 2) NOT NULL,
    dataagc VARCHAR(10),
    rjextinta VARCHAR(3) NOT NULL
);
"""

criartabelaadmuj = """
CREATE TABLE IF NOT EXISTS admjud (
    iddados_rj INT AUTO_INCREMENT PRIMARY KEY,
    administradorjudicial VARCHAR(45) NOT NULL,
    siteadm VARCHAR(45) NOT NULL,
    contatoadm VARCHAR(45) NOT NULL
);
"""

cursor = conectar.cursor()
cursor.execute(criartabeladados_rj)
cursor.execute(criartabelaadmuj)

conectar.close()
