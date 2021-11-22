#importando os módulos
import csv
import random

#abrindo o arquivo de perguntas e respostas
lista = open("PerguntasERespostas(utf8).csv","r")

linha = lista.readline()
print(linha)

#fechando o arquivo de perguntas e respostas
lista.close()