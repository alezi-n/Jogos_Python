import forca
import adivinhar

print("*********************************")
print("********Seleção de Jogos!********")
print("*********************************")

print('(1) Forca (2) Adivinhação')

jogo = int(input('Qual o Jogo? '))

if jogo == 1:
    print('Jogando Forca!')
    forca.jogar()
elif jogo == 2:
    print('Jogando Adivinhação!')
    adivinhar.jogar()