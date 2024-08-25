import numpy as np

def criar_matriz_complexa_diversificada(n):
    # Gera diferentes tipos de números complexos
    casos = [
        lambda: np.random.rand() + 1j * np.random.rand(),    # Caso 1: Real e imaginário positivos
        lambda: -np.random.rand() + 1j * -np.random.rand(),  # Caso 2: Real e imaginário negativos
        lambda: np.random.rand() + 1j * -np.random.rand(),   # Caso 3: Real positivo, imaginário negativo
        lambda: -np.random.rand() + 1j * np.random.rand()    # Caso 4: Real negativo, imaginário positivo
    ]
    
    # Inicializa a matriz vazia
    matriz_complexa = np.empty((n, n), dtype=complex)
    
    # Preenche a matriz com valores complexos diversificados
    for i in range(n):
        for j in range(n):
            matriz_complexa[i, j] = np.random.choice(casos)()
    
    return matriz_complexa

# Exemplo de uso
n = 3  # Defina o tamanho da matriz
matriz = criar_matriz_complexa_diversificada(n)
print(matriz)
