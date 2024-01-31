import random
##o objetivo deste jogo e adivinhar as cores sorteadas o usuario tem tentativas limites

CORES = ["R", "G", "B", "Y", "W", "O"]
tries = 10
TAMANHO_CODIGO = 4


def gerar_codigo():
    code = []

    for _ in range(TAMANHO_CODIGO):
        cor = random.choice(CORES)
        code.append(cor)
    return code


def adivinhar():
    while True:
        chute = input("adivinhe: ").upper().split(" ")

        if len(chute) != TAMANHO_CODIGO:
            print(
                F"voce digitou uma quantidade: {TAMANHO_CODIGO} invalida! digite 4 CORES")
            continue

        for color in chute:
            if color not in CORES:
                print(f"cor INVALIDA: {color} tente de novo!")
                break
        else:
            break
    return chute


def checar_cor(chute,cor_certa):
    cor_quantidade = {}
    poss_correta = 0
    poss_incorreta = 0

    for color in cor_certa:
        if color not in cor_quantidade:
            cor_quantidade[color] = 0
        cor_quantidade[color] += 1


    for cor_chute,cor_real in zip(chute,cor_certa):
        if cor_chute == cor_real:
            poss_correta += 1
            cor_quantidade[cor_chute] -= 1

    for cor_chute,cor_real in zip(chute,cor_certa):
        if cor_chute in cor_real and cor_quantidade[cor_chute] > 0:
            poss_incorreta += 1
            cor_quantidade[cor_chute] -= 1
    return poss_correta,poss_incorreta


                
          
def game():
    print(f"bem vindo ao jogo humano! voce tem {tries} tentativas para acertar as cores!")
    code = gerar_codigo()
    for tentativas in range(1, tries + 1):
        chute = adivinhar()
        poss_correta,poss_incorreta = checar_cor(chute,code)
        if poss_correta == TAMANHO_CODIGO:
            print(f"voce acertou com: {tentativas} tentativas!")
        print(f"posicoes corretas: {poss_correta}|| posicoes incorretas: {poss_incorreta}")
    else:
        print(f"voce passou da tentativas!", * code)    





if __name__ == "__main__":
    game()