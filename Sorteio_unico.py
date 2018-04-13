#Autor: Jucio Gabriel
#Versao: 1.0
#Formas de Contato: Gmail: juciogabriel@gmail.com
#Whats app: 085985427699
#Gmail secundario: juciogabriel01@gmail.com
#Tentei melhorar ao maximo cada script.
#coding: utf-8
pri=seg=ter=qua=""
import random
for c in range(1,5):
    nome = str(input("Nome Do Aluno:")).strip()
    if c == 1:
        pri = nome
    if c == 2:
        seg = nome
    if c == 3:
        ter = nome
    else:
        qua = nome
a = random.choice([pri,seg,ter,qua])
print(f"O Escolhido Foi {a}")
    
