
# 1 - capitalize(): Converte o primeiro caractere para maiúsculo.

texto = "python é incrível"
print(texto.capitalize())  # Python é incrível

# 2 - lower(): Converte todos os caracteres para minúsculo.

texto = "PYTHON É INCRÍVEL"
print(texto.lower())  # python é incrível

# 3 - upper(): Converte todos os caracteres para maiúsculo.

texto = "python é incrível"
print(texto.upper())  # PYTHON É INCRÍVEL

# 4 - count(substring): Conta quantas vezes uma substring aparece na string.

texto = "banana"
print(texto.count("a"))  # 3

# 5 - find(substring): Retorna o índice da primeira ocorrência da substring.

texto = "encontrar"
print(texto.find("tra"))  # 5

# 6 - replace(old, new): Substitui todas as ocorrências de uma substring por outra.

texto = "olá mundo"
print(texto.replace("mundo", "Python"))  # olá Python

# 7 - split(separator): Divide a string em uma lista, usando o separador especificado.

texto = "um,dois,três"
print(texto.split(","))  # ['um', 'dois', 'três']

# 8 - strip(): Remove espaços em branco do início e do fim da string.

texto = "   espaço   "
print(texto.strip())  # espaço

# 9 - startswith(prefix): Verifica se a string começa com o prefixo especificado.

texto = "Python"
print(texto.startswith("Py"))  # True

# 10 - endswith(suffix): Verifica se a string termina com o sufixo especificado.

texto = "Python"
print(texto.endswith("on"))  # True