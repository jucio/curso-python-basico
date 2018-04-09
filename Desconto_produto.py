#Autor: Jucio Gabriel
#Versao: 1.0
#Formas de Contato: Gmail: juciogabriel@gmail.com
#Whats app: 085985427699
#Gmail secundario: juciogabriel01@gmail.com
#Tentei melhorar ao maximo cada script.
#coding: utf-8
from time import sleep

while True:
    nome_do_produto = str(input("Nome Do Produto:")).strip().title()
    
    preco_do_produto = float(input(f"Digite O Valor Do {nome_do_produto}:"))
    
    print(f"O Produto Se Chama {nome_do_produto}")
    
    print(f"O Preco do produto é de {preco_do_produto}")
    
    print(f"Seu Novo Preco com 15% De Desconto é de {preco_do_produto-(preco_do_produto*15/100)}")
    stop = str(input("Quer Continuar: [S/N]")).strip().upper()[0]
    if stop == "N":
        break
print(18*"=")
print("Fim Da Execucao")
print(18*"=")
    
