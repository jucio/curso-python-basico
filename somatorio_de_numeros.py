#Autor: Jucio Gabriel
#Versao: 1.0
#Formas de Contato: Gmail: juciogabriel@gmail.com
#Whats app: 085985427699
#Gmail secundario: juciogabriel01@gmail.com
#Tentei melhorar ao maximo cada script.
#coding: utf-8
print(20*"=")
print("Somatorio de Numeros")
print(20*"=")
soma = pri = seg = 0
for num in range(1,3):
    numero = int(input("Numero:"))
    soma += numero
    if num == 1:
        pri = numero
    elif num == 2:
        seg = numero
print(f"A soma entre {pri} e {seg} totaliza {soma}")