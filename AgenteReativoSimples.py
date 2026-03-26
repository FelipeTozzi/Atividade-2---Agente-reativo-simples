#Grupo: Mateus Euzébio, Felipe Tozzi Marinho de Oliveira, Ivan de Oliveira Nantes

import random

linhas, colunas = 5, 5

limite_movimentos = 500

ambiente = [[" " for _ in range(colunas)] for _ in range(linhas)]

qtd_sujeira = random.randint(2, 6)

posicoes = set()
while len(posicoes) < qtd_sujeira:
    x = random.randint(0, linhas - 1)
    y = random.randint(0, colunas - 1)
    posicoes.add((x, y))

for (x, y) in posicoes:
    ambiente[x][y] = "~"

robo = [random.randint(0, linhas - 1), random.randint(0, colunas - 1)]


def mostrar():
    for i in range(linhas):
        for j in range(colunas):
            if [i, j] == robo:
                print("R", end=" ")
            else:
                print(ambiente[i][j], end=" ")
        print()
    print("-" * 20)

movimentos = [(-1,0), (1,0), (0,-1), (0,1)]

passos = 0

while passos < limite_movimentos:
    mostrar()
    
    input("Pausado, turno - " + str(passos) + " limite " + str(limite_movimentos))

    x, y = robo

    if ambiente[x][y] == "~":
        print(f"Posição ({x}, {y}) limpa")
        ambiente[x][y] = " "
    
    else:
        dx, dy = random.choice(movimentos)
        novo_x = x + dx
        novo_y = y + dy
        
        if 0 <= novo_x < linhas and 0 <= novo_y < colunas:
            robo = [novo_x, novo_y]

    passos += 1

mostrar()

if passos >= limite_movimentos:
    print("Limite de movimentos atingido. Encerrando o programa.")