from bot_save_list import *
import os

def criar_lista():
  return []

def inserir_item(lista, elemento):
    os.system('cls')
    lista.append(elemento)
    os.system('cls')
    return lista

def sair(lista):
  if not lista:
    os.system('cls')
    print("sua lista está vazia")
    print()

  else:
    print('Sua lista ficou assim: ')
    print()
    for indice,item in enumerate(lista):
      print(indice,'-', item)

def apagar(lista,indice_apagar):
  for indice,item in enumerate(lista):
       print(indice,item)

  try:
    del lista[indice_apagar]
    os.system('cls')

  except IndexError:
    os.system('cls')
    print('Esse indice não existe')
    print()

  except:
    print('Erro desconhecido')
    print()

def listar(lista):
  if not lista:
    os.system('cls')
    print('A lista está vazia')
    print()
    
  else:
      os.system('cls')

      for indice,item in enumerate(lista):
        # os.system('cls')
        print('-'*5)
        print(indice, '-', item)

def salvar_lista(lista, nome_lista):
  print()
  print("O bot irá salvar sua lista. Aguarde 5 segundos e, por favor, não mexa em nada. O programa se encerrará automaticamente.")
  print()
  pega_lista(lista, nome_lista)
  sair(lista)

def comecar(gatilho):
  lista = criar_lista()



  # inserir um entrada_formatada para usar o lower()
  while gatilho:
    
    entrada = input('Selecione uma opção \n'
                    '[i]nserir [s]air [a]pagar [l]istar [g]uardar: '
                   )
    entrada_formatada = entrada.lower()
    print()

    if entrada_formatada == 'i':
      elemento = input('O que você deseja inserir na lista? ')
      
      inserir_item(lista,elemento)

    elif entrada_formatada == 's':
      sair(lista)
      gatilho = False

    elif entrada_formatada == 'a':
      
        
          
        try:
          indice_apagar = int(input('Qual indice deseja apagar? ' ))
          apagar(lista, indice_apagar)
          
          
        except ValueError:
          os.system('cls') 
          print('Insira um número')

    elif entrada_formatada == 'l':
      listar(lista)

    elif entrada_formatada == 'g':
      print()
      nome_lista = input('com qual nome deseja salvar essa lista? ')
      salvar_lista(lista,nome_lista)
      gatilho = False
