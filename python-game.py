import random

sorteado = random.randint(1,6)
comodos = ["sala", "cozinha", "quarto", "banheiro", "jardim", "garagem"]

tentativas = 0
while True:
    tentativa = int(input("Tente adivinhar o comodo sorteado (1-6):"))
    if tentativa < 1 or tentativa > 6:
        print("Numero invalido! Tente novamente.")
        continue
    if tentativa == sorteado:
        print(f"Parabens! Voce acertou o comodo sorteado! Estava no(a) {comodos[sorteado - 1]}")
        break
    else:
        print(f"Errado! Nao esta no(a) {comodos[sorteado - 1]}")