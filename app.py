from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Página inicial
@app.route('/')
def index():
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()
    cursor.execute('SELECT aluno.nome, aluno.email, curso.nome FROM aluno JOIN curso ON aluno.curso_id = curso.id')
    alunos = cursor.fetchall()
    cursor.execute('SELECT professor.nome, professor.email, curso.nome FROM professor JOIN curso ON professor.curso_id = curso.id')
    professores = cursor.fetchall()
    cursor.execute('SELECT disciplina.nome, curso.nome FROM disciplina JOIN curso ON disciplina.curso_id = curso.id')
    disciplinas = cursor.fetchall()
    conexao.close()
    return render_template('index.html', alunos=alunos,professores=professores,disciplinas=disciplinas)

# Página de cadastro de Aluno
@app.route('/cadastro_aluno', methods=['GET', 'POST'])
def cadastro_aluno():
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()
    
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        curso_id = request.form['curso_id']
        cursor.execute('INSERT INTO aluno (nome, email, curso_id) VALUES (?, ?, ?)', (nome, email, curso_id))
        conexao.commit()
        conexao.close()
        return redirect('/')
    
    cursor.execute('SELECT * FROM curso')
    cursos = cursor.fetchall()
    conexao.close()
    return render_template('cadastro_aluno.html', cursos=cursos)

# Página de cadastro de Professor
@app.route('/cadastro_professor', methods=['GET', 'POST'])
def cadastro_professor():
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()
    
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        curso_id = request.form['curso_id']
        cursor.execute('INSERT INTO professor (nome, email, curso_id) VALUES (?, ?, ?)', (nome, email, curso_id))
        conexao.commit()
        conexao.close()
        return redirect('/')
    
    cursor.execute('SELECT * FROM curso')
    cursos = cursor.fetchall()
    conexao.close()
    return render_template('cadastro_professor.html', cursos=cursos)

# Página de cadastro de Disciplina
@app.route('/cadastro_disciplina', methods=['GET', 'POST'])
def cadastro_disciplina():
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()
    
    if request.method == 'POST':
        nome = request.form['nome']
        curso_id = request.form['curso_id']
        cursor.execute('INSERT INTO disciplina (nome, curso_id) VALUES (?, ?)', (nome, curso_id))
        conexao.commit()
        conexao.close()
        return redirect('/')
    
    cursor.execute('SELECT * FROM curso')
    cursos = cursor.fetchall()
    conexao.close()
    return render_template('cadastro_disciplina.html', cursos=cursos)

#pagina deletar aluno
@app.route('/deletar_aluno/<int:id>')
def deletar_aluno(id):
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM aluno WHERE id = ?', (id,))
    conexao.commit()
    conexao.close()
    return redirect('/')

#pagina editar aluno
@app.route('/editar_aluno/<int:id>', methods=['GET', 'POST'])
def editar_aluno(id):
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()
    
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        curso_id = request.form['curso_id']
        cursor.execute('UPDATE aluno SET nome=?, email=?, curso_id=? WHERE id=?', (nome, email, curso_id, id))
        conexao.commit()
        conexao.close()
        return redirect('/')
    
    cursor.execute('SELECT * FROM aluno WHERE id = ?', (id,))
    aluno = cursor.fetchone()
    cursor.execute('SELECT * FROM curso')
    cursos = cursor.fetchall()
    conexao.close()
    return render_template('editar_aluno.html', aluno=aluno, cursos=cursos)



if __name__ == '__main__':
    app.run(debug=True)
