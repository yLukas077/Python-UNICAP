entrada = input().split()
salario = float(entrada[0])
novo_salario = 0.0
valor_reajuste = 0.0
percentual = 0

if salario <= 400.00:
    percentual = 15
elif salario <= 800.00:
    percentual = 12
elif salario <= 1200.00:
    percentual = 10
elif salario <= 2000.00:
    percentual = 7
else:
    percentual = 4

valor_reajuste = salario * (percentual / 100)
novo_salario = salario + valor_reajuste

print("Novo salario: {:.2f}".format(novo_salario))
print("Reajuste ganho: {:.2f}".format(valor_reajuste))
print("Em percentual: {} %".format(percentual))
