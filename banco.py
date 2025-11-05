import sqlite3

# Conecta (ou cria) o banco de dados
conn = sqlite3.connect('banco.db')
cursor = conn.cursor()

# Cria a tabela curso
cursor.execute('''
CREATE TABLE IF NOT EXISTS curso (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
)
''')

# Cria a tabela aluno
cursor.execute('''
CREATE TABLE IF NOT EXISTS aluno (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    curso_id INTEGER,
    FOREIGN KEY (curso_id) REFERENCES curso(id)
)
''')
# Cria a tabela Professor
cursor.execute('''
CREATE TABLE IF NOT EXISTS professor (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    curso_id INTEGER,
    FOREIGN KEY (curso_id) REFERENCES curso(id)
)
''')
# Cria a tabela Disciplina
cursor.execute('''
CREATE TABLE IF NOT EXISTS disciplina (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    curso_id INTEGER,
    FOREIGN KEY (curso_id) REFERENCES curso(id)
)
''')

# Adiciona cursos iniciais
cursor.execute("INSERT INTO curso (nome) VALUES ('Engenharia de Software')")
cursor.execute("INSERT INTO curso (nome) VALUES ('Ciência da Computação')")
cursor.execute("INSERT INTO curso (nome) VALUES ('Sistemas de Informação')")

conn.commit()
conn.close()

print("Banco de dados criado com sucesso!")
