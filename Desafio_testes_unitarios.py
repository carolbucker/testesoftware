# Desafio - Testes Unitários

# Criando programa

#Importando a biblioteca random
import random

# Definindo a variável lista com 5 números aleatórios entre 1 e 100
lista = [random.randint(1,100) for _ in range(5)]



#Solicitando ao usuário um número para o usuário adicionar na lista e incluir na lista
numero1 = int(input("Digite um número para adicionar a lista: "))
lista.append("numero1")

#Exibir lista atualizada
