vogais = "aeiouAEIOU|àáãâÁÀÃÂéèêÉÈÍÌÎóòõôÓÒÕúùûÚÙÛ"
qtd_vogais = 0

texto = input ("Colque uma palavra:")
for vogal in vogais:
    for letra in texto:
        if(letra == vogal):
            qtd_vogais +=1

print("A quantidade de vogais é", qtd_vogais)