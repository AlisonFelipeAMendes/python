# 3. Números Primos: Verifique se um número é primo.
def eh_primo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Recebendo o número do usuário
numero = int(input("Digite um número para verificar se é primo: "))

# Verificando se o número é primo
if eh_primo(numero):
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")
