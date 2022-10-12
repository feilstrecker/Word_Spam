import pyautogui
from time import sleep
import os
from keyboard import is_pressed
word_list = []
word = ''
split_word = False
loop = False

question1 = input('Deseja separar as palavras a cada espaço? y/n: ')
question2 = input('Deseja repetir as palavras? y/n: ')

if question1 == 'y':
    split_word = True
if question2 == 'y':
    loop = True


while word != 'exit':
    os.system('cls')
    print("Digite 'exit' para iniciar o spam. ")
    word = input('frase/palavra: ')
    if word == 'exit':
        pass
    else:
        if split_word == True:
            word = word.split(' ')
            for element in word:
                word_list.append(element)
        else:
            word_list.append(word)

os.system('cls')
print('Iniciando em 10 segundos, certifique que você está no chat')
sleep(5)
if loop:
    print("Segure a tecla '-' para fechar.")
    while is_pressed('-') == False:
        for word in word_list:
            pyautogui.write(word)
            sleep(0.5)
            pyautogui.press('Enter')
            sleep(0.2)
else:
    for word in word_list:
        pyautogui.write(word)
        sleep(0.5)
        pyautogui.press('Enter')
        print('message sent ✓')
        sleep(0.2)


