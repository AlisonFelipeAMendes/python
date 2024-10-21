 # 2. Fatorial: Calcule o fatorial de um número dado.
# Recebendo o número do usuário
numero = int(input("Digite o número que você deseja saber o fatorial: "))

# Inicializando a variável que armazenará o resultado
resultado = 1

# Calculando o fatorial utilizando o for no formato regressivo
for i in range(numero, 0, -1):
    resultado *= i

# Exibindo o resultado
print(f"O fatorial de {numero} é {resultado}") #utilizando f-string para dispor as informações das variaveis