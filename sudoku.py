def mostrar_fachada():
    limpar_tela()
    print("=" * 50)
    print("  ███████ ██    ██ ██████  ███████ ██  ██ ██    ██ ")
    print("  ██      ██    ██ ██   ██ ██   ██ ██ ██  ██    ██")
    print("  ███████ ██    ██ ██   ██ ██   ██ ████   ██    ██")
    print("       ██ ██    ██ ██   ██ ██   ██ ██ ██  ██    ██")
    print("  ███████  ██████  ██████  ███████ ██  ██  ██████   ")
    print("=" * 50)
    print("                SUPER JOGO DE SUDOKU")
    print("-" * 50)
    print("Objetivo:")
    print("Complete o tabuleiro 9x9 com números de 1 a 9,")
    print("sem repetir em linhas, colunas e subgrades 3x3.")
    print()
    input("Pressione Enter para iniciar o jogo...")


import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def imprimir_tabuleiro(tabuleiro):
    limpar_tela()
    print("    1 2 3   4 5 6   7 8 9")
    print("  +-------+-------+-------+")
    for i in range(9):
        linha = f"{i+1} | "
        for j in range(9):
            valor = tabuleiro[i][j]
            linha += f"{valor if valor != 0 else '.'} "
            if (j + 1) % 3 == 0:
                linha += "| "
        print(linha)
        if (i + 1) % 3 == 0:
            print("  +-------+-------+-------+")

def verificar_linha(tabuleiro, linha, num):
    return num not in tabuleiro[linha]

def verificar_coluna(tabuleiro, coluna, num):
    return all(tabuleiro[i][coluna] != num for i in range(9))

def verificar_subgrade(tabuleiro, linha, coluna, num):
    inicio_linha = (linha // 3) * 3
    inicio_coluna = (coluna // 3) * 3
    for i in range(inicio_linha, inicio_linha + 3):
        for j in range(inicio_coluna, inicio_coluna + 3):
            if tabuleiro[i][j] == num:
                return False
    return True

def jogada_valida(tabuleiro, linha, coluna, num):
    if tabuleiro[linha][coluna] != 0:
        return False
    return (verificar_linha(tabuleiro, linha, num) and
            verificar_coluna(tabuleiro, coluna, num) and
            verificar_subgrade(tabuleiro, linha, coluna, num))

def verificar_vitoria(tabuleiro):
    for linha in range(9):
        for coluna in range(9):
            num = tabuleiro[linha][coluna]
            if num == 0:
                return False
    return True

def receber_jogada():
    while True:
        try:
            entrada = input("Digite sua jogada no formato linha coluna número (ex: 2 3 5): ")
            linha, coluna, numero = map(int, entrada.strip().split())
            if 1 <= linha <= 9 and 1 <= coluna <= 9 and 1 <= numero <= 9:
                return linha - 1, coluna - 1, numero
            else:
                print("Valores devem estar entre 1 e 9.")
        except ValueError:
            print("Entrada inválida. Tente novamente no formato correto.")

def jogo_sudoku():
    tabuleiro_inicial = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    tabuleiro = [linha[:] for linha in tabuleiro_inicial]

    while True:
        imprimir_tabuleiro(tabuleiro)
        if verificar_vitoria(tabuleiro):
            print("Parabéns! Você completou o Sudoku!")
            break

        linha, coluna, numero = receber_jogada()

        if tabuleiro_inicial[linha][coluna] != 0:
            print(" Você não pode alterar uma célula já preenchida!")
            input("Pressione Enter para continuar...")
            continue

        if jogada_valida(tabuleiro, linha, coluna, numero):
            tabuleiro[linha][coluna] = numero
        else:
            print(" Jogada inválida! Conflito com linha, coluna ou subgrade.")
            input("Pressione Enter para tentar novamente...")

if __name__ == "__main__":
    jogo_sudoku()
