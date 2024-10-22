#Ordenação: Implemente o algoritmo de ordenação Bubble Sort.
quantidade = int(input("Quantos elementos serão ordenados: "))
elementos = []

for i in range(quantidade):
    valor  = int(input("Informe o valor do item: "))
    elementos.append(valor)
    print(elementos[i])
    elementos.sort

for i in range(quantidade): print(elementos[i])