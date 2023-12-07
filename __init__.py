def gerarAcaoDict(totalGasto, NovaAcao):
    novaAcao = dict()
    novaAcao['ticker'] = NovaAcao
    novaAcao['nomeEmpresa'] = input('Digite o nome da empresa:')
    novaAcao['preco'] = float(input('Digite o preço unitário da ação:'))
    novaAcao['quantidade'] = int(input('Digite a quantidade:'))
    novaAcao['valorGasto'] = novaAcao['preco'] * novaAcao['quantidade']
    totalGasto.append(novaAcao['valorGasto'])
    print('--------------------------------')
    print('Ação cadastrada com sucesso!')
    print('--------------------------------')
    return novaAcao

def buscarAcao(campo, acoes):
    busca = input('Digite o ticker da ação:')
    print('--------------------------------')
    achei = False
    for i in range(0, len(acoes)):
        if (busca in acoes[i][campo]):
            print(f'ID: {i}'
                  f'\nNome/ticker:{acoes[i]["ticker"]}'
                  f'\nNome da Empresa: {acoes[i]["nomeEmpresa"]}'
                  f'\nPreço: {acoes[i]["preco"]}'
                  f'\nQuantidade: {acoes[i]["quantidade"]}')
            achei = True
            print('--------------------------------')
    if (not achei):
        print('Ação não encontrada!')
        print('--------------------------------')

def listar(acoes):
    print('--------------------------------')
    for i in range(0, len(acoes)):
        print(f'ID: {i}'
              f'\nNome/ticker:{acoes[i]["ticker"]}'
              f'\nNome da Empresa: {acoes[i]["nomeEmpresa"]}'
              f'\nPreço: {acoes[i]["preco"]}'
              f'\nQuantidade: {acoes[i]["quantidade"]}')
        print('--------------------------------')

def comprarAcoes(totalGasto, acoes):
    busca = input('Digite o ticker da ação:')
    print('--------------------------------')
    achei = False
    opcoes = set()
    for i in range(0, len(acoes)):
        if (busca in acoes[i]['ticker']):
            print(f'ID: {i} Nome:{acoes[i]["ticker"]}')
            achei = True
            opcoes.add(i)
    if achei:
        print('--------------------------------')
        idAcao = int(input('Digite o ID da ação:'))
        while idAcao not in opcoes:
            print('ID da ação não listado. Tente novamente.')
            idAcao = int(input('Digite o ID da ação:'))
        precoCompra = float(input('Digite o preço unitário da ação:'))
        quantidadeCompra = int(input('Digite a quantidade de ações compradas:'))
        acoes[idAcao]['preco'] = ((acoes[idAcao]['preco'] * acoes[idAcao]['quantidade']) + (
                precoCompra * quantidadeCompra)) / (acoes[idAcao]['quantidade'] + quantidadeCompra)
        acoes[idAcao]['quantidade'] += quantidadeCompra
        print('--------------------------------')
        print('Compra de ações registrada!')
        totalGasto.append(precoCompra * quantidadeCompra)
        print('--------------------------------')
    else:
        print('Ação não encontrada. Cadastre ação!')
        print('--------------------------------')
    opcoes.clear()
    return achei

def venderAcao(acoes):
    busca = input('Digite o ticker da ação que será vendida:')
    print('--------------------------------')
    achei = False
    opcoes = set()
    for i in range(0, len(acoes)):
        if (busca in acoes[i]['ticker']):
            print(f'ID: {i} Nome:{acoes[i]["ticker"]}')
            achei = True
            opcoes.add(i)
    if achei:
        print('--------------------------------')
        idAcao = int(input('Digite o ID da ação:'))
        while idAcao not in opcoes:
            print('ID da ação não listado. Tente novamente.')
            idAcao = int(input('Digite o ID da ação:'))
        precoVenda = float(input('Digite o preço unitário de venda da ação:'))
        quantidadeVenda = int(input('Digite a quantidade de ações vendidas:'))
        while quantidadeVenda > acoes[idAcao]['quantidade']:
            print(f'Você tem apenas', acoes[idAcao]['quantidade'], 'disponíveis para vemda')
            quantidadeVenda = int(input('Digite a quantidade de ações vendidas:'))
        acoes[idAcao]['quantidade'] -= quantidadeVenda
        print('--------------------------------')
        print('Venda de ações registrada!')
        print('--------------------------------')
        print(f'Nome/ticker:{acoes[idAcao]["ticker"]}',
              f'\nNome da Empresa: {acoes[idAcao]["nomeEmpresa"]}',
              f'\nPreço Médio: {acoes[idAcao]["preco"]}',
              f'\nQuantidade: {acoes[idAcao]["quantidade"]}')
        if precoVenda > acoes[idAcao]["preco"]:
            print(f'Lucro por ação: R$', (precoVenda - acoes[idAcao]["preco"]),
                  f'\nLucro total da venda: R$',(precoVenda - acoes[idAcao]["preco"])*quantidadeVenda)
        elif precoVenda < acoes[idAcao]["preco"]:
            print(f'Prejuizo por ação: R$',(precoVenda - acoes[idAcao]["preco"]) * -1,
                  f'\nPrejuizo total da venda: R$',(precoVenda - acoes[idAcao]["preco"])*quantidadeVenda * -1)
        print('--------------------------------')
        opcoes.clear()
    else:
        print('Ação não encontrada!')
        print('--------------------------------')

def gastoTotal(totalGasto):
    print('--------------------------------')
    print(F'O total gasto na compra de Ações é: ', sum(totalGasto))
    print('--------------------------------')

def lucroPrejuizo(acoes):
    busca = input('Digite o ticker da ação:')
    print('--------------------------------')
    achei = False
    opcoes = set()
    for i in range(0, len(acoes)):
        if (busca in acoes[i]['ticker']):
            print(f'ID: {i} Nome:{acoes[i]["ticker"]}')
            achei = True
            opcoes.add(i)
    if achei:
        print('--------------------------------')
        idAcao = int(input('Digite o ID da ação:'))
        while idAcao not in opcoes:
            print('ID da ação não listado. Tente novamente.')
            idAcao = int(input('Digite o ID da ação:'))
        precoAtual = int(input('Digite o preço atual de mercado da Ação:'))
        resultado = precoAtual - acoes[idAcao]['preco']
        print('--------------------------------')
        if resultado > 0:
            print(f'LUCRO REGISTRADO EM', acoes[idAcao]['ticker'],
                  f'\nLUCRO POR AÇÃO: R$', resultado,
                  '\nLUCRO TOTAL: R$',resultado*acoes[idAcao]['quantidade'])
            print('--------------------------------')
        elif resultado < 0:
            print(f'PREJUIZO REGISTRADO EM', acoes[idAcao]['ticker'],
                  f'\nPREJUÍZO POR AÇÃO: R$', resultado,
                  '\nPREJUÍZO TOTAL: R$', resultado * acoes[idAcao]['quantidade'])
            print('--------------------------------')
        else:
            print(f'Não houve lucro ou prejuízo!')
    else:
        print('Ação não encontrada!')
        print('--------------------------------')
        opcoes.clear()

def acoesOrdenadas(acoes):
    copiaAcoes = acoes[:]
    print('--------------------------------')
    for i in range(0, len(acoes) - 1):
        for j in range(i+1, len(acoes)):
            if copiaAcoes[i]['preco'] * copiaAcoes[i]['quantidade'] < copiaAcoes[j]['preco'] * copiaAcoes[j]['quantidade']:
                aux = copiaAcoes[i]
                copiaAcoes[i] = copiaAcoes[j]
                copiaAcoes[j] = aux
    for acao in copiaAcoes:
        print(
            f'Nome/ticker:{acao["ticker"]}'
            f'\nPeso:{acao["preco"]*acao["quantidade"]}'
            f'\nNome da Empresa: {acao["nomeEmpresa"]}'
            f'\nPreço: {acao["preco"]}'
            f'\nQuantidade: {acao["quantidade"]}')
        print('--------------------------------')

def salvarArquivo(localSalvar, acoes):
    Arquivo = open(localSalvar, 'w')
    for i in range(0, len(acoes)):
        texto=(f'\nID: {i}'
              f'\nNome/ticker:{acoes[i]["ticker"]}'
              f'\nNome da Empresa: {acoes[i]["nomeEmpresa"]}'
              f'\nPreço: {acoes[i]["preco"]}'
              f'\nQuantidade: {acoes[i]["quantidade"]}'
              f'\n--------------------------------')
        Arquivo.write(texto)
    Arquivo.close()
    print('--------------------------------')
    print('Arquivo salvo com sucesso!')
    print('--------------------------------')