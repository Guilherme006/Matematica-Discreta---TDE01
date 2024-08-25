# Guilherme Felippe Lazari

# O programa que você desenvolverá irá receber como entrada um arquivo de texto (.txt) 
# contendo vários conjuntos de dados e várias operações. Estas operações e dados estarão representadas 
# em um arquivo de textos contendo apenas os dados referentes as operações que devem ser realizadas 
# segundo a seguinte regra fixa: a primeira linha do arquivo de texto de entrada conterá o número de 
# operações que estão descritas no arquivo, este número de operações será um inteiro; as linhas 
# seguintes seguirão sempre o mesmo padrão de três linhas: a primeira linha apresenta o código da 
# operação (U para união, I para interseção, D para diferença e C produto cartesiano), a segunda e 
# terceira linhas conterão os elementos dos conjuntos separados por virgulas.

def ConjuntoOperacoes(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

    numero_operacoes = int(linhas[0].strip())
    inicio = 1
    resultados = []

    for _ in range(numero_operacoes):
        operacao = linhas[inicio].strip()
        conjunto_01 = set(linhas[inicio + 1].strip().split(', '))
        conjunto_02 = set(linhas[inicio + 2].strip().split(', '))
        
        if operacao == 'U':
            resultado = conjunto_01.union(conjunto_02)
            nome_conjunto = "União"
        elif operacao == 'I':
            resultado = conjunto_01.intersection(conjunto_02)
            nome_conjunto = "Interseção"
        elif operacao == 'D':
            resultado = conjunto_01.difference(conjunto_02)
            nome_conjunto = "Diferença"
        elif operacao == 'C':
            resultado = {(a, b) for a in conjunto_01 for b in conjunto_02}
            nome_conjunto = "Produto Cartesiano"
        
        if operacao == 'I' and not resultado:
            resultado_conjuntos = '∅'
        elif operacao != 'C':
            resultado_conjuntos = ', '.join(sorted(resultado))
        else:
            resultado_conjuntos = ', '.join(str(elemento) for elemento in sorted(resultado))
        
        resultados.append(f"{nome_conjunto}: conjunto 1 {{{', '.join(sorted(conjunto_01))}}}, conjunto 2 {{{', '.join(sorted(conjunto_02))}}}. Resultado: {{{resultado_conjuntos}}}\n")

        inicio += 3

    for resultado in resultados:
        print(resultado)

# Coloque o nome do arquivo que quer ler aqui
ConjuntoOperacoes('arquivo_03.TXT')
