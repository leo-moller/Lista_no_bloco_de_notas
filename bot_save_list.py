import time
import pyautogui

def pega_lista(lista, nome_lista):
    time.sleep(5.0)
    
    pyautogui.press("win")
    pyautogui.write("Bloco de Notas")
    time.sleep(1)
    
    pyautogui.press("enter")
    time.sleep(0.5)

    for index, item in enumerate(lista, start=1):
        pyautogui.write(f'{index} - {item}')
        pyautogui.press('enter')
    
    time.sleep(2)

    pyautogui.hotkey("ctrl", "shift", "s")
    time.sleep(2.0)

    pyautogui.write(nome_lista + ".txt", interval=0.1)
    time.sleep(7)

    pyautogui.press("enter")
    time.sleep(2.0)

    pyautogui.hotkey("alt", "f4")
    print()
    print(f"lista salva com nome de: {nome_lista}")

    #print()

