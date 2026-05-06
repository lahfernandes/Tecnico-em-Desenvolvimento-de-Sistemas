idade = int(input("Digite sua idade:"))
carteira = input("Você tem CNH? ")

if(idade >= 18 and carteira == "Sim"):
    print("Você pode dirirgir!")
elif(idade >= 18 and carteira == "Não"):
    print("Você não pode dirergir!")
elif(idade < 18):   
    print("Você não pode tirar CNH")
else:
    print("Erro!")
