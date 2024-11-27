import random

def escolher_palavra():
    palavras = ["melancia", "acerola", "computador", "tamarindo", "esperanca", "flamengo", "humanidade" ]
    return random.choice(palavras)

def mostrar_palavra_oculta(palavra, letras_reveladas):
    resultado = ""
    for letra in palavra:
        if letra in letras_reveladas:
            resultado += letra
        else:
            resultado += "_"
    return resultado

def chute_palavra(palavra):
    palpite = input("Tente adivinhar a palavra inteira: ").lower()
    return palpite == palavra

def jogo_da_forca():
    print("Bem-vindo ao jogo da forca!")

    while True:
        opcao = input("Digite 1 para iniciar uma nova partida ou digite 2 para sair: ")
        
        if opcao == '2':
            print("Até outra hora!")
            break
        elif opcao == '1':
            palavra = escolher_palavra()
            letras_reveladas = []
            tentativas = 5
            letras_chutadas = []

            print(f"A palavra escolhida tem {len(palavra)} letras: {mostrar_palavra_oculta(palavra, letras_reveladas)}")

            while tentativas > 0:
                letra = input("Digite APENAS uma letra ou 'chutar' para tentar adivinhar a palavra: ").lower()

                if letra == 'sair':
                    print("Você escolheu sair, então até logo!")
                    return

                if letra == 'chutar':
                    if not chute_palavra(palavra):
                        tentativas = 0  
                        print("Você errou o palpite! Perdeu todas as tentativas.")
                        print(f"A palavra era '{palavra}'.")
                        break
                    else:
                        print("Parabéns! Você acertou a palavra!")
                        break

                if not letra.isalpha() or len(letra) != 1:
                    print("Entrada inválida. Por favor, digite uma única letra.")
                    continue

                if letra in letras_chutadas:
                    print("Você já chutou essa letra. Tente outra.")
                    continue

                letras_chutadas.append(letra)

                if letra in palavra:
                    letras_reveladas.append(letra)
                    print("Letra correta!")
                else:
                    tentativas -= 1
                    print(f"Letra incorreta. Chances restantes: {tentativas}")

                print(f"Palavra: {mostrar_palavra_oculta(palavra, letras_reveladas)}")
                print(f"Letras já informadas: {', '.join(letras_chutadas)}")

                if "_" not in mostrar_palavra_oculta(palavra, letras_reveladas):
                    print("Parabéns! Você descobriu a palavra!")
                    break

            if tentativas == 0 and "_" in mostrar_palavra_oculta(palavra, letras_reveladas):
                print(f"Infelizmente, a palavra era '{palavra}'. Boa sorte na próxima vez!")

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    jogo_da_forca()
