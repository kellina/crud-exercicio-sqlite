import sqlite3
import csv

DB_NAME = "faculdade.db"

def init_db():
  try:
    print("Criando tabelas...")
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS notas')
    cursor.execute('DROP TABLE IF EXISTS disciplina')
    cursor.execute('DROP TABLE IF EXISTS alunos')

    sql_query_alunos = '''
              CREATE TABLE alunos (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                cpf VARCHAR(11) NOT NULL UNIQUE,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                matricula INTEGER NOT NULL UNIQUE,
                disciplina_id TEXT,
                FOREIGN KEY (disciplina_id) REFERENCES disciplina (id)
              )
              '''
    sql_query_disciplina = '''
              CREATE TABLE disciplina (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                codigo INTEGER NOT NULL UNIQUE
              )
              '''
    sql_query_notas = '''
              CREATE TABLE notas (
                aluno_id INTEGER,
                disciplina_id INTEGER,
                nota1 NUMERIC NOT NULL,
                nota2 NUMERIC NOT NULL,
                nota3 NUMERIC NOT NULL,
                FOREIGN KEY (aluno_id) REFERENCES aluno (id),
                FOREIGN KEY (disciplina_id) REFERENCES disciplina (id)
              )
              '''
    cursor.execute(sql_query_disciplina)
    cursor.execute(sql_query_alunos)
    cursor.execute(sql_query_notas)
    print('Tabelas criadas com sucesso!\n')
  finally:
    if conn:
      conn.close()
          
def feed_db():
  conn = sqlite3.connect(DB_NAME)
  cursor = conn.cursor()
  try:
    print('Populando as tabelas....\n')
    
    ''' INSERT '''
    disciplinas = [
        ('Calculo',	'CK2342'),
        ('Algoritmo',	'CK4537'),
        ('Python',	'CK4533'),
        ('Banco de dados',	'CK7534')
    ]
    cursor.executemany('''
            INSERT INTO disciplina (nome, codigo)
            VALUES (?, ?)
            ''', disciplinas)

    alunos = [
        ('123456789-12',	'Maria Lucia',	'lucia@mail.com', 123,	1),
        ('111222333-44',	'Paulo Rogerio',	'paulo@mail.com', 789,	2),
        ('121213145-14',	'Ana Julia',	'julia@mail',	222,	3),
        ('252131245-15',	'Maria Raquel',	'raquel@mail',	225,	4),
        ('444545145-45',	'Pedro Luis',	'luis@mail.com',	456,	1),
        ('789456123-78',	'Joao Vitor',	'vitor@mail',	232,	4)
    ]
    cursor.executemany('''
      INSERT INTO alunos (cpf, nome, email, matricula, disciplina_id)
      VALUES (?, ?, ?, ?, ?)
      ''', alunos)

    notas = [
      (1, 1, 7.5, 8.0, 8.5),
      (2, 2, 9.8, 9.5, 10.0),
      (3, 3, 7.0, 6.8, 9.5),
      (4, 4, 8.8, 8.5, 10.0),
      (5, 1, 5.5, 6.0, 5.0),
      (6, 4, 5.8, 7.5, 6.0)
    ]
    cursor.executemany('''
      INSERT INTO notas (aluno_id, disciplina_id, nota1, nota2, nota3)
      VALUES (?, ?, ?, ?, ?)
      ''', notas)
    print('Tabelas alimentadas')
    conn.commit()
  finally:
    conn.close()

def query_disciplinas():
  conn = sqlite3.connect(DB_NAME)
  cursor = conn.cursor()
  try:
    cursor.execute('''
      SELECT d.codigo, d.nome
      FROM
        disciplina d
    ''')
    rows = cursor.fetchall()
    arquivo = open('disciplinas.csv', 'w')
    meu_arquivo = csv.writer(arquivo)
    meu_arquivo.writerows(rows)
    arquivo.close()
    return rows

  finally:
    conn.close()

def query_situacao_aluno():
  conn = sqlite3.connect(DB_NAME)
  cursor = conn.cursor()
  try:
    cursor.execute('''
      SELECT
        a.matricula,
        a.nome,
        n.nota1,
        n.nota2,
        n.nota3,
        CASE
          WHEN round((n.nota1 + n.nota2 + n.nota3)/3.0, 2) > 6 THEN  'Aprovado'
          ELSE 'Reprovado'
        END resultado
      FROM
        alunos a
        INNER JOIN notas n ON (a.id = n.aluno_id)
    ''')
    rows = cursor.fetchall()
    arquivo = open('situacao_aluno.csv', 'w')
    meu_arquivo = csv.writer(arquivo)
    meu_arquivo.writerows(rows)
    arquivo.close()
  
    return rows
    
  finally:
    conn.close()

def query_alunos():
  conn = sqlite3.connect(DB_NAME)
  cursor = conn.cursor()
  try:
    cursor.execute('''
      SELECT
        a.cpf, a.matricula, a.nome, a.email,
        d.codigo as cod_disciplina,
        d.nome as nome_disciplina
      FROM
        alunos a
        INNER JOIN disciplina d ON (a.disciplina_id = d.id)
    ''')
    rows = cursor.fetchall()
    arquivo = open('alunos.csv', 'w')
    meu_arquivo = csv.writer(arquivo)
    meu_arquivo.writerows(rows)
    arquivo.close()

    return rows
  finally:
    conn.close()

def insert_data(data):
  conn = sqlite3.connect(DB_NAME)
  cursor = conn.cursor()
  try:
    aluno = [data["cpf"], data["nome"], data["email"], data["matricula"]]
    cursor.execute("select * from disciplina where codigo = ?", [data["cod_disciplina"]])
    disciplina = cursor.fetchone()
    disciplina_id = None
    if disciplina:
      disciplina_id = disciplina["id"]
      aluno.append(disciplina["id"])
    else:
      cursor.execute(
        "INSERT into disciplina (codigo, nome) VALUES (?, ?)",
        [data["cod_disciplina"], data["disciplina"]]
      )
      disciplina_id = cursor.lastrowid
      aluno.append(disciplina_id)
    cursor.execute('''INSERT INTO alunos
      (cpf, nome, email, matricula, disciplina_id)
      VALUES(?, ?, ?, ?, ?)''', aluno)
    notas = [cursor.lastrowid, disciplina_id, data["nota1"], data["nota2"], data["nota3"]]
    cursor.execute(
      '''INSERT INTO notas
        (aluno_id, disciplina_id, nota1, nota2, nota3)
        VALUES(?, ?, ?, ?, ?)''', notas
    )

    conn.commit()
  finally:
    conn.close()

''' UPDATE '''
def update_data(old_data, new_data):
  aluno_id = old_data[9]
  disciplina_id = old_data[10]
  print(aluno_id, disciplina_id)
  conn = sqlite3.connect(DB_NAME)
  cursor = conn.cursor()
  try:
    cursor.execute('''
      UPDATE alunos SET
        matricula = ?,
        cpf = ?,
        nome = ?,
        email = ?
      WHERE id = ?
    ''',
    [
      new_data["matricula"],
      new_data["cpf"],
      new_data["nome"],
      new_data["email"],
      aluno_id
    ])

    cursor.execute('''
      UPDATE disciplina SET
        codigo = ?,
        nome = ?
      WHERE id = ?
    ''',
    [
      new_data["cod_disciplina"],
      new_data["disciplina"],
      disciplina_id
    ])

    cursor.execute('''
      UPDATE notas SET
        nota1 = ?,
        nota2 = ?,
        nota3 = ?
      WHERE aluno_id = ?
      AND disciplina_id = ?
    ''',
    [
      new_data["nota1"],
      new_data["nota2"],
      new_data["nota3"],
      aluno_id,
      disciplina_id
    ])

    conn.commit()
  finally:
    conn.close()

''' DELETE '''
def delete_data(matricula):
  conn = sqlite3.connect(DB_NAME)
  cursor = conn.cursor()
  try:
    cursor.execute("select id from alunos where matricula = ?", [matricula])
    id_aluno = cursor.fetchone()[0]
    cursor.execute("delete from notas where aluno_id = ?", [id_aluno])
    cursor.execute("delete from alunos where id = ?", [id_aluno])
    conn.commit()
  finally:
    conn.close()

def query_data_for_update(matricula):
  conn = sqlite3.connect(DB_NAME)
  cursor = conn.cursor()
  try:
    cursor.execute('''
      SELECT
        a.matricula,
        a.cpf,
        a.nome,
        a.email,
        d.codigo as cod_disciplina,
        d.nome as nome_disciplina,
        n.nota1,
        n.nota2,
        n.nota3,
        a.id as aluno_id,
        d.id as disciplina_id
      FROM
        alunos a
        INNER JOIN disciplina d ON (a.disciplina_id = d.id)
        INNER JOIN notas n ON (a.id = n.aluno_id AND a.disciplina_id = d.id)
      WHERE a.matricula = ?
    ''', [matricula])
    return cursor.fetchone()
  finally:
    conn.close()
