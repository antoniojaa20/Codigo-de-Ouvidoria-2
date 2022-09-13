import ElogioArquivo
import ReclamacaoArquivo
claims = ReclamacaoArquivo.Reclamacao()
compliments = ElogioArquivo.Elogio()
isTrue = True

while isTrue:
  
  print('-' * 70)
  print('{}Seja bem vindo à ouvidoria da Celgon{}'.format('\033[1;34m', '\033[m'))
  print('-' * 70)
  print('Menu do Sistema \n')
  print('Opcões: \n')
  print('Digite 1 para acessar seu cadastro')
  print('Digite 2 para cadastrar uma ocorrencia')
  print('Digite 3 para ver as listas de ocorrencia')
  print('Digite 4 para excluir algum item das listas')
  print('Digite 5 para apagar uma das listas')
  print('Digite 6 para ser encaminhado à um atendente')
  print('Digite 7 para sair \n')
  opcao = int(input('{}Digite a sua opção: {}'.format('\033[1;34m', '\033[m')))


  if opcao == 1:
    e = input('{}Digite o seu email: {}'.format('\033[1;34m', '\033[m'))
    s = input('{}Digite a sua senha: {}'.format('\033[1;34m', '\033[m'))
    n = input('{}Digite seu nome: {}'.format('\033[1;34m', '\033[m'))
    print('{}Olá, seja bem vindo {}{}'.format('\033[1;34m', '\033[m', n.title()))


  elif opcao == 2:
    print('{}Qual ocorrencia deseja criar:{} \n'.format('\033[1;34m', '\033[m'))
    print('Digite 1 para Elogio')
    print('Digite 2 para Reclamação \n')
    ocorrencia = int(input('{}Digite sua opção: {}'.format('\033[1;34m', '\033[m')))
    
    if ocorrencia == 1:
      valor = input('{}Digite seu Elogio: {}'.format('\033[1;34m', '\033[m'))
      compliments.adicionar(valor)
      
    elif ocorrencia == 2:
      valor = input('{}Digite a sua Reclamação: {}'.format('\033[1;34m', '\033[m'))
      claims.adicionar(valor)
      
  


  elif opcao == 3:
    print('{}Qual lista você deseja visualizar:{}\n'.format('\033[1;34m', '\033[m'))
    print('Digite 1 para lista de Elogios')
    print('Digite 2 para lista de Reclamções\n')
    opcaoLista = int(input('{}Digite sua opção: {}'.format('\033[1;34m', '\033[m')))
  
    if opcaoLista == 1:
      compliments.mostrarListaElogio()
      
    elif opcaoLista == 2:
      claims.mostrarListaReclamacao()
      


  elif opcao == 4:
    print('{}Escolha uma lista:{}\n'.format('\033[1;34m', '\033[m'))
    print('Digite 1 para elogio')
    print('Digite 2 para Reclamação\n')
    opcaoListaExcluir = int(input('{}Digite qual a lista desejada: {}'.format('\033[1;34m', '\033[m')))
    
    if opcaoListaExcluir == 1:
      itemExcluido = int(input('{}Digite qual valor da lista você deseja apagar: {}'.format('\033[1;34m', '\033[m')))
      compliments.excluirItemListaElogio(itemExcluido)
      print('{}O item selecionado foi apagado.{}'.format('\033[1;34m', '\033[m'))
    
    elif opcaoListaExcluir == 2:
      itemExcluido = int(input('{}Digite qual valor da lista você deseja apagar: {}'.format('\033[1;34m', '\033[m')))
      claims.excluirItemListaReclamacao(itemExcluido)
      print('{}O item selecionado foi apagado.{}'.format('\033[1;34m', '\033[m'))
    


  elif opcao == 5:
    print('{}Qual lista você deseja apagar?{}\n'.format('\033[1;34m', '\033[m'))
    print('Digite 1 para Elogio')
    print('Digite 2 para reclamação\n')
    opcaoApagarLista = int(input('{}Digite a sua opção: {}'.format('\033[1;34m', '\033[m')))

    if opcaoApagarLista == 1:
      compliments.apagarListaElogio()
      print('{}Sua lista de Elogio foi apagada.{}'.format('\033[1;34m', '\033[m'))
    
    elif opcaoApagarLista == 2:
      claims.apagarListaReclamacao()
      print('{}Sua lista de Reclamações foi apagada.{}'.format('\033[1;34m', '\033[m'))
    

  elif opcao == 6:
    print('{}Você será redirecionado para um atendente, por favor aguarde...{}'.format('\033[1;34m', '\033[m'))
    print('{}Olá meu nome é Sérgio, em que posso ajudar?{}'.format('\033[1;34m', '\033[m'))
  
  elif opcao == 7:
    isTrue = False
  

print('{}Por favor, avalie o nosso atendimento com uma nota de 0 a 10.{}'.format('\033[1;34m', '\033[m'))
nota = input('Qual a sua nota para o nosso atendimento: ')
print('{}Obrigado pela sua atenção, a Celgon agradece!{}'.format('\033[1;34m', '\033[m'))
print('-' * 70)