import sqlite3

with sqlite3.connect("escola.db") as conexaoe:
    cursor = conexaoe.cursor()
    
    # 1. Ativando o suporte a chaves estrangeiras
    cursor.execute("PRAGMA foreign_keys = ON")

    # 2. Tentamos atualizar a carteirinha do aluno_id = 2 (Ana)
    #cursor.execute("""
   # UPDATE carteirinhas
    #SET codigo_de_acesso = 'eojajajajaja'
    #WHERE aluno_id = 2
   # """)
    
   # if cursor.rowcount == 0:
    #    print("A Ana (ID 2) não tinha nenhuma carteirinha registrada. Criando uma nova agora...")
        
        # 3. Se não alterou nada, inserimos a carteirinha dela pela primeira vez
        #cursor.execute("""
        #INSERT INTO carteirinhas (codigo_de_acesso, aluno_id)
        #VALUES ('eojajajajaja', 2)
       ## print("Carteirinha da Ana INSERIDA com sucesso!")
    ##print(f"Carteirinha da Ana ATUALIZADA com sucesso! Linhas modificadas: {cursor.rowcount}")

    # Forçando o salvamento manual por garantia absoluta
  #  conexaoe.commit()

    # 4. para listar tudo que esta na carteirinha
  ## cursor.execute("SELECT * FROM carteirinhas")
   # linhas = cursor.fetchall()
    
   # if not linhas:
     #   print("A tabela carteirinhas está completamente vazia!")
   # else:
      #  for linha in linhas:
            #print(f"ID Carteirinha: {linha[0]} | Código: {linha[1]} | ID Aluno: {linha[2]}")

            #--para mostrar a lista de alunos salvos
    #print("---Lista de alunos no banco ---")
    #cursor.execute("SELECT id, nome FROM alunos")
    ##   print(f"ID: {id_aluno} | Nome: {nome_aluno}")
    #print("\n-------------------------------------------\n")

    #print("--- CARTEIRINHAS NO BANCO---")
    #cursor.execute("SELECT * FROM carteirinhas")
    #for para desempacotar e pegar o primeiro valor numero e joga na variavel id_aluno e pega o segundo valor e joga na variavel nome_aluno
    #for linha in cursor.fetchall():
        #print(f"ID Carteirinha: {linha[0]} | Código: {linha[1]} | ID Aluno: {linha[2]}")

    #para atualizar o id do aluno cursor.execute("""
                   #UPDATE  alunos
                   #SET id = 2
                   #WHERE nome = 'Ana'
                   #""")
    
    #Para obtter um join com nome do aluno e o cdcodigo de acesso da carteirinha e unir eles
    #print("--- Nomes dos alunos e seus códigos de acesso ---")
    #cursor.execute("""SELECT alunos.nome,carteirinhas.codigo_de_acesso
                   #FROM alunos
                   #JOIN carteirinhas ON alunos.id = carteirinhas.aluno_id
                  # """)
   # for linha in cursor.fetchall():
        #print(f"Nome: {linha[0]} | Código de Acesso: {linha[1]}")


    #relacao de um para muitos entre professores e disciplinas,pois cada diciplina tem um professor, pois um professor pode ter varias disciplinas
    #e uma disciplina tem um professor
 #cursor.execute("""
    #INSERT INTO disciplinas (nome, professor_id) VALUES
    #('matematica',3),
    #('Logica de progamacao',4),
    #('ARQUITETURA DE COMPUTADORES',1),
    #('Artes',2),
    #('ciencas',3)            
#""")
 #print("esta inserido com sucesso")

    #cursor.execute("""SELECT professores.nome, disciplinas.nome
                    #  FROM professores
                     # JOIN disciplinas ON professores.id = disciplinas.professor_id
                 #  """)
                
   # for linha in cursor.fetchall():
       # print(f"Professor: {linha[0]} | Disciplina: {linha[1]}")

       #relacao de muitos para muitos:
    cursor.execute("""

                   """)