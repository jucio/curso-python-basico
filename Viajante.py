#Autor: Jucio Gabriel
#Versao: 1.0
#Formas de Contato: Gmail: juciogabriel@gmail.com
#Whats app: 085985427699
#Gmail secundario: juciogabriel01@gmail.com
#Tentei melhorar ao maximo cada script.
#coding: utf-8

print(10*"=")
print("Viajante")
print(10*"=")

while True:
    km_percorridos = float(input("Qual A Quantidade De KM Percorridos:"))
    dias_alugados = int(input("Quantos Dias Voce Alugou Seu Carro:"))
    print(f"Voce Percorreu Por KM {km_percorridos}")
    print(f"Voce Alugou Esse Carro Por {dias_alugados} Dias")
    print(f"Voce Tera Que Pagar R$ {(60*dias_alugados) + (0.15*km_percorridos)}")
    
    stop = str(input("Quer Continuar [S/N]?")).strip().upper()[0]
    
    if stop == "N":
        break
        
print(16*"=")
print("Fim Da Execucao")
print(16*"=")