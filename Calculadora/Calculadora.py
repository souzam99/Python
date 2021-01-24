# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 11:00:37 2021

@author: souza

Projeto: Calculadora

Concitos abordados:
    Estruturas de controle;
    Funções
    Funções lambda
    
Nível de dificuldade: Inciante

"""

def imprimirOpcoes():
    print("######################################")
    print("#                                    #")
    print("#       Calculadora em Python        #")
    print("#                                    #")
    print("######################################")
    print("")
    print("Selecione uo número da operação desejada:")
    print("")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

soma = lambda n1,n2: n1 + n2
sub = lambda n1,n2: n1 - n2
mul = lambda n1,n2: n1 * n2
div = lambda n1,n2: n1 / n2
    
def calcular(n1, n2, opcao):
    if opcao == 1:
        resultado = soma(n1, n2)
        print("\n%s + %r = %u" %(n1, n2, resultado))
    elif opcao == 2:
        resultado = sub(n1, n2)
        print("\n%s - %r = %u" %(n1, n2, resultado))
    elif opcao == 3:
        resultado = mul(n1, n2)
        print("\n%s * %r = %u" %(n1, n2, resultado))
    elif opcao == 4:
        if n2 == 0:
            print("Não é possível realizar uma divisão por 0!")
        else:
            resultado = div(n1, n2)
            print("\n%s / %r = %u" %(n1, n2, resultado))
        

continuar = True
while continuar == True:
    imprimirOpcoes()
    opcao = int(input("Digite a opção (1/2/3/4/5): "))
    if opcao in range(1,6):
        n1 =  float(input("Digite o primeiro número: "))
        n2 =  float(input("Digite o segundo número: "))
        calcular(n1,n2, opcao)
        aux = input("Deseja realizar outro cálculo? (s/n): ")
        while (aux != "s") and (aux != "n"):
            print("Opçao invalida!")
            aux = input("Deseja realizar outro cálculo? (s/n): ")
        if aux == "s":
            continuar = True
        elif aux == "n":
            continuar = False
            print("Obrigado!")
    else:
        print("\nOpção invalida, favor digitar outro opção. \n\n")
        



