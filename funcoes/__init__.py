
import matplotlib.pyplot as plt
import pandas as pd
def verificar_senha(senha, senha2):
  if(senha == senha2):
    return True
  else:
    return False
  
def verificar_email(email):
    return '@' in email and '.com' in email
  
def verificar_user_existente(email, usuarios):
  if not verificar_email(email):
    print("E-mail inválido!")
    return False  
  if email in usuarios:
    print("Usuário já existente!")
    return False 
  return True  

def adicionar_usuario_arquivo(email, senha, nome):
  with open('usuarios.txt', 'a') as arquivo:
    arquivo.write(f"{email},{senha},{nome}\n")
  
def informacoes_usu():
  print('|---|''Cadastro''|---|')
  nome = input('Digite seu nome: ')
  email = input('digite seu e-mail: ')
  senha = input('digite sua senha: ')
  senha2 = input('Repita sua senha: ')
  
  return nome, email, senha, senha2, 
    
def verificar_idade(idade, usuarios, email):  
  if idade < 13:
    print('você está abaixo da idade permitida')
  else:
    print(f"{usuarios[email]['nome']} você está na idade permitida")
  return idade
  
def login_arquivo(email, senha):
  with open('usuarios.txt', 'r') as arquivo:
    for linha in arquivo:
      dados = linha.strip().split(',')
      if dados[0] == email and dados[1] == senha:
        return True
    return False

def ler_email_organizador(email):
  arquivo = open('usuarios.txt','r')
  linhas = arquivo.readlines()
  for linha in linhas:
    dados = linha.split(',')
    if dados[0] == email:
      print(email)
      return dados[2]
  arquivo.close()

def adicionar_participantes(email):
  arquivo = open('participantes.txt','a')
  arquivo.write(f'{email}\n')
  arquivo.close()

def criar_eventos(email, eventos):
    nome_organizador = ler_email_organizador(email)
    titulo = input("Digite o título do evento: ")
    descricao = input("Digite a descrição do evento: ")
    data = input("Digite a data do evento (DD/MM/AAAA): ")
    local = input("Digite o local do evento: ")
    valor = float(input("Digite o valor de inscrição: "))
    evento = {
      'organizador':email,
      'nome_organizador': nome_organizador,
      'titulo': titulo,
      'descricao': descricao,
      'data': data,
      'local': local,
      'valor': valor,
      'participantes': []  
    }
    eventos.append(evento)
    print('Evento cadastrado com sucesso!')
    
def buscar_eventos(eventos):
  nome = input("digite o nome do evento: ")
  evento_encontrado = False
  for evento in eventos:
    if nome == evento["titulo"]:
      evento_encontrado = True
      print(f"{evento["titulo"]}, {evento["data"]}, {evento["local"]}, {evento["valor"]}")
      break
  else:
      print("evento não encontrado")
  return evento_encontrado

def listar_eventos(eventos):
  if not eventos:
    print("Nenhum evento cadastrado.")
  else:
    for evento in eventos:
      print(f"- {evento['titulo']} (Organizador: {evento['nome_organizador']})")
    
def remover_evento(email, eventos):
  nome_evento = input('Digite o nome do evento a ser removido: ')
  evento_encontrado = None
  for evento in eventos:
    if evento['titulo'] == nome_evento and evento['organizador'] == email:
      evento_encontrado = evento
      break
  if evento_encontrado:
      confirmacao = input("Tem certeza que deseja remover o evento? (s/n): ").lower()
      if confirmacao == 's':
        eventos.remove(evento)
        print("Evento removido com sucesso.")
      else:
        print("Remoção cancelada.")
  else:
    print("Evento não encontrado ou você não tem permissão para removê-lo.")
  
def inscrever_evento(email, eventos, bloqueados, usuarios):
  nome_evento = input('Digite o nome do evento para se inscrever: ')
  for evento in eventos:
    if evento['titulo'] == nome_evento:
      idade = int(input("Digite sua idade: "))
      if idade < 13:
        bloqueados.append(email)
        verificar_idade(idade, usuarios, email)
      else:
        if email not in evento['participantes']:
          evento['participantes'].append(email)
          print("Inscrição realizada com sucesso!")
        else:
          print("Você já está inscrito neste evento!")
          break
    else:
      print("Evento não encontrado.")
  
  
def adicionar_participante_evento(email, eventos):
  nome_evento = input("Digite o nome do evento para adicionar participantes: ")
  evento_encontrado = None

  for evento in eventos:
    if evento['titulo'] == nome_evento and evento['organizador'] == email:
      evento_encontrado = evento
      break

  if evento_encontrado:
    email_participante = input("Digite o email do participante: ")
    if email_participante not in evento_encontrado['participantes']:
      evento_encontrado['participantes'].append(email_participante)
      print(f"Participante {email_participante} adicionado com sucesso ao evento '{nome_evento}'!")
    else:
      print("Esse participante já está inscrito no evento.")
  else:
    print("Evento não encontrado ou você não   tem permissão para adicionar participantes.")

def listar_participantes_evento(eventos):
  nome_evento = input("Digite o nome do evento: ")
  evento_encontrado = None

  for evento in eventos:
    if evento['titulo'] == nome_evento:
      evento_encontrado = evento
      break

  if evento_encontrado:
    print("Participantes do evento:")
    with open(f"{nome_evento}_participantes.txt", "w") as arquivo:
      for participante in evento_encontrado['participantes']:
        print(participante)
        arquivo.write(participante + "\n")
        print(f"Lista salva no arquivo '{nome_evento}_participantes.txt'.")
  else:
    print("Evento não encontrado.")


def gerar_grafico_participantes(eventos):
  titulos = [evento['titulo'] for evento in eventos]
  quantidades = [len(evento['participantes']) for evento in eventos]

  if not titulos:
    print("Não há eventos cadastrados.")

  plt.bar(titulos, quantidades, color='blue')
  plt.xlabel("Eventos")
  plt.ylabel("Número de Participantes")
  plt.title("Quantidade de Participantes por Evento")
  plt.xticks(rotation=45, ha='right')
  plt.tight_layout()
  plt.show() 
  
def valor_arrecadado(email, eventos):
  nome_evento = input('Digite o nome do evento: ')
  for evento in eventos:
    if evento['titulo'] == nome_evento and evento['organizador'] == email:
      numero_participantes = len(evento['participantes'])
      valor_total = numero_participantes * evento['valor']
      print(f"O número de inscritos é: {numero_participantes}")
      print(f"O valor total arrecadado é: R${valor_total:.2f}")

      dados = []
      for participante in evento['participantes']:
        dados.append({'Participante': participante,
                    'Valor Pago': evento['valor']
                    })
        df = pd.DataFrame(dados)
        df['Valor Total'] = df['Valor Pago'] * numero_participantes  
        nome_arquivo = f"{nome_evento}_participantes.xlsx"
        df.to_excel(nome_arquivo, index=False, engine='openpyxl')
        print(f"Arquivo Excel gerado com sucesso: {nome_arquivo}")
        break 

    else:
      print("Evento não encontrado ou você não é o organizador deste evento.")