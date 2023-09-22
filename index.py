import requests
import regex as re #Importando o pacote regex como 're'
from bs4 import BeautifulSoup

#Criando dicionários para verificar se determinadas palavras estão presentas no comentário
#Dicionário Positivo
palavras_positivas = {
    "bom" : 1,
    "ótimo" : 2,
    "excelente": 3,
    "maravilhoso": 3,
    "incrível": 3,
    "feliz": 2,
    "satisfeito": 2,
    "espetacular": 3,
    "amei": 2, 
    "filmaço" : 2,
    "indescritível": 3,
    "fantástico": 5,
    "épico": 3,
    "aclamado": 2,
    "melhor": 1,
    "surpreendente": 2,
    "deslumbrante": 3,
    "único": 2,
    "instigante": 2,
    "imperdível": 2,
    "encantado": 2,
    "fascinante": 2,
    "obra-prima": 5,
    "instigante": 2,
    "brilhante": 3,
    "melhores": 2,
    "adorável": 2,
    "mágico": 2,
    "hipnotizante": 3,
    "soberbo": 3,
    "inspirador": 2,
    "sublime": 3,
    "impressionante": 3,
    "extraordinário": 3,
    "imensurável": 3,
    "sofisticado": 2,
    "glorioso": 3,
    "incomparável": 3,
    "cativante": 2,
    "inigualável": 3,
    "envolvente": 2,
    "estupendo": 3,
    "radiante": 2,
    "celestial": 3,
    "deslumbrante": 3,
    "excelência": 3,
    "arrepiar": 2,
    "intenso": 2,
    "filmão": 2,
    "filmao": 2,
    "marcante": 2,
    "sensacional": 3,
    "foda": 3,
    "gostei": 1,
    "interessantíssimo": 3,
    "impecável": 2,
    "impecáveis": 3
}

#Dicionário Negativo
palavras_negativas = {
    "ruim": -1,
    "péssimo": -2,
    "horrível": -3,
    "terrível": -3,
    "desapontado": -2,
    "triste": -2,
    "frustrado": -2,
    "fracasso": -3,
    "odiei": -2,
    "bosta": -3,
    "lixo": -3,
    "decepcionado": -2,
    "merda": -2,
    "fraquíssimo": -2,
    "bizarro": -2,
    "não": -1,
    "ridículo": -2,
    "equivocado": -1,
    "arrastado": -1, 
    "confuso": -1,
    "inutil": -1,
    "desnecessário": -2,
    "falho": -1,
    "abominável": -3,
    "horrendo": -3,
    "miserável": -2,
    "detestável": -2,
    "desagradável": -2,
    "monstruoso": -3,
    "lamentável": -3,
    "terrível": -3,
    "desapontante": -2,
    "chato": -2,
    "desastroso": -3,
    "horrível": -3,
    "tedioso": -2,
    "medíocre": -2,
    "ridículo": -2,
    "confuso": -2,
    "agonizante": -3,
    "péssimo": -3,
    "cansativo": -2,
    "fracassado": -2,
    "insatisfatório": -2,
    "desgostoso": -2,
    "irritante": -2,
    "fiasco": -3,
    "enganador": -2,
    "insosso": -2,
    "atroz": -3,
    "superestimado": -2,
    "horrivel": -2,
    "piorando": -1,
    "pífeo": -2
}

# Frases negativas
frases_negativas = [
    r'Não gostei',
    r'Achei fraco',
    r'Não recomendo',
    r'Esperava mais',
    r'Perda de tempo',
    r'Muito parado',
    r'Enrola muito',
    r'Não vale a pena', 
    r'Decepção total',
    r'Esperava muito mais deste filme, mas me decepcionou',
    r'Uma experiência terrível que me fez perder tempo',
    r'O roteiro é um verdadeiro desastre, não recomendo',
    r'Frustrado com a falta de originalidade deste filme',
    r'Uma produção tão ruim que não vale a pena assistir',
    r'Triste em ver como este filme é medíocre',
    r'Um verdadeiro fiasco do início ao fim',
    r'Decepcionante em todos os aspectos, não gostei',
    r'Um filme confuso e arrastado que me deixou entediado',
    r'Uma obra cinematográfica lamentável, não recomendo'
]

# Frases positivas
frases_positivas = [
    r'Obra prima',
    r'O melhor filme',
    r'Colírio para meus olhos',
    r'Me emocionei',
    r'Muito bom',
    r'Bem produzido',
    r'Sem palavras',
    r'Um dos melhores filmes',
    r'Me surpreendi',
    r'Uma experiência cinematográfica incrível que todos devem assistir',
    r'Este filme é uma verdadeira obra-prima da sétima arte',
    r'Fiquei hipnotizado pela atuação dos atores',
    r'A trilha sonora é simplesmente magnífica',
    r'Um filme tão bom que me deixou sem palavras',
    r'Épico em todos os sentidos, uma joia rara do cinema',
    r'Um dos melhores filmes que já tive o prazer de assistir',
    r'Esta produção é uma pérola entre as películas',
    r'A cinematografia deste filme é deslumbrante',
    r'Uma história fascinante que cativou meu coração'
]

class AdoroCinema:

    def extrairSinopseFilme (self, filme):      
        url = "https://www.adorocinema.com/filmes/" + filme +'/'
        htmlFilme = requests.get(url).text
        bsS = BeautifulSoup(htmlFilme, 'html.parser')
        sinopse = bsS.find('div', class_="content-txt").get_text(strip=True)
        return sinopse
    
    def salvarSinopseFilme(self, filme, sinopse):
        arq_saida = open(filme+'_sinopse.txt', 'w',encoding='utf-8')
        for line in sinopse:
            arq_saida.write(line)
        arq_saida.close()

    def extrairComentariosFilme(self, filme, n):
        comentarios = []
        for i in range(1,n+1):
            url = 'http://www.adorocinema.com/filmes/' + filme + '/criticas/espectadores/?page=' + str(i)
            htmlComentarios = requests.get(url).text
            bsC = BeautifulSoup(htmlComentarios, 'html.parser')
            comentarios_com_tags = bsC.find_all('div', class_="content-txt review-card-content")
            for comentario_com_tag in comentarios_com_tags:
                comentarios.append(comentario_com_tag.get_text().strip())
        return comentarios

    def salvarComentariosFilme(self, filme, comentarios):
        arq_saida = open(filme+'_comentarios.txt', 'w', encoding='utf-8')
        for comentario in comentarios:
            arq_saida.write(comentario + '\n') #Retirando um \n para remover os espaços entre os comentários
        arq_saida.close()

    #Ideia principal
    # Fazer um for que percorra todos os comentários (linha por linha) e verifique se ele possui a palavra em questão do dicionário
    # Fazer 2 dicionários, um com palavras posivitas e negativas (a fim de realizar a analise de sentimento)
    # Dado o comentário em questão, percorrer os dois dicionários e contabilizar as palavras positivas e negativas (somadores)
    # Caso o somador positivo seja maior, o comentário é positivo, se o negativo for maior, o comentário é negativo, senão é neutro
    # Armazenar os comentários positivos em uma lista e os negativos em outra
    # Printar as duas listas e a quantidade de comentários positivos/negativos obtidos

    #Função para ler arquivo
    def lerArquivo(self, filme):
        listaLinhas = []
        arquivo = open(filme + '_comentarios.txt', "r", encoding="utf-8") #Comando para formatar o arquivo.txt em utf-8 (padrão dos caracteres)
        lines = arquivo.readlines()

        for line in lines:
            listaLinhas.append(line.strip()) #removendo o \n
            
        arquivo.close()

        return listaLinhas


    # def calcular_sentimento(self, comentario):
    #     soma_sentimento = 0
    
    #     #Verificando as frases negativas
    #     for frase in frases_negativas:
    #         if re.search(frase, comentario, re.IGNORECASE):
    #             print(f"Frase negativa encontrada: {frase}")
    #             soma_sentimento -= 1
    #             for palavra, pontuacao in palavras_negativas.items():
    #                 if re.search(r'\b' + re.escape(palavra) + r'\b', comentario, re.IGNORECASE):
    #                     print(f"Palavra negativa encontrada: {palavra}")
    #                     soma_sentimento += pontuacao

    #     #Verificando as frases positivas
    #     for frase in frases_positivas:
    #         if re.search(frase, comentario, re.IGNORECASE): #Verificando se o comentário possui tal frase, ignorando o case sensitive
    #             print(f"Frase positiva encontrada: {frase}")
    #             soma_sentimento += 1
    #             for palavra, pontuacao in palavras_positivas.items(): #Iterando sobre o meu dicionário (objeto com chave-valor)
    #                 if re.search(r'\b' + re.escape(palavra) + r'\b', comentario, re.IGNORECASE):
    #                     print(f"Palavra positiva encontrada: {palavra}")
    #                     soma_sentimento += pontuacao
    #                     print(f"pontuação -> {pontuacao}")
            
    #     #Verificando as palavras positivas
    #     for palavra in palavras_positivas.keys():
    #         padrao = r'\b' + re.escape(palavra) + r'\b'
    #         ocorrencias = len(re.findall(padrao, comentario, re.IGNORECASE))
    #         soma_sentimento += ocorrencias * palavras_positivas[palavra]

    #     #Verificando as palavras negativas
    #     for palavra in palavras_negativas.keys():
    #         padrao = r'\b' + re.escape(palavra) + r'\b'
    #         ocorrencias = len(re.findall(padrao, comentario, re.IGNORECASE))
    #         soma_sentimento += ocorrencias * palavras_negativas[palavra]

    #     return soma_sentimento

    def calcular_sentimento(self, comentario):
        soma_sentimento = 0

        # Verificando as frases negativas
        for frase in frases_negativas:
            if re.search(frase, comentario, re.IGNORECASE):
                soma_sentimento -= 1

        # Verificando as frases positivas
        for frase in frases_positivas:
            if re.search(frase, comentario, re.IGNORECASE):
                soma_sentimento += 1

        # Verificando as palavras positivas
        for palavra, pontuacao in palavras_positivas.items():
            padrao = r'\b' + re.escape(palavra) + r'\b'
            ocorrencias = len(re.findall(padrao, comentario, re.IGNORECASE))
            soma_sentimento += ocorrencias * pontuacao

        # Verificando as palavras negativas
        for palavra, pontuacao in palavras_negativas.items():
            padrao = r'\b' + re.escape(palavra) + r'\b'
            ocorrencias = len(re.findall(padrao, comentario, re.IGNORECASE))
            soma_sentimento += ocorrencias * pontuacao

        return soma_sentimento
    
    def calcular_sentimento_lista(self, comentarios):
        sentimentos = []
        
        for comentario in comentarios:
            sentimento = crawler.calcular_sentimento(comentario)
            sentimentos.append(sentimento)

        return sentimentos
    
    def gerarArquivoFinal(self, listaResultado):
        print(listaResultado)


filme = input('Digite o código do filme, conforme listado na barra de endereço do site https://www.adorocinema.com/: ')
n = int(input('Digite quantas páginas de comentários você deseja consultar: '))
crawler = AdoroCinema()
sinopse = crawler.extrairSinopseFilme(filme)
crawler.salvarSinopseFilme(filme, sinopse)
comentarios = crawler.extrairComentariosFilme(filme, n)
crawler.salvarComentariosFilme(filme, comentarios)
print('Programa executado com sucesso. Consulte os arquivos gerados com a sinopse e os comentários do filme.')

print('-----------------------------------------------------------------------------------------------------------------')

listaResultado = []
listaComentarios = crawler.lerArquivo(filme)

sentimentos = crawler.calcular_sentimento_lista(listaComentarios)

total = len(listaComentarios)
totalPositivos = 0
totalNegativos = 0
totalNeutros = 0

for i, sentimento in enumerate(sentimentos):
    comentario = listaComentarios[i]
    if sentimento > 0:
        print(f"Comentário {i + 1}: {comentario} - Comentário positivo\n")
        listaResultado.append(f"Comentário {i + 1}: {comentario} - Comentário positivo\n")
        totalPositivos += 1
    elif sentimento < 0:
        print(f"Comentário {i + 1}: {comentario} - Comentário negativo\n")
        listaResultado.append(f"Comentário {i + 1}: {comentario} - Comentário negativo\n")
        totalNegativos += 1
    else:
        print(f"Comentário {i + 1}: {comentario} - Comentário neutro\n")
        listaResultado.append(f"Comentário {i + 1}: {comentario} - Comentário neutro\n")
        totalNeutros += 1
    
print(f"O total de comentários lido foi de: {i + 1} comentário(s).")
print(f"Percentual de comentários positivos -> {(totalPositivos / total) * 100}")
print(f"Percentual de comentários negativos -> {(totalNegativos / total) * 100}")
print(f"Percentual de comentários neutros -> {(totalNeutros / total) * 100}")

crawler.gerarArquivoFinal(listaResultado)


