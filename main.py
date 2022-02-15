# Código criado por @jimitogni e adaptado por @jonnybcw
# Disponível em: https://github.com/jimitogni/genetic_algorithm

import random

print("Modelo de entrada:")
print("a b c d e f g h i ... j")
print("Digite seu modelo:")
modelo_entrada = input()
# split() retorna uma lista com as palavras da string
# e em seguida converte para inteiro
modelo = [int(i) for i in modelo_entrada.split()]
print("\n")
print("Modelo: {}".format(modelo))
print("\n")
tam_individuo = len(modelo)
tam_populacao = 10
pais = 2
prob_mutacao = 0.5


def individuo(min, max):
    # gera um int aleatório dentro da faixa especificada para cada atributo do indivíduo
    return [random.randint(min, max) for _ in range(tam_individuo)]


def criar_populacao():
    # gera a lista de indivíduos de acordo com o tamanho da população
    return [individuo(0, 9) for _ in range(tam_populacao)]


def funcao_fitness(individuo):
    fitness = 0
    # verifica se cada atributo do indivíduo corresponde ao modelo
    for i in range(len(individuo)):
        if individuo[i] == modelo[i]:
            # caso afirmativo, incrementa a variável fitness
            fitness += 1
    return fitness


def selecao_e_reproducao(populacao):
    # calcula o valor fitness de cada indivíduo
    pontuados = [(funcao_fitness(i), i) for i in populacao]
    # sorted() -> retorna a lista ordenada
    # e em seguida pega o elemento na posição 1 de cada item
    pontuados = [i[1] for i in sorted(pontuados)]
    populacao = pontuados

    # pega apenas os indivíduos no final da lista
    selecionados = pontuados[(len(pontuados) - pais):]

    for i in range(len(populacao) - pais):
        # escolhe um dos atributos do indivíduo aleatoriamente
        ponto = random.randint(1, tam_individuo - 1)
        # escolhe aleatoriamente 2 itens da lista
        pai = random.sample(selecionados, 2)

        # mescla as características do indivíduo i com o indivíduo pai selecionado
        populacao[i][:ponto] = pai[0][:ponto]
        populacao[i][ponto:] = pai[1][ponto:]

    return populacao


def mutacao(populacao):
    # percorre toda a população (menos os pais)
    for i in range(len(populacao) - pais):
        # gera um valor entre 0 e 1 e
        # verifica se é menor que a probabilidade de mutação
        if random.random() <= prob_mutacao:
            # escolhe um dos atributos do indivíduo aleatoriamente
            ponto = random.randint(0, tam_individuo - 1)
            # gera um novo valor para esse atributo (entre 1 e 9)
            novo_valor = random.randint(1, 9)

            while novo_valor == populacao[i][ponto]:
                # se o novo valor for igual ao valor atual, gera outro
                novo_valor = random.randint(1, 9)

            # atribui esse novo valor para o atributo do indivíduo
            populacao[i][ponto] = novo_valor

    return populacao


populacao = criar_populacao()
print("População Inicial: {}".format(populacao))
execucoes = 100
for i in range(execucoes):
    populacao = selecao_e_reproducao(populacao)
    populacao = mutacao(populacao)
print('O algoritmo de evolução foi executado %i vezes' % (execucoes - 1))
print("População Final: {}".format(populacao))
