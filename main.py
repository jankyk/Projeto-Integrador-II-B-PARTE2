#importando os módulos
import os
import time
import csv
import random

#abrindo o arquivo de perguntas e respostas
arquiv = open("PerguntasERespostas.csv","r")
#leitura das linhas no CSV
linha = arquiv.readline()
#função e parametro de leitura
loader = csv.reader(arquiv, delimiter=";")
#importação e criação da lista de perguntas
quests = []
for linha in loader:
  quests.append(linha)
#fechando o arquivo de perguntas e respostas
arquiv.close()

menu = 4
while menu != 0:
  print("MENU DE PERGUNTAS E RESPOSTAS\n")
  print("Selecione a opção desejada:\n")
  print("0 - Sair do Jogo.\n")
  print("1 - Gerar Rodada de Perguntas.\n")
  print("2 - Ver Pontuação Total.\n")
  print("3 - Ver Maior Pontuação em uma rodada até o momento .\n")
  menu = int(input('Informe um opção: '))
  pontos = 0
  maiorpontorodada = 0
  listapontorodada = []
  qntrespostacerta = 0

  if menu == 1: #GERAÇÃO DE RODADA DE PERGUNTAS
    perguntaLista = []
    for i in range (2):
      pergunta = (random.choice(quests))
      perguntaLista.append(pergunta)

    for x in range (2):
      print("\nQuestão: ",perguntaLista[x][0])#pergunta
      print("\nAlterantiva 1: ",perguntaLista[x][1])#resposta 1
      print("\nAlterantiva 2: ",perguntaLista[x][2])#resposta 2
      print("\nAlterantiva 3 ",perguntaLista[x][3])#resposta 3
      rcerta = int(perguntaLista[x][4])#resposta correta
      print (rcerta)
      rusuario = int(input('\n' + 'Qual será a resposta correta? '))
      print(type(rusuario))
      if (rusuario >= 1 and rusuario <= 3):
        if (rusuario == rcerta):
          pontos += 20
          qntrespostacerta += 1
          os.system('clear') or None
          print ('\n' + 'Parabéns '  +', você acertou e está com  pontos')
          time.sleep(1) #função de espera
        else:
          os.system('clear') or None
          print ('\n' + 'Resporta incorreta, ' + '\nA resposta correta é: ', rcerta)
          time.sleep(1) #função de espera
    # usuário digitou opção inválida - Vai inforamr o erro, e solicitar a pergunta novamente
      else:
        while (rusuario <1) or (rusuario >3):
          os.system('clear') or None
          print ('Informação inválida, Você digitou: ' + str(rusuario) + ' favor informar uma opção válida') 
          print("\nQuestão: ",perguntaLista[x][0])#pergunta
          print("\nAlterantiva 1: ",perguntaLista[x][1])#resposta 1
          print("\nAlterantiva 2: ",perguntaLista[x][2])#resposta 2
          print("\nAlterantiva 3 ",perguntaLista[x][3])#resposta 3
          print ('\n')
          print ('Para opção 1 digite o numeral 1, para opção 2 digite o numeral 2 e para opção 3 digite o numeral 3 ')
          rusuario = int(input('Informe a alternativa correta? '))
      time.sleep(1) #função de espera
      os.system('clear') or None #esse comando limpa a tela do console
    print ('Resultado final:')
    print ('Jogador, você fez', + pontos, 'pontos! O total de acertos é =',qntrespostacerta)
    listapontorodada.append(pontos)
    if (pontos > maiorpontorodada):
      maiorpontorodada = pontos

  
  elif menu == 2: #Geração de pontuação total
    print ("")
    
  elif menu == 3: #Geração de maior pontuação
   print ("Sua maior pontuação em uma rodada :" , maiorpontorodada,"\n")
   print ("Lista da rodada :" , listapontorodada,"\n")