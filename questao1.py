from db import * 
from screen import *
import traceback

try:
  init_db()
  feed_db()
  
  op = 0
  while op != SAIR:
    op = main_menu()
    if(op == INCLUIR_DADO):
      insert_data(read_data())
    elif(op == CONSULTAR_ALUNO):
      print_alunos(query_alunos())
    elif(op == CONSULTAR_DISCIPLINA):
      print_disciplinas(query_disciplinas())
    elif(op == CONSULTAR_SITUACAO):
      print_situacao_aluno(query_situacao_aluno())
    elif(op == EXCLUIR_DADO):
      delete_data(get_matricula_aluno())
    elif(op == ALTERAR_DADO):
      old_data = query_data_for_update(get_matricula_aluno())
      update_data(old_data, get_new_data(old_data))
  print("Fim do programa")
except Exception as error:
  print('Erro geral: ', error)
  traceback.print_exc()

