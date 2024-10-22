# 5. Palíndromo: Verifique se uma palavra é um palíndromo.
palavra = str(input("Escreva a palavra que deseje ver se é palíndroma: "))
teste = palavra[::-1] #Recurso que inverte a ordem de escrite e coloca o texto ao contrario.
print(teste)
if palavra == teste:
    print("As palavras são palídrona!")
else:
    print("As palavras não são palídrona!")