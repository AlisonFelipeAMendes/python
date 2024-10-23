
linhas = int(input("Informe quantas linhas a matriz terá:"))
colunas = int(input("Informe quantas colunas a matriz terá:"))



# matriz = [[0 for _ in range(linhas)] for _ in range(colunas)]
matriz = [[0 for _ in range(colunas)] for _ in range(linhas)]
for i in range(linhas):
    for j in range(colunas):
        matriz[i][j] = str(f"[{i}.{j}]")
        # print(" ".join(matriz[i][j]))

# Imprime a matriz de forma organizada
for linha in matriz:
    print(" ".join(linha))
    