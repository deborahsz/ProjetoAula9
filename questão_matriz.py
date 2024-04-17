import numpy as np

# Criando a matriz A de tamanho 10x10 com valores inteiros aleatórios
A = np.random.randint(1, 100, size=(10, 10))

# Imprimindo a matriz A
print("Matriz A:")
print(A)

# Calculando a soma de todos os valores da matriz A
soma_A = np.sum(A)
print("\nSoma de todos os valores da matriz A:", soma_A)

# Criando a matriz B onde cada item é o valor da matriz A multiplicado por 3
B = A * 3

# Imprimindo a matriz B
print("\nMatriz B (cada item é o valor da matriz A * 3):")
print(B)
