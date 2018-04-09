#Funcao Que calcula A conversao para a opcao 1
from time import sleep

opcoes_validas = [1,2,3,4,5,6,7]#Lista De Opcoes Validas Para a Variavel Opcao

print(25*"=")
print("Conversor De Temperaturas")
print(25*"=")

def calculo_conversao():#Funcao Que da Um Time Para Calcular a Conversao
    print("Calculando Conversao...")
    sleep(2.3)
    
def fc():#Funcao Que calcula A conversao para a opcao 1
    
    f = float(input("Valor Da Temperatura Em Fahrenheit:"))
    
    print(f"A Temperatura em Fahrenheit é {f}")
    
    calculo_conversao()
    
    print(f"Sua Conversao Pra Celsius foi de {(f-32) * (5/9):.1f}")    

def fk():#Funcao Que calcula A conversao para a opcao 2
    
    cfk = float(input("Valor Da Temperatura Em Fahrenheit:"))
    
    print(f"A Temperatura Em Fahrenheit é de {cfk}")
    
    calculo_conversao()
    
    print(f"Sua Conversao Para Kelvin Foi De {(cfk-32) * (5/9) +273:.1f}")
  
def cf():#Funcao Que calcula A conversao para a opcao 3
    c = float(input("Digite A Temperatura Em Celsius:"))
    
    print(f"A Temperatura Em Celsius Foi de {c}")
    
    calculo_conversao()
    
    print(f"A Conversao Para Fahrenheit Foi de {(c*1.8) + 32:.1f}")      

def ck():#Funcao Que calcula A conversao para a opcao 4
    
    ckc = float(input("Digite A Temperatura Em Celsius:"))
    
    calculo_conversao()
    
    print(f"A Temperatura Convertida Para Kelvin Foi de {(ckc+273):.1f}")

def kc():#Funcao Que calcula A conversao para a opcao 5
    
    kcc = float(input("Digite O Valor Da Temperatura Em Kelvin:"))
   
    calculo_conversao()
     
    print(f"A Temperatura Convertida Para Celsius Foi de {(kcc-273):.1f}")

def kf():#Funcao Que calcula A conversao para a opcao 6
    kfc = float(input("Digite O Valor Da Temperatura Em Kelvin:"))
    
    print(f"A Temperatura Em Kelvin foi de {kfc}")
    
    calculo_conversao()
    
    print(f"A Conversao Para Fahrenheit Foi De {((kfc-273)*1.8)+32:.1f}")
    
while True:
    print("""Escolha Uma Opcao:
        [1]Fahrenheit Para Celsius
        [2]Fahrenheit Para Kelvin
        [3]Celsius Para Fahrenheit
        [4]Celsius Para Kelvin
        [5]Kelvin Para Celsius
        [6]Kelvin Para Fahrenheit
        [7]Sair Do Programa""")
        
    opcao = int(input("Escolha Uma opcao:"))#Variavel Que o usuario escolhe entre as disponiveis
    
    if opcao not in opcoes_validas:#Condicao que testa se o usuario Digitar Uma Opcao Errada
        print("Analisando Opcao...")
        sleep(3)
        print("Opcao Invalida")
   
    else:#Condicao Que Testa Se O usuario digitar A Opcao Certa
        print("Analisando Opcao...")
        sleep(1.4)
        
    if opcao == 1:
        fc()
        
    elif opcao == 2:
        fk()
     
    elif opcao == 3:
        cf()
    
    elif opcao == 4:
        ck()
        
    elif opcao == 5:
        kc()
    elif opcao == 6:
        kf()
    elif opcao == 7:
        break
      
print(20*"=")
print("Fim Da Execucao")
print(20*"=")
        
         
        
        
        
