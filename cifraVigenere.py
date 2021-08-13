import unicodedata
import string

class CifraDeVigenere (object):

  # original = "IMAGINAÇÃO É MAIS IMPORTANTE QUE CONHECIMENTO"
  # palavra_chave = "ORQUESTRA"

  #Remover acentos e passa para maiuscula
  def adequar_texto(self, original):
    texto = unicodedata.normalize("NFD", original)
    texto = texto.encode("ascii", "ignore")
    texto = texto.decode("utf-8")
    texto = self.maiusculo(texto)
    return texto

  #Passar texto para maiusculo
  def maiusculo(self, texto):
    texto = texto.upper()
    
    return texto

  #Transcreve o texto com a palavra-chave
  def transcrever(self, texto, palavra_chave):
    tam_texto = len(texto)
    tam_palavra_chave = len(palavra_chave)

    transcrito = ""
    ponteiro = 0

    for i in range(tam_texto):
      if((ord(texto[i]) >= 65) and (ord(texto[i]) <= 90)):
        transcrito = "".join((transcrito,palavra_chave[ponteiro]))
        
        if(ponteiro == tam_palavra_chave-1):
          ponteiro = 0
        else:
          ponteiro += 1
      else:
        transcrito = "".join((transcrito,texto[i]))
    return transcrito  

  def alfabeto(self):
    alfabeto = string.ascii_uppercase 
    alfabeto = list(alfabeto)   
    return alfabeto

  #Montar tabela da cifra 
  def montar_tabela(self):
    tabula = []
    alfabeto = self.alfabeto()

    for i in range(len(alfabeto)):
      tabula.append(alfabeto)
      alfabeto = alfabeto[1:] + alfabeto[:1]
    
    return tabula

  #cifra a mensagem: frase original + frase transcrita = frase cifrada
  def cifrar_texto(self, texto, palavra_chave):
    texto = self.adequar_texto(texto)
    palavra_chave = self.adequar_texto(palavra_chave)
    transcrito = self.transcrever(texto, palavra_chave)

    cifrado = ""
    alfabeto = self.alfabeto()
    tabula = self.montar_tabela()

    for i in range(len(texto)):
      if((ord(texto[i]) >= 65) and (ord(texto[i]) <= 90)):
        ind_texto = alfabeto.index(texto[i]) 
        ind_trans = alfabeto.index(transcrito[i])
        cifrado = cifrado + tabula[ind_texto][ind_trans]
      else:
        cifrado = cifrado + texto[i]
    
    return cifrado
    
  # Decifra a mensagem: frase cifrada + palavra chave = frase original
  def decifrar_texto(self, cifrado, palavra_chave):
    cifrado = self.adequar_texto(cifrado)
    palavra_chave = self.adequar_texto(palavra_chave)
    transcrito = self.transcrever(cifrado, palavra_chave)
    decifrado = ""
    alfabeto = self.alfabeto()
    tabula = self.montar_tabela()

    for i in range(len(cifrado)):
      if((ord(cifrado[i]) >= 65) and (ord(cifrado[i]) <= 90)):
        ind_p_chave = alfabeto.index(transcrito[i])
        ind_cifrado = tabula[ind_p_chave].index(cifrado[i])
        decifrado = decifrado + alfabeto[ind_cifrado]
      else:
        decifrado = decifrado + cifrado[i]
    
    return decifrado

