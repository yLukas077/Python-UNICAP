entrada = input().split()

count_positivos = 0
soma_positivos = 0

valor1 = float(entrada[0])
valor2 = float(entrada[1])
valor3 = float(entrada[2])
valor4 = float(entrada[3])
valor5 = float(entrada[4])
valor6 = float(entrada[5])

if valor1 > 0:
    count_positivos += 1
    soma_positivos += valor1

if valor2 > 0:
    count_positivos += 1
    soma_positivos += valor2

if valor3 > 0:
    count_positivos += 1
    soma_positivos += valor3

if valor4 > 0:
    count_positivos += 1
    soma_positivos += valor4

if valor5 > 0:
    count_positivos += 1
    soma_positivos += valor5

if valor6 > 0:
    count_positivos += 1
    soma_positivos += valor6

media_positivos = soma_positivos / count_positivos

print(f"{count_positivos} valores positivos")
print(f"{media_positivos:.1f}")
