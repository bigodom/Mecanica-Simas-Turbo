from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/manutencao')
def manutencao():
    return render_template('manutencao.html')

@app.route('/manutencao/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    placa = request.form['placa']
    data = request.form['data']
    tipo = request.form['tipo']
    valor = request.form['valor']
    observacoes = request.form['observacoes']

    conn = psycopg2.connect(host='localhost', database='manutencao', user='postgres', password='123')
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO manutencao (nome, placa, data, tipo, valor, observacoes) VALUES ('{nome}', '{placa}', '{data}', '{tipo}', '{valor}', '{observacoes}')")
    conn.commit()
    conn.close()

    return redirect(url_for('manutencao'))

@app.route('/manutencao/listar')
def listar():
    conn = psycopg2.connect(host='localhost', database='manutencao', user='postgres', password='123')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM manutencao')
    manutencoes = cursor.fetchall()
    conn.close()

    return render_template('listar.html', manutencoes=manutencoes)

@app.route('/manutencao/excluir/<int:id>')
def excluir(id):
    conn = psycopg2.connect(host='localhost', database='manutencao', user='postgres', password='123')
    cursor = conn.cursor()
    cursor.execute(f'DELETE FROM manutencao WHERE id = {id}')
    conn.commit()
    conn.close()

    return redirect(url_for('listar'))

@app.route('/manutencao/editar/<int:id>')
def editar(id):
    conn = psycopg2.connect(host='localhost', database='manutencao', user='postgres', password='123')
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM manutencao WHERE id = {id}')
    manutencao = cursor.fetchone()
    conn.close()

    return render_template('editar.html', manutencao=manutencao)

@app.route('/manutencao/atualizar', methods=['POST'])
def atualizar():
    id = request.form['id']
    nome = request.form['nome']
    placa = request.form['placa']
    data = request.form['data']
    tipo = request.form['tipo']
    valor = request.form['valor']
    observacoes = request.form['observacoes']

    conn = psycopg2.connect(host='localhost', database='manutencao', user='postgres', password='123')
    cursor = conn.cursor()
    cursor.execute(f"UPDATE manutencao SET nome = '{nome}', placa = '{placa}', data = '{data}', tipo = '{tipo}', valor = '{valor}', observacoes = '{observacoes}' WHERE id = {id}")
    conn.commit()
    conn.close()

    return redirect(url_for('listar'))

@app.route('/manutencao/visualizar/<int:id>')
def visualizar(id):
    conn = psycopg2.connect(host='localhost', database='manutencao', user='postgres', password='123')
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM manutencao WHERE id = {id}')
    manutencao = cursor.fetchone()
    conn.close()

    return render_template('visualizar.html', manutencao=manutencao)

@app.route('/manutencao/limpar')
def limpar():
    conn = psycopg2.connect(host='localhost', database='manutencao', user='postgres', password='123')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM manutencao')
    conn.commit()
    conn.close()

    return redirect(url_for('listar'))

app.run(debug=True)