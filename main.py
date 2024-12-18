from magica import *
import os

iniciar = input('começar? (S/N) ')
os.system('cls')

iniciar_fomatado = iniciar.lower()
gatilho = None

if iniciar_fomatado == 's':
  gatilho = True
  comecar(gatilho)

elif iniciar_fomatado == 'n':
  print('Programa encerrado')
  gatilho = False

else:
  print('Opção inválida')

