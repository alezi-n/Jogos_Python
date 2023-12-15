import random

def imprimir_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def selecionar_palavra_secreta():
    with open('palavras.txt','r') as arquivo:
        conteudo = arquivo.read()
    lista_conteudo = conteudo.split()
    return random.choice(lista_conteudo).lower()

def verificar_chute(chute,palavra_secreta,letras_acertadas):
    if chute in palavra_secreta:
        idx = 0 
        for letra in palavra_secreta:
            if chute == letra:
                letras_acertadas[idx] = chute
            idx += 1
        return True
    else:
        return False

def validar_chute(chute,list_letra):
    if chute in list_letra or chute == '' or len(chute) == 2:
        print('Letra já usada, tente novamente!')
        return True

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def jogar():

    imprimir_abertura()

    palavra_secreta = selecionar_palavra_secreta()

    letras_acertadas = ['_' for i in palavra_secreta]

    enforcou = False
    acertou = False
    tentativas = 0

    list_letra = []

    rodadas = 1
    while not enforcou and not acertou:
        print(f'Rodada {rodadas}')

        if rodadas > 1:
            print(f'Lista de letras já digitadas:\n{list_letra}')

        print(f'Palavra Secreta:\n{letras_acertadas}')

        chute = input('Digite uma Letra: ').lower().strip()

        if validar_chute(chute,list_letra):
            continue

        list_letra.append(chute)

        if not verificar_chute(chute,palavra_secreta,letras_acertadas):
            tentativas += 1
            desenha_forca(tentativas)

        rodadas += 1

        acertou = '_' not in letras_acertadas
        enforcou = tentativas == 7

        if acertou :
            print('Você Ganhou!')
        if enforcou:
            print('Você Perdeu!')

    print('Fim de Jogo')

if __name__ == '__main__':
    jogar()