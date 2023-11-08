from flask import Flask, render_template, request
import mysql.connector


mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345678',
    database='aula_13_10'
)

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/setor')
def setor():
    return render_template('setor.html')

@app.route('/setor', methods=['POST'])
def add_setor():
    nome = request.form['nome']
    cursor.execute(f"INSERT INTO setor (nome) VALUES ('{nome}')")
    cursor.execute('SELECT * FROM setor')
    setores = cursor.fetchall()
    mydb.commit()
    return '<h1>Adicionado com Sucesso</h1>'

@app.route('/cargo')
def cargo():
    return render_template('cargo.html')


@app.route('/cargo', methods=['POST'])
def add_cargo():
    nome = request.form['nome']
    id_setor = request.form['id_setor']
    cursor.execute(f"INSERT INTO cargos (nome, id_setor) VALUES ('{nome}', {id_setor})")
    cursor.execute('SELECT * FROM cargos')
    cargos = cursor.fetchall()
    mydb.commit()
    return '<h1>Adicionado com Sucesso</h1>'


@app.route('/funcionario')
def funcionario():
    return render_template('funcionario.html')


@app.route('/funcionario', methods=['POST'])
def add_funcionario():
    primeiro_nome = request.form['primeiro_nome']
    sobrenome = request.form['sobrenome']
    data_admissao = request.form['data_admissao']
    status_funcionario = request.form['status_funcionario']
    id_setor = request.form['id_setor']
    cursor.execute(f"INSERT INTO funcionarios (primeiro_nome, sobrenome, data_admissao, status_funcionario, id_setor) VALUES ('{primeiro_nome}', '{sobrenome}', '{data_admissao}', '{status_funcionario}', {id_setor})")
    cursor.execute('SELECT * FROM funcionarios')
    funcionarios = cursor.fetchall()
    mydb.commit()
    return '<h1>Adicionado com Sucesso</h1>'


if __name__ == '__main__':
    cursor = mydb.cursor()
    app.run(debug=True)
