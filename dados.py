import sqlite3

# Conecta (ou cria) o banco de dados
conn = sqlite3.connect('banco.db')
cursor = conn.cursor()

