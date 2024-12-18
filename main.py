from magica import *
import os


print("Bem-vindo ao programa de listas! Você pode criar listas de mercado, afazeres, ideias e muito mais. \n"
      "Sua lista sera salvaa automaticamente no bloco de notas. Por favor, aguarde enquanto o BOT salva sua lista.\n"
      'Espere 5 segundos')
time.sleep(8)

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

