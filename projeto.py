import funcoes as fu

usuarios = {}
eventos = []
bloqueados = []

op = -1 
while op != 0:
  print('1 - cadrastar usuario')
  print('2 - login')
  print('0 - sair')
  op_possivel = ['0', '1', '2']
  opcao = input("Escolha uma opção: ")
  if opcao in op_possivel:
    op = int(opcao)
    if op == 1:
      nome, email, senha, senha2 = fu.informacoes_usu()
      while not fu.verificar_user_existente(email, usuarios):
        print("Cadastro não realizado. Usuário já existente.")
        email = input('digite novamente seu email: ')
      while( not fu.verificar_senha(senha, senha2)):
        print("As senhas não coincidem. Tente novamente.")
        senha = input("Digite sua senha: ")
        senha2 = input("Repita sua senha: ")
      usuarios[email] = {'nome': nome, 'senha': senha}
      fu.adicionar_usuario_arquivo(email, senha, nome)
      print("Usuário cadastrado com sucesso!")
    elif op == 2:
      email = input('digite seu email: ')
      senha = input('digite sua senha: ')
      if not fu.login_arquivo(email, senha):
        print('email ou senha invalidos')
      else: 
        opcao_menu = -1
        while(opcao_menu != 0):
          print("\n|---| MENU DO USUÁRIO |---|")
          print("1 - Criar Evento")
          print("2 - Buscar Evento")
          print("3 - Listar Eventos")
          print("4 - Remover Evento")
          print("5 - Inscrever-se em Evento")
          print("6 - adicionar participante")
          print("7 - listar participantes")
          print("8 - gerar grafico")
          print("9 - valor arrecadado")
          print("0 - Sair")
          
          op_possivel2 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
          opcao2 = input('digite a opçao desejada: ')
          
          if opcao2 in op_possivel2:
            opcao_menu = int(opcao2)
            if(opcao_menu == 1):
              fu.criar_eventos(email, eventos)
            elif(opcao_menu == 2):
              fu.buscar_eventos(eventos)
            elif(opcao_menu == 3):
              fu.listar_eventos(eventos)
            elif(opcao_menu == 4):
              fu.remover_evento(email, eventos)
            elif(opcao_menu == 5):
              fu.inscrever_evento(email, eventos, bloqueados)
            elif opcao_menu == 6:
              fu.adicionar_participante_evento(email, eventos)
            elif opcao_menu == 7:
              fu.listar_participantes_evento(eventos)
            elif opcao_menu == 8:
              fu.gerar_grafico_participantes(eventos)
            elif opcao_menu == 9:
              fu.valor_arrecadado(email, eventos)
            elif opcao_menu == 0:
              break
            else:
              print("Opção inválida. Tente novamente.")
        
    elif op == 0:
      print("Saindo do sistema...")
      break
    else:
      print("Opção inválida. Tente novamente.")