from GerenciarCarteira import *

acoes = [{'ticker':'BBAS3', 'nomeEmpresa':'BANCO DO BRASIL','preco':32, 'quantidade':10},{'ticker':'ITUB4', 'nomeEmpresa':'ITAU UNIBANCO','preco':23, 'quantidade':20}, {'ticker':'BBAS4', 'nomeEmpresa':'BANCO DO BRASIL','preco':35, 'quantidade':30},]
totalGasto = [320, 460, 1050]
opc = -1

while (opc != 0):
    print('1- Inserir ação na Carteira:')
    print('2- Buscar ação:')
    print('3- Listar todas as ações:')
    print('4- Comprar mais unidades de uma ação:')
    print('5- Vender unidades de uma ação:')
    print('6- Exibir valor total gasto na compra de ações:')
    print('7- Verificar se houve lucro ou prejuízo:')
    print('8- Exibir lista de ações ordenadas:')
    print('9- Salvar em arquivo de texto a lista de ações:')
    print('0- Sair')
    print('--------------------------------')

    opc = int(input('Digite a opção desejada:'))

    if(opc == 1):
        NovaAcao = input('Digite o código da Ação:')
        achei = False
        for acao in acoes:
            if NovaAcao == acao["ticker"]:
                print('--------------------------------')
                print('Ação já cadastrada. '
                      '\nTente a opção 4 do menu para comprar novas ações da', NovaAcao)
                print('--------------------------------')
                achei = True

        if not achei:
            acoes.append(gerarAcaoDict(totalGasto, NovaAcao))

    elif(opc == 2):
        buscarAcao('ticker', acoes)

    elif(opc == 3):
        listar(acoes)

    elif(opc == 4):
        comprarAcoes(totalGasto,acoes)

    elif(opc == 5):
        venderAcao(acoes)

    elif(opc == 6):
        gastoTotal(totalGasto)

    elif (opc == 7):
        lucroPrejuizo(acoes)

    elif (opc == 8):
        acoesOrdenadas(acoes)

    elif (opc == 9):
        localSalvar = ('C:\\Users\\Jefferson\\Downloads\\PROJETO\\Arquivo.txt')
        salvarArquivo(localSalvar, acoes)

    else:
        print('--------------------------------')
        print('Opção inexistente. Tente novamente!')
        print('--------------------------------')