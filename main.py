from magica import *
import os
import time

print("Bem-vindo ao programa de listas! Você pode criar listas de mercado, afazeres, ideias e muito mais. \n"
      "Sua lista será salva automaticamente no bloco de notas. Por favor, aguarde enquanto o BOT salva sua lista.\n"
      'Espere 5 segundos')

time.sleep(5)

iniciar = input('Começar? (S/N) ')
os.system('cls')

iniciar_formatado = iniciar.lower()
gatilho = None

if iniciar_formatado == 's':
    gatilho = True
    comecar(gatilho)
elif iniciar_formatado == 'n':
    print('Programa encerrado')
    gatilho = False
else:
    print('Opção inválida')
    #print()