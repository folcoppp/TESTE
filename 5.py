string = input("Digite a string a ser invertida: ")  # lê a string a ser invertida
inverted_string = ""  # define uma string vazia que irá armazenar a string invertida

# percorre a string de trás para frente e adiciona cada caractere na string invertida
for i in range(len(string)-1, -1, -1):
    inverted_string += string[i]

print("A string invertida é:", inverted_string)  # imprime a string invertida
