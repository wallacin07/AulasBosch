'''arquivo = open('arquivo.txt', 'r')
palavra_user = input('Escolha uma palavra para ver se tem ela no roteiro -- ')
count = 0
for palavra in arquivo:
    palavra = palavra.strip()
    palavra = palavra.split(' ')
    for i in palavra:
        if i  == palavra_user:
            count +=1

print(f"A palavra {palavra_user} aparece {count} vezes")'''
r = open('dadosfinais.txt', 'w')
f = open('dados.txt', 'r')
preresultado = f.read()
infgeral = preresultado.split('\n')
print(infgeral)
infalunos = []
for i in infgeral:
    infalunos = i.split(', ')
    print(infalunos)
    media = 0
    soma = 0
    maiormedia = 0
    alunonotaalta = ""
    for i in infalunos:
        if i.isdigit():
            soma += int(i)  
            
    media = soma/3
    ''' deu errado
     
       if maiormedia < media:
        maiormedia = media
        alunonotaalta = infalunos[0]'''
    if media > 6:
        resultado = 'Aprovado!'
        round(media, 2)
        r.write(f'Aluno {infalunos[0]} : Media {media:.2} Resultado : {resultado} \n') 
    else:
        resultado = 'Reprovado!'
        r.write(f'Aluno {infalunos[0]} : Media {media:.2} Resultado : {resultado} \n') 
r.write(f'A maior media foi de {maiormedia} de {alunonotaalta}') 
r.close()


