from InquirerPy import prompt
import os
from bot_save_list import pega_lista
import time

def criar_lista():
    return []

def inserir_item(lista, item):
    lista.append(item)
    print(f'Item "{item}" inserido na lista.')

def apagar(lista, indice):
    try:
        item = lista.pop(indice)
        print(f'Item "{item}" removido da lista.')
    except IndexError:
        print('Índice inválido.')

def listar(lista):
    if lista:
        for i, item in enumerate(lista):
            print(f'{i} - {item}')
    else:
        print('A lista está vazia.')

def salvar_lista(lista, nome_lista):
    print()
    print("O bot irá salvar sua lista. Aguarde 5 segundos e, por favor, não mexa em nada. O programa se encerrará automaticamente.")
    print()
    pega_lista(lista, nome_lista)

def comecar(gatilho):
    lista = criar_lista()

    while gatilho:
        
        time.sleep(2)
        print("Use as setinhas para navegar e o Enter para selecionar.")
        perguntas = [
            {
                "type": "list",
                "message": "Escolha uma opção",
                "choices": [
                    "Inserir",
                    "Sair",
                    "Apagar",
                    "Listar",
                    "Guardar"
                ],
                "name": "choices"
            }
        ]
        entrada = prompt(perguntas)

        if entrada["choices"] == 'Inserir':
            elemento = input('O que você deseja inserir na lista? ')
            inserir_item(lista, elemento)
            os.system('cls')

        elif entrada["choices"] == 'Sair':
            gatilho = False
            os.system('cls')

        elif entrada["choices"] == 'Apagar':
            try:
                indice_apagar = int(input('Qual índice deseja apagar? '))
                apagar(lista, indice_apagar)
            except ValueError:
                print('Insira um número')
            os.system('cls')

        elif entrada["choices"] == 'Listar':
            listar(lista)
            input("Pressione Enter para continuar...")
            os.system('cls')

        elif entrada["choices"] == 'Guardar':
            nome_lista = input('Com qual nome deseja salvar essa lista? ')
            salvar_lista(lista, nome_lista)
            gatilho = False
            os.system('cls')
    #print()
