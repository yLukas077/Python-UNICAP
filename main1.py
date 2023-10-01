# Lê a entrada como uma única string e a divide em código e quantidade
entrada = input().split()

codigo = entrada[0]
quantidade = entrada[1]

if codigo == '1':
    preco_unitario = 4.00
elif codigo == '2':
    preco_unitario = 4.50
elif codigo == '3':
    preco_unitario = 5.00
elif codigo == '4':
    preco_unitario = 2.00
elif codigo == '5':
    preco_unitario = 1.50
else:
    preco_unitario = 0.00

quantidade = int(quantidade)

valor_total = preco_unitario * quantidade

print("Total: R$ {:.2f}".format(valor_total))
