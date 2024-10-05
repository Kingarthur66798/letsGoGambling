import random
escolha = 0
saldo = 0



print("=========================\nBem vindo ao PETANO!\n=========================")
print("Digite seu nome : ")
Nome = input()
print(f"Olá, {Nome}! Digite sua idade : ")
Idade = int(input())
if Idade < 18:
    print("Você tem que ser maior de 18 para apostar.")
    exit()
    

    
while escolha != 5:
    print(f'Saldo atual : R${saldo}\n' \
          '================================\n' \
          'O que vai ser hoje?\n' \
          'Jogue com moderação...\n' \
          '1. Depositar\n2. Sacar\n3. Apostar\n4. Saldo\n5. Sair\n' \
          '================================\n')
    escolha = int(input("Comando : "))
    if escolha == 1:
       print("Quanto deseja depositar? : ")
       valor = float(input())
       saldo = saldo + valor
       print("Operação realizada com sucesso!")
    elif escolha == 2:
       print("Quanto deseja sacar? : ")
       valor = float(input())
       while valor > saldo:
           print("Saldo insuficiente para ser sacado!")
           valor = float(input("Insira um valor valido : "))
    saldo -= valor
    print("Operação realizada com sucesso!")