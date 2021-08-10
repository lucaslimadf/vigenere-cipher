import importlib
from cifraVigenere import CifraDeVigenere

def main():

  # texto = "IMAGINAÇÃO É MAIS IMPORTANTE QUE CONHECIMENTO"
  # palavra_chave = "ORQUESTRA"
  resposta = 9
  vigenere = CifraDeVigenere()

  while resposta != 0:
    print("\n===================")
    print("O que deseja fazer?\n")
    print("1 - CIFRAR mensagem")
    print("2 - DECIFRAR mensagem")
    print("3 - ATACAR")
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
      print("Ainda não implementado '_'")
      scape = input("\nPressione ENTER para retornar ao MENU...")

  # print(texto)
  # print(palavra_chave)
  # print(decifrado)

main()