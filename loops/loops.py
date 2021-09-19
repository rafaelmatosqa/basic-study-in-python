# Loop FOR

# Criando uma tupla e imprimindo cada um dos valores
tp = (2, 3, 4)
for i in tp:
    print(i)

# Criando uma lista e imprimindo cada um dos valores
lista = ["maçâ", "uva", "melancia", "mamão"]
for i in lista:
    print(i)

# Imprimindo os valores no intervalo entre 0 e 5 (exclusive)
for contador in range(0, 5):
    print(contador)

# Imprimindo na tela os números pares da lista de números
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in lista:
    if num % 2 == 0:
        print(num)

# Imprimindo na tela os números ímpares da lista de números
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in lista:
    if num % 2 != 0:
        print(num)

# Listar todos os números primos

start = 10
end = 20

for i in range(start, end + 1):
    if i > 1:
        for j in range(2, i):
            if (i % j == 0):
                break
        else:
            print(i)

# Strings também são sequências
for caracter in 'Python é uma linguagem de programação divertida!':
    print(caracter)

# Loops aninhados
for i in range(0, 5):
    for a in range(0, 5):
        print(a)

# Operando os valores de uma lista com loop for
listaB = [32, 53, 85, 10, 15, 17, 19]
soma = 0
for i in listaB:
    double_i = i * 2
    soma += double_i

print(soma)

# Loops em lista de listas
listas = [[1, 2, 3], [10, 15, 14], [10.1, 8.7, 2.3]]
for valor in listas:
    print(valor)

# Contando os itens de uma lista
lista = [5, 6, 10, 13, 17]
count = 0
for item in lista:
    count += 1

print(count)

# Contando o número de colunas
lst = [[1, 2, 3], [3, 4, 5], [5, 6, 7]]
primeira_linha = lst[0]
count = 0
for column in primeira_linha:
    count = count + 1

print(count)

# Pesquisando em listas
listaC = [5, 6, 7, 10, 50]

# Loop através da lista
for item in listaC:
    if item == 5:
        print("Número encontrado na lista!")

# Listando as chaves de um dicionário
dict = {'k1': 'Python', 'k2': 'R', 'k3': 'Scala'}
for item in dict:
    print(item)

# Imprimindo chave e valor do dicionário. Usando o método items() para retornar os itens de um dicionário
for k, v in dict.items():
    print(k, v)

# Loop for com soma de valores de um array de objetos
lista_de_Valores = [{'valor1': 32, 'valor2': 53}, {'valor1': 45, 'valor2': 33}]
totals = 0
for i in lista_de_Valores:
    double_i = i['valor1'] * 2  # multiplica por dois cada item valor1 da lista
    totals += double_i  #soma os valores após multiplicados

print(totals)
