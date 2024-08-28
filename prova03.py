compras = {}
cont = 0
while cont < 5:
 produto = str(input('Informe o nome do produto: ')).strip()
 valor = float(input('Informe o preço do produto: '))
 compras[produto]= valor
 cont += 1
 
print(compras)
total = compras.values()
print(f'o  valor total das compras é de {sum(total):.2f}')