INCLUIR_DADO = 1
ALTERAR_DADO = 2
EXCLUIR_DADO = 3
CONSULTAR_SITUACAO = 4
CONSULTAR_DISCIPLINA = 5
CONSULTAR_ALUNO = 6
SAIR = 7

def main_menu():
  print("--------------")
  print("Menu principal")
  print("--------------")
  print("1. Incluir dado")
  print("2. Alterar dado")
  print("3. Excluir dado")
  print("4. Consultar situacao dos alunos")
  print("5. Consultar disciplinas")
  print("6. Consultar alunos")
  print("7. Sair")

  return int(input("Selecione uma opção: "))

def read_data():
  print("------------------")
  print("Novo registro")
  print("------------------")
  matricula = input("Matricula: ").strip()
  if(matricula == ""):
    print("A matricula deve ser informada.")
    return
  cpf = input("CPF: ").strip()
  if(cpf == ""):
    print("O CPF deve ser informado.")
    return
  nome = input("Nome: ").strip()
  email = input("Email: ").strip()
  disciplina = input("Disciplina: ").strip()
  cod_disciplina = input("Cod. Displina: ").strip()
  nota1 =  input("Nota1: ").strip()
  nota2 = input("Nota2: ").strip()
  nota3 = input("Nota3: ").strip()
  return {
    "matricula": matricula,
    "cpf": cpf,
    "nome": nome,
    "email": email,
    "disciplina": disciplina,
    "cod_disciplina": cod_disciplina,
    "nota1": nota1,
    "nota2": nota2,
    "nota3": nota3
  }
def get_new_data(previus_data):
  print("------------------")
  print("Altere o registro")
  print("------------------")
  matricula = input("Matricula [{}]: ".format(previus_data[0]))
  cpf = input("CPF [{}]: ".format(previus_data[1]))
  nome = input("Nome [{}]: ".format(previus_data[2]))
  email = input("Email [{}]: ".format(previus_data[3]))
  disciplina = input("Disciplina [{}]: ".format(previus_data[4]))
  cod_disciplina = input("Cod. Displina [{}]: ".format(previus_data[5]))
  nota1 =  input("Nota1 [{}]: ".format(previus_data[6]))
  nota2 = input("Nota2 [{}]: ".format(previus_data[7]))
  nota3 = input("Nota3 [{}]: ".format(previus_data[8]))
  return {
    "matricula": matricula or previus_data[0],
    "cpf": cpf or previus_data[1],
    "nome": nome or previus_data[2],
    "email": email or previus_data[3],
    "disciplina": disciplina or previus_data[4],
    "cod_disciplina": cod_disciplina or previus_data[5],
    "nota1": nota1 or previus_data[6],
    "nota2": nota2 or previus_data[7],
    "nota3": nota3 or previus_data[8]
  }

def get_matricula_aluno():
  return input("Matricula do aluno: ")

def print_alunos(alunos):
  print("-------------------------------------------------------------------------------------------")
  print("ALUNOS ")
  print("-------------------------------------------------------------------------------------------")
  ALUNOS_FORMAT_PATTERN = "{:<15} {:>10} {:<20} {:<20} {:<6} {:<15}"
  print(ALUNOS_FORMAT_PATTERN.format("CPF", "Matricula", "Nome", "E-mail", "C.Disc", "Disciplina"))
  print("-------------------------------------------------------------------------------------------")
  for aluno in alunos:
    print(ALUNOS_FORMAT_PATTERN.format(aluno[0], aluno[1], aluno[2], aluno[3], aluno[4], aluno[5]))

def print_disciplinas(disciplinas):
  DISCIPLINAS_PATTERN = "{:>10} {:<40}"
  print("--------------------------------------------------")
  print("DISCIPLINAS")
  print("--------------------------------------------------")
  print(DISCIPLINAS_PATTERN.format("Codigo", "Nome"))
  print("--------------------------------------------------")
  for disciplina in disciplinas:
    print(DISCIPLINAS_PATTERN.format(disciplina[0], disciplina[1]))

def print_situacao_aluno(situacoes):
  SITUACAO_PATTERN = "{:>10} {:<30} {:>5} {:>5} {:>5} {:<10}"
  print("-----------------------------------------------------------------")
  print("SITUACAO DO ALUNO")
  print("-----------------------------------------------------------------")
  print(SITUACAO_PATTERN.format("Matricula", "Nome", "Nota1", "Nota2", "Nota3", "Resultado"))
  print("-----------------------------------------------------------------")
  for situacao in situacoes:
    print(SITUACAO_PATTERN.format(situacao[0], situacao[1], situacao[2], situacao[3], situacao[4], situacao[5]))
