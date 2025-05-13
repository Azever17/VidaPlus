import sqlite3

# Lê o conteúdo do arquivo SQL
with open('create_tables.sql', 'r', encoding='utf-8') as f:
    sql_script = f.read()

# Conecta ao banco e executa o script
conn = sqlite3.connect('vida_plus.db')
cursor = conn.cursor()

try:
    cursor.executescript(sql_script)
    conn.commit()
    print('Tabelas criadas com sucesso!')
except Exception as e:
    print(f'Erro ao criar tabelas: {e}')
finally:
    conn.close() 