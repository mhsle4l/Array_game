import vetores

sair = False
v = []
while not sair:
    print('\n# MENU PRINCIPAL')
    print('\n(1) Gerar o vetor')
    print('(2) Gerar o vetor ordenado')
    print('(3) Verificar se elemento está no vetor')
    print('(4) Somar elementos do vetor')
    print('(5) Calcular a média dos elementos do vetor')
    print('(6) Obter o maior valor')
    print('(7) Obter o menor valor')
    print('(8) Verificar se vetor está ordenado')
    print('(0) Sair')

    op = input('# Escolha uma opção: ')

    if op == '1':
        v = vetores.gerar(8)
        print('\n# Vetor gerado:', v)
    elif op == '2':
        v = vetores.gerar_ord(8)
        print('\n# Vetor ordenado gerado:', v)
    elif op == '3':
        elemento = input('# Escolha o elemento:')
        resposta = vetores.contem(v, elemento)
        print('\n', resposta)
    elif op == '4':
        soma = vetores.somar(v)
        print('A soma do Vetor é:', soma)
    elif op == '5':
        media_aritimetica = vetores.media(v)
        print('A média do Vetor é:', media_aritimetica)
    elif op == '6':
        maior_numero = vetores.maior(v)
        print('A média do Vetor é:', maior_numero)
    elif op == '7':
        menor_numero = (v)
        print('A média do Vetor é:', menor_numero)
    elif op == '8':
        if vetores.ordenado(v) == True:
            print('Está em ordem')
        else:
            print('Não está em ordem')
    elif op == '0':
        sair = True
    else:
        print('\n# Opção inválida!')

print('\n#Fim!')