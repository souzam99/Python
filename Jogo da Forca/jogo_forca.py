# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 12:33:08 2021

@author: souza

Projeto: Jogo da Forca

Concitos abordados:
    Programação Orientada a Objetos
    
Nível de dificuldade: Médio

"""

forca_carcteres = [
' +-----|\n\
 |     |\n\
       |\n\
       |\n\
       |\n\
       |\n\
_______|\n',
' +-----|\n\
 |     |\n\
 0     |\n\
       |\n\
       |\n\
       |\n\
_______|\n',
' +-----|\n\
 |     |\n\
 0     |\n\
 |     |\n\
       |\n\
       |\n\
_______|\n',
' +-----|\n\
 |     |\n\
 0     |\n\
/|     |\n\
       |\n\
       |\n\
_______|\n',
' +-----|\n\
 |     |\n\
 0     |\n\
/|\    |\n\
       |\n\
       |\n\
_______|\n',
' +-----|\n\
 |     |\n\
 0     |\n\
/|\    |\n\
/      |\n\
       |\n\
_______|\n',
' +-----|\n\
 |     |\n\
 0     |\n\
/|\    |\n\
/ \    |\n\
       |\n\
_______|\n',]



import random




class forca():
    def __init__ (self, palavra):
        self.palavra = {}
        self.erros = 0
        self.palavras_certas = []
        self.palavras_erradas = []
        self.espacos = {}
        
        num = 0
        for i in palavra:
            self.palavra.update({num:i})
            self.espacos.update({num:"_"})
            num += 1
        
            
    def imprimir(self):
        print("\n==================== JOOG DA FORCA ====================\n")
        print(forca_carcteres[self.erros])
        print('Palavra:')
        aux = ""
        for i in self.espacos.values():
            aux += i + " "
        print(aux)
        print("\n")
        
        aux = ""
        print("Letras certas:")
        for i in self.palavras_certas:
            aux += i + " "
        print(aux)
        
        aux = ""
        print("Letras errdadas:")
        for i in self.palavras_erradas:
            aux += i + " "
        print(aux)
        
        
        
    def verificar(self, letra):
        encontrou = False
        print(letra)
        
        
        if self.palavras_certas.count(letra) or self.palavras_erradas.count(letra):
            print("A palavra já selecionada!\n")
            self.contabilizar_erro()
        else:
            for k,i in self.palavra.items():
                if letra == i:
                    self.espacos[k] = i
                    encontrou = True
                    if not self.palavras_certas.count(letra):
                        self.palavras_certas.append(letra)
                        self.palavras_certas.sort()
            if not encontrou:
                print("A palavra não possui essa letra!\n")
                self.palavras_erradas.append(letra)
                self.palavras_erradas.sort()                
                self.contabilizar_erro()
    
    def contabilizar_erro(self):
        self.erros += 1
        
    
    def testar_vitoria(self):
        aux = False
        for i in self.espacos.values():
            if i == "_":
                aux = True
        if aux:    
            return False
        else:
            self.imprimir()
            print("Parabéns, você acertou a palavra!")
            return True
            
            
    def testar_derrota(self):
        if self.erros > 6:
            print("\nVocê foi enforcado!")
            return True
        else:
            return False
                    
       
        


class main():
    jogar = True
    
    while jogar:
        arquivo = open('palavras.txt','r')
        conteudo = arquivo.read()
        conteudo = str(conteudo)
        palavras = conteudo.split()
        palavra = palavras[random.randrange(0,len(palavras))]
        forca1 = forca(palavra)
        while not forca1.testar_vitoria() and not forca1.testar_derrota():
            forca1.imprimir()
            letra = input("Digite uma letra: ")
            forca1.verificar(letra)      
        aux = input("Jogar novamente? (s/n): ")
        if aux != "s":
            jogar = False
    




