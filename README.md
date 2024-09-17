# Projeto: AImpress

## Integrantes:

552421 - Flavio Sousa Vasconcelos

552368 - WELLINGTON DE OLIVEIRA URCINO DA SILVA

97887 - João Carlos França Figueiredo

550200 - Leonardo Oliveira Esparza

# Descrição

Este projeto é uma aplicação web desenvolvida em Python utilizando o framework Flask. A aplicação conecta-se a um banco de dados SQL Azure para gerenciar informações de usuários e seus respectivos currículos. Ela permite realizar operações CRUD (Create, Read, Update, Delete) nas tabelas Usuario e Curriculo, além de executar consultas que relacionam os dados dessas tabelas através de operações JOIN.

## Componentes Principais

Banco de Dados SQL Azure

Tabela Usuario: Armazena informações básicas dos usuários, como ID, nome e e-mail.
Tabela Curriculo: Contém detalhes dos currículos dos usuários, incluindo educação, experiência e habilidades. Relaciona-se com a tabela Usuario através da chave estrangeira usuario_id.
Aplicação Flask

Conexão com o Banco de Dados: Utiliza a biblioteca pyodbc para conectar-se ao SQL Azure.
# Rotas da API:

## Usuários:
GET /usuarios: Lista todos os usuários.

GET /usuarios/<usuario_id>: Obtém um usuário específico.

POST /usuarios: Cria um novo usuário.

PUT /usuarios/<usuario_id>: Atualiza um usuário existente.

DELETE /usuarios/<usuario_id>: Remove um usuário.

## Currículos:

GET /curriculos: Lista todos os currículos.

GET /curriculos/<curriculo_id>: Obtém um currículo específico.

POST /curriculos: Cria um novo currículo.

PUT /curriculos/<curriculo_id>: Atualiza um currículo existente.

DELETE /curriculos/<curriculo_id>: Remove um currículo.

Consulta com JOIN:

GET /usuarios_curriculos: Retorna uma lista de usuários com seus respectivos currículos.
Dependências

Python 3.x
Flask
pyodbc
Driver ODBC para SQL Server

# Instalação e Configuração

Clonar o Repositório

Faça o download ou clone este repositório em sua máquina local.

Configurar o Banco de Dados

Crie as tabelas Usuario e Curriculo no SQL Azure utilizando os scripts SQL fornecidos.
Insira dados iniciais nas tabelas utilizando os comandos INSERT de exemplo.
Configurar o Ambiente Python

Criar um Ambiente Virtual (recomendado):
python -m venv venv

Instalar as Dependências:
pip install -r requirements.txt

Instalar o Driver ODBC:
Certifique-se de que o ODBC Driver 17 for SQL Server está instalado no seu sistema.

Configurar a Aplicação

Edite o arquivo app.py e atualize as informações de conexão com o banco de dados:
server = 'seu_servidor.database.windows.net'
database = 'seu_banco_de_dados'
username = 'seu_usuario'
password = 'sua_senha'

Utilização da Aplicação

Você pode interagir com a API utilizando ferramentas como Postman, Insomnia ou cURL.

# Exemplos de Requisições

Criar um Novo Usuário

POST http://localhost:5000/usuarios
Body (JSON):
{
    "nome": "Ana Pereira",
    "email": "ana.pereira@example.com"
}

Atualizar um Usuário

PUT http://localhost:5000/usuarios/1
Body (JSON):
{
    "nome": "Ana P. Souza",
    "email": "ana.souza@example.com"
}

Deletar um Usuário

DELETE http://localhost:5000/usuarios/1

Listar Currículos

GET http://localhost:5000/curriculos

Obter Usuários com seus Currículos

GET http://localhost:5000/usuarios_curriculos
