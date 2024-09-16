from flask import Flask, request, jsonify
import pyodbc

app = Flask(__name__)

# Configuração da conexão com o banco de dados
server = 'aimpress.database.windows.net'
database = 'Sprint-3'
username = 'RM550200'
password = 'Fiap.1234'

connection_string = (
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=' + server + ';'
    'DATABASE=' + database + ';'
    'UID=' + username + ';'
    'PWD=' + password
)

def get_db_connection():
    conn = pyodbc.connect(connection_string)
    return conn

# CRUD para Usuario

@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Usuario')
    rows = cursor.fetchall()
    usuarios = []
    for row in rows:
        usuarios.append({'id': row.id, 'nome': row.nome, 'email': row.email})
    conn.close()
    return jsonify(usuarios)

@app.route('/usuarios/<int:usuario_id>', methods=['GET'])
def get_usuario(usuario_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Usuario WHERE id = ?', (usuario_id,))
    row = cursor.fetchone()
    usuario = {'id': row.id, 'nome': row.nome, 'email': row.email} if row else {}
    conn.close()
    return jsonify(usuario)

@app.route('/usuarios', methods=['POST'])
def create_usuario():
    novo_usuario = request.get_json()
    nome = novo_usuario['nome']
    email = novo_usuario['email']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Usuario (nome, email) VALUES (?, ?)', (nome, email))
    conn.commit()
    conn.close()
    return jsonify({'mensagem': 'Usuário criado com sucesso!'}), 201

@app.route('/usuarios/<int:usuario_id>', methods=['PUT'])
def update_usuario(usuario_id):
    atualizar_usuario = request.get_json()
    nome = atualizar_usuario['nome']
    email = atualizar_usuario['email']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE Usuario SET nome = ?, email = ? WHERE id = ?', (nome, email, usuario_id))
    conn.commit()
    conn.close()
    return jsonify({'mensagem': 'Usuário atualizado com sucesso!'})

@app.route('/usuarios/<int:usuario_id>', methods=['DELETE'])
def delete_usuario(usuario_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Usuario WHERE id = ?', (usuario_id,))
    conn.commit()
    conn.close()
    return jsonify({'mensagem': 'Usuário deletado com sucesso!'})

# CRUD para Curriculo

@app.route('/curriculos', methods=['GET'])
def get_curriculos():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Curriculo')
    rows = cursor.fetchall()
    curriculos = []
    for row in rows:
        curriculos.append({
            'id': row.id,
            'usuario_id': row.usuario_id,
            'educacao': row.educacao,
            'experiencia': row.experiencia,
            'habilidades': row.habilidades
        })
    conn.close()
    return jsonify(curriculos)

@app.route('/curriculos/<int:curriculo_id>', methods=['GET'])
def get_curriculo(curriculo_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Curriculo WHERE id = ?', (curriculo_id,))
    row = cursor.fetchone()
    curriculo = {
        'id': row.id,
        'usuario_id': row.usuario_id,
        'educacao': row.educacao,
        'experiencia': row.experiencia,
        'habilidades': row.habilidades
    } if row else {}
    conn.close()
    return jsonify(curriculo)

@app.route('/curriculos', methods=['POST'])
def create_curriculo():
    novo_curriculo = request.get_json()
    usuario_id = novo_curriculo['usuario_id']
    educacao = novo_curriculo.get('educacao', '')
    experiencia = novo_curriculo.get('experiencia', '')
    habilidades = novo_curriculo.get('habilidades', '')
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO Curriculo (usuario_id, educacao, experiencia, habilidades) VALUES (?, ?, ?, ?)',
        (usuario_id, educacao, experiencia, habilidades)
    )
    conn.commit()
    conn.close()
    return jsonify({'mensagem': 'Currículo criado com sucesso!'}), 201

@app.route('/curriculos/<int:curriculo_id>', methods=['PUT'])
def update_curriculo(curriculo_id):
    atualizar_curriculo = request.get_json()
    usuario_id = atualizar_curriculo['usuario_id']
    educacao = atualizar_curriculo.get('educacao', '')
    experiencia = atualizar_curriculo.get('experiencia', '')
    habilidades = atualizar_curriculo.get('habilidades', '')
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'UPDATE Curriculo SET usuario_id = ?, educacao = ?, experiencia = ?, habilidades = ? WHERE id = ?',
        (usuario_id, educacao, experiencia, habilidades, curriculo_id)
    )
    conn.commit()
    conn.close()
    return jsonify({'mensagem': 'Currículo atualizado com sucesso!'})

@app.route('/curriculos/<int:curriculo_id>', methods=['DELETE'])
def delete_curriculo(curriculo_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Curriculo WHERE id = ?', (curriculo_id,))
    conn.commit()
    conn.close()
    return jsonify({'mensagem': 'Currículo deletado com sucesso!'})

# SELECT com JOIN

@app.route('/usuarios_curriculos', methods=['GET'])
def get_usuarios_curriculos():
    conn = get_db_connection()
    cursor = conn.cursor()
    query = '''
    SELECT u.id, u.nome, u.email, c.educacao, c.experiencia, c.habilidades
    FROM Usuario u
    JOIN Curriculo c ON u.id = c.usuario_id
    '''
    cursor.execute(query)
    rows = cursor.fetchall()
    resultado = []
    for row in rows:
        resultado.append({
            'usuario_id': row.id,
            'nome': row.nome,
            'email': row.email,
            'educacao': row.educacao,
            'experiencia': row.experiencia,
            'habilidades': row.habilidades
        })
    conn.close()
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)
