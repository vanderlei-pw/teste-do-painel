from flask import Flask, jsonify, request
import sqlite3  # Substitua por outro banco se necessário

app = Flask(__name__)

# Configuração do banco de dados
DATABASE = 'seu_banco_de_dados.db'

# Função para conectar ao banco
def db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Rota para listar clientes
@app.route('/clientes', methods=['GET'])
def get_clientes():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify(clientes)

# Rota para bloquear cliente
@app.route('/clientes/bloquear', methods=['POST'])
def bloquear_cliente():
    data = request.json
    cliente_id = data['id']
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE clientes SET status = 'bloqueado' WHERE id = ?", (cliente_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Cliente bloqueado com sucesso!'})

# Rota para desbloquear cliente
@app.route('/clientes/desbloquear', methods=['POST'])
def desbloquear_cliente():
    data = request.json
    cliente_id = data['id']
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE clientes SET status = 'ativo' WHERE id = ?", (cliente_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Cliente desbloqueado com sucesso!'})

if __name__ == '__main__':
    app.run(debug=True)
