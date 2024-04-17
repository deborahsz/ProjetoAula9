import array

#Cria um vetor com 10 posições
vetor = array.array('i', [] * 10)
#Cria um vetor vazio para armazenas possíveis números repetidos
repetidos = []

#For loop para pedir um número 10 vezes
for i in range(0, 10):
    vetor.append(int(input("Informe um número: ")))

#Varre o vetor 10 vezes (tamanho do vetor)
for i in range(len(vetor)):
    #Cada varredura no vetor, compara com o proximo número para verificar se existe igual
    for j in range(i + 1, len(vetor)):
        #Verifica se o valor dos indices buscados são iguais
        if vetor[i] == vetor[j]: #true
            #Em caso positivo, adidiona o número repetido no vetor 'repetidos'.
            repetidos.append(vetor[i])


if len(repetidos) > 0: #Caso o vetor 'repetidos' seja maior que zero, significa que temos números repetidos, nesse caso printamos na tela a mensagem que foram encontrados numeros repetidos e quais são eles em seguida.
    print("Foram encontrados números repetidos, segue a lista: ")
    print(repetidos)
else: #Caso contrario, informamos que não existem numeros repetidos
    print("Não foram encontrados números repetidos.")

