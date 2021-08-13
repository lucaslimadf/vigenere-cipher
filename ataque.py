import unicodedata
import re

class ataqueVigenere (object):
  def encontrar_espacamento(self, cifrado):
    cifrado_norm = self.remover_espaco_esp(cifrado)
    sequencia_espacamento = []

    #verifica o espaçamento de sequencias repetidas. Tamanho = 3 
    for i in range(len(cifrado_norm)):
      #pega 3 letras em sequencia
      if (i+2 < len(cifrado_norm)):
        sequencia = cifrado_norm[i] + cifrado_norm[i+1] + cifrado_norm[i+2]

        #escolhidas as 3 letras, verifica no resto do texto quantas vezes encontra a sequencia
        for j in range(len(cifrado_norm)):
          if(j+2 < len(cifrado_norm)):
            sequencia_2 = cifrado_norm[j] + cifrado_norm[j+1] + cifrado_norm[j+2]
            #Se a sequencia do primeiro for tiver sido encontrada no texto, insere essa sequencia no array com seu espaçamento
            if((sequencia == sequencia_2)):
              if(j>i):
                espacamento = j-i
              else:
                espacamento = i-j

              elemento = [sequencia, espacamento]

              if ((elemento not in sequencia_espacamento) and elemento[1] != 0):
                sequencia_espacamento.append([sequencia, espacamento])
          else:
            break
      else:
        break
    
    return sequencia_espacamento

  #Remove espaços e caracteres especiais 
  def remover_espaco_esp(self, cifrado):
    # Unicode normalize transforma um caracter em seu equivalente em latin.
    nfkd = unicodedata.normalize('NFKD', cifrado)
    palavraSemAcento = u"".join([c for c in nfkd if not unicodedata.combining(c)])

    # Usa expressão regular para retornar a palavra apenas com números, letras e espaço. incluir numeros: re.sub('[^a-zA-Z0-9 \\\]', '', palavraSemAcento)
    texto = re.sub('[^a-zA-Z \\\]', '', palavraSemAcento)
    texto = texto.replace(" ", "")

    #retorna o texto cifrado apenas com as letras 
    return texto

  def obter_fatores(self, sequencia_espacamento):
    fatores = []
    fator_comum = []

    for i in range(len(sequencia_espacamento)):
      if sequencia_espacamento[i][1] not in fatores:
        fatores.append(sequencia_espacamento[i][1])

    #encontra os fatores 
    for fator in fatores:
      for divisor in range(2, fator+1):
        if (fator % divisor == 0):
          fator_comum.append(divisor)
    
    #conta quantas vezes cada fator aparece 
    contador = 0
    qtd_fator = []
    for fator in fator_comum:
      for i in fator_comum:
        if fator == i: 
          contador += 1
      if [fator, contador] not in qtd_fator:
        qtd_fator.append([fator, contador])
      contador = 0

    return qtd_fator

  def possiveis_tam_chave(self, qtd_fator):
    total = 0
    for fator in qtd_fator:
      total = total + fator[1]

    print("Os possíveis tamanhos da chave são: ")
    for fator in qtd_fator:
      percentual = (fator[1]*100)/total
      print(fator[0], "-", percentual, "%")
    print("\n")