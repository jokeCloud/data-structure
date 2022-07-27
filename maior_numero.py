numeros = []

qtd_numeros = int(input('Quantos números você quer comparar? '))


for i in range(qtd_numeros):
    numeros.append(int(input('Digite um número: ')))


maior_numero = 0
contador = 0


for numero in numeros:
    if numero > contador:
        maior_numero = numero
    contador = numero

for numero in numeros:
    if numero > maior_numero:
        maior_numero = numero


print(maior_numero)
