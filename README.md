# Projeto - Software Product
 
Linguagens Utilizadas:
	SQL
	PYTHON
PREPARAÇÃO:
Instalar IDE Python
	Utilizado no projeto – PyCharm
	download PyCharm
Instalar SGBD
	Utilizado no projeto – MySQL
	MySQL :: MySQL Downloads
Abrir SGBD
Abrir o IDE Python
	Abrir o terminal da IDE 
Instalar a biblioteca MySQL Connector
			Pip install mysql-connector-python

CRIANDO O BANCO DE DADOS:
No IDE Python
	Abrir o arquivo Bd.py
		Executar o código
		Obs1: Para o código rodar em seu equipamento é necessário alterar as linhas 12 e 21 do código.
conectar = conectarMysql('localhost', 'root', 'XXXXXX')
conectarMysql('localhost', 'root', 'XXXXXX', 'bdprojetoimpacta')
		Os campos que devem obrigatoriamente ser alterados é o de senha de acesso ao MySQL, identificados por XXXXXX.
		Caso o MySQL esteja hospedado em outra local, diferente do equipamento que está executando o código, deve ser alterado o primeiro campo, que no código está como localhost.

UTILIZANDO A GESTÃO DE RECUPERAÇÃO JUDICIAL
No IDE Python
	Abrir o arquivo AC1.py
