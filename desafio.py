operacoes = '''
[d] depositar
[s] sacar
[e] extrato
[q] sair '''

saldo = 0 
limite = 500 # o limite de cada saque é no máximo 500,00
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3 # uma constante: deve realizar apenas 3 saques diários

while True:
  mensagem = input(operacoes) # escolhe uma operação
  
  if mensagem == 'd':
    valor = float(input('informe o valor do depósito: '))
    if valor > 0: # evita valores negativos
      saldo += valor # vai adicionar o valor à váriavel saldo
      extrato += f'valor do depósito R${valor:.2f}\n' # vai adicionar uma linha do extrato 
    else:
      print('o valor informado é inválido, tente novamente.') # caso a pessoa informe um valor menor que 0
      
  elif mensagem == 's':
    valor = float(input('informe o valor do saque: '))               
    excedeu_saldo = valor > saldo
    excedeu_limite_saldo = valor > limite
    excedeu_limite_saques = numero_saques >= LIMITE_SAQUES
    if excedeu_saldo:
      print('você não tem saldo suficiente, tente novamente.')
    elif excedeu_limite_saldo:
      print('você excedeu o limite de cada saque, tente um valor menor que 500 reais.')
    elif excedeu_limite_saques:
      print('você excedeu o limite diário de 3 saques, tente outro dia.')      
    elif valor > 0:
      saldo -= valor # subtrai o valor no saldo com o novo valor inserido 
      extrato += f'valor do saque R${valor:.2f}\n'
      numero_saques += 1 # aumenta o número de saques realizado no dia
    else:
      print('o valor informado é inválido, tente novamente.')

  elif mensagem == 'e':
    print('\n---------------EXTRATO---------------')
    print('não foram realizadas movimentações.' if not extrato else extrato) # caso não há nenhum extrato no histórico
    print(f'\nO saldo da conta é: R${saldo:.2f}')
    print('------------------------------------')

  elif mensagem == 'q':
    break # quebra o loop caso a pessoa deseje terminar a sua operação

  else:
    print('operação inválida, insira novamente a operação desejada.')