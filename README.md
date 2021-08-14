# vigenere-cipher
Este programa foi desenvolvido para fins de estudo na área de segurança computacional. 

## Execução do programa 
Para executar o projeto:
1. Navegue até a pasta raíz.
2. Execute o comando `python3 main.py`.

## Funcionamento 
O programa é composto por um cifrador/decifrador, que utiliza a lógica desenvolvida por Vigenère para criptografar uma mensagem usando uma palavra-chave, e
uma simulação de de ataque, que tem o intuito de quebrar a cifra e tentar descriptografar a mensagem utilizando o método “Kasiski Examination”. 
**O ataque ainda não foi implementado corretamente**

### Menu de Escolhas 
Ao executar o comando para iniciar o vigenere-cipher, você poderá selecionar uma das opções, digitando seu respectivo número:
1. Cifrar um texto, passando uma palavra-chave que será usada na criptografia.
2. Decifrar um texto, passando uma palavra-chave (que deve ser a mesma usada para a fase de cifração).
3. Cifrar / Decifrar usando um arquivo texto. Para essa opção, o texto deve estar nos arquivos cifrar.txt ou decifrar.txt, que são encontrados dentro do diretório
dados_entrada. No arquivo cifrar.txt deve conter um texto a ser cifrado. No decifrar.txt deve conter um texto a ser decifrado. Em ambas as opções será solicitada 
uma palavra-chave para realizar o processo. 
4. Ataque, essa opção ainda **não foi implementada.**
0. Finalizar o programa 

Observação: Os textos dentro dos arquivos cifrar.txt e decifrar.txt podem ser alterados em tempo de execução.

