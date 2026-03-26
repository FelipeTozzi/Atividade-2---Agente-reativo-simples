#Grupo: Mateus Euzébio, Felipe Tozzi Marinho de Oliveira, Ivan de Oliveira Nantes

import random

campo = 10

limite_movimentos = 500

ambiente = [" " for _ in range(campo)]

qtd_sujeira = random.randint(2, 6)

posicoes = random.sample(range(campo), qtd_sujeira)

for (pos) in posicoes:
    ambiente[pos] = "~"

robo = random.randint(0, campo - 1)


def mostrar():
    for i in range(campo):
        if i == robo:
            print("R", end=" ")
        else:
            print(ambiente[i], end=" ")
    print()
    print("-" * 30)

movimentos = [-1,1]

passos = 0

while passos < limite_movimentos:
    mostrar()
    
    input("Pausado, turno - " + str(passos) + " limite " + str(limite_movimentos))

    x = robo

    if ambiente[robo] == "~":
        print(f"Posição ({robo}) limpa")
        ambiente[robo] = " "
    
    else:
        dx = random.choice(movimentos)
        novo = robo + dx
        
        if 0 <= novo < campo:
            robo = novo

    passos += 1

mostrar()

if passos >= limite_movimentos:
    print("Limite de movimentos atingido. Encerrando o programa.")