numero = 0
soma = 0
quantidade = 0

while(numero != -1):
    numero = int(input("Digite o número desejado:"))

    if(numero != -1):
        soma = soma + numero
        quantidade = quantidade + 1

media = soma / quantidade
print("A média é: ", media)