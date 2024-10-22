# 4. Fibonacci: Gere a sequência de Fibonacci até um número n.
numero = int(input("Informe o número que deseja sabe o fibonacci: "))

a, b = 0, 1
while a < numero:
    print(a)
    a, b = b, a + b