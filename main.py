import importlib
from cifraVigenere import CifraDeVigenere
from ataque import ataqueVigenere

def main():

  resposta = 9
  opt = 9
  vigenere = CifraDeVigenere()
  ataque = ataqueVigenere()

  while resposta != 0:
    print("\n===================")
    print("O que deseja fazer?\n")
    print("1 - CIFRAR mensagem")
    print("2 - DECIFRAR mensagem")
    print("3 - ATACAR")
    print("4 - USAR ARQUIVO PARA CIFRAR OU DECIFRAR")
    print("0 - SAIR\n")

    resposta = int(input())

    if resposta == 1:
      texto = input("Informe o texto a ser cifrado: ")
      palavra_chave = input("Informe a palavra-chave: ")
      cifrado = vigenere.cifrar_texto(texto, palavra_chave)
      print("\nTexto Cifrado:")
      print(cifrado)
      scape = input("\nPressione ENTER para retornar ao MENU...")

    elif resposta == 2:
      cifrado = input("Informe o texto cifrado: ")
      palavra_chave = input("Informe a palavra-chave: ")
      decifrado = vigenere.decifrar_texto(cifrado, palavra_chave)
      print("\nTexto Decifrado:")
      print(decifrado)
      scape = input("\nPressione ENTER para retornar ao MENU...")
    
    elif resposta == 3:
      cifrado_atk = input("Informe o texto cifrado: ")
      sequencia_espacamento = ataque.encontrar_espacamento(cifrado_atk)
      qtd_fator = ataque.obter_fatores(sequencia_espacamento)
      tam_chave = ataque.possiveis_tam_chave(qtd_fator)
      scape = input("\nPressione ENTER para retornar ao MENU...")

    elif resposta == 4:
      while((opt != 1) and (opt != 2) and (opt != 0)):
        print("\n===================")
        print("O que deseja fazer?\n")
        print("1 - CIFRAR mensagem (arquivo cifrar.txt)")
        print("2 - DECIFRAR mensagem (arquivo decifrar.txt)")
        print("0 - RETORNAR AO MENU ANTERIOR")
        opt = int(input())

        if opt == 1: 
          arquivo = open('./entrada_dados/cifrar.txt', 'r') 
          texto = arquivo.read()
          palavra_chave = input("Informe a palavra-chave: ")
          cifrado_arq = vigenere.cifrar_texto(texto, palavra_chave)
          print("\nTexto Cifrado:")
          print(cifrado_arq)

        elif opt == 2:
          arquivo = open('./entrada_dados/decifrar.txt', 'r') 
          texto = arquivo.read()
          palavra_chave = input("Informe a palavra-chave: ")
          decifrado_arq = vigenere.cifrar_texto(texto, palavra_chave)
          print("\nTexto Decifrado:")
          print(decifrado_arq)
          
      opt = 9
      scape = input("\nPressione ENTER para retornar ao MENU...")

main()