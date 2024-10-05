import random
escolha = 0
saldo = 0
timesV = ["Brasil", "Italia", "Estados Unidos", "Russia", "Alemanha", "Polonia", "Cuba", "Argentina"]
timesB = ["Los Angeles Lakers", "Chicago Bulls", "Boston Celtics", "Golden State Warriors", "Miami Heat", "San Antonio Spurs", "Real Madrid ", "Barcelona", "Dallas Mavericks", "Toronto Raptors"]
timesF = ["Real Madrid", "Barcelona", "Manchester United", "Liverpool", "Bayern de Munique", "Paris Saint-Germain", "AC Milan", "Manchester City", "Chelsea", "Juventus"]

print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\nBem vindo ao PETANO!\n=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
print("Digite seu nome : ")
Nome = input()
print(f"Olá, {Nome}! Digite sua idade : ")
Idade = int(input())
if Idade < 18:
    print("Você tem que ser maior de 18 para apostar.")
    exit()
    

    
while escolha != 5:
    print(f'Saldo atual : R${saldo}\n' \
          '=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n' \
          'O que vai ser hoje?\n' \
          'Jogue com moderação...\n' \
          '1. Depositar\n2. Sacar\n3. Apostar\n4. Saldo\n5. Sair\n' \
          '=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n')
    escolha = int(input("Comando : "))
    if escolha == 1:                           #Pra depositar money
       print("Quanto deseja depositar? : ")
       valor = float(input())
       saldo = saldo + valor
       print("Operação realizada com sucesso!")
    elif escolha == 2:                         #Pra tirar money
       print("Quanto deseja sacar? : ")
       valor = float(input())
       while valor > saldo:
           print("Saldo insuficiente para ser sacado!")
           valor = float(input("Insira um valor valido : "))
    saldo -= valor
    print("Operação realizada com sucesso!")
    elif escolha == 3:                         #Pra apostar money
       print("Quanto deseja apostar? : ")
       valor = float(input())
       while valor > saldo:
           print("Saldo insuficiente para ser sacado!")
           valor = float(input("Insira um valor valido : "))
       print('EM qual jogo quer apostar?\n' \
          '=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n' \
          '1. Basquete\n2. Tênis\n3. Futebol\n
          '=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n')
       escolhaJogo = int(input("Comando :"))
       if escolhaJogo == 1:
           print("Esses são os eventos atuais:")
