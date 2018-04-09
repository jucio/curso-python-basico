#Autor: Jucio Gabriel
#Versao: 1.0
#Formas de Contato: Gmail: juciogabriel@gmail.com
#Whats app: 085985427699
#Gmail secundario: juciogabriel01@gmail.com
#Tentei melhorar ao maximo cada script.
#coding: utf-8
while True:
    alt = float(input("Digite O Valor Da Altura:"))
    
    lar = float(input("Digite O Valor Da Largura:"))
    
    print(f"A Altura é de {alt}")
    
    print(f"A Largura é de {lar}")
    
    print(f"Voce Precisara de {(alt*lar)/2} Litros de Tinta Para Pintar {alt*lar}")
    
    stop = str(input("Quer Continuar: [S/N]")).strip().upper()[0]
    
    if stop  == "N":
        break
        
print(18*"=")
print("Fim Da Execucao")
print(18*"=")