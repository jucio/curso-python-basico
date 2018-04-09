#Autor: Jucio Gabriel
#Versao: 1.0
#Formas de Contato: Gmail: juciogabriel@gmail.com
#Whats app: 085985427699
#Gmail secundario: juciogabriel01@gmail.com
#Tentei melhorar ao maximo cada script.
#coding: utf-8

from time import sleep as s 

print(28*"=")
print("Calculo Aumento De Salario")
print(28*"=")

while True:
    salario_antigo = float(input("Digite O Valor do Seu Antigo Salario:"))
    print("Calculando Salario Com 15% De Aumento...")
    s(2)
    print(f"Seu Salario Era de R$ {salario_antigo} Com O Aumento Ficou de R$ {salario_antigo+(salario_antigo*15/100):.1f}")
    
    stop = str(input("Quer Continuar [S/N]")).strip().upper()[0]
    if stop == "N":
        break
print(17*"=")
print("Fim Da Execucao")
print(17*"=")
