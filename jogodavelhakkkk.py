import random

dic = {'a':'a', 'b':'b', 'c':'c', 'd':'d', 'e':'e', 'f':'f', 'g':'g', 'h':'h', 'i':'i'}
escolhas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

computador = 'o'
jogador = 'x'

for c in escolhas:
    escolha_computador = random.choice(escolhas)
    dic[escolha_computador] = computador

    escolha_jogador = input('Escolha: ')
    dic[escolha_jogador] = jogador

    print(f"{dic['a']} | {dic['b']} | {dic['c']}")
    print(f"--+---+---")
    print(f"{dic['d']} | {dic['e']} | {dic['f']}")
    print("--+---+---")
    print(f"{dic['g']} | {dic['h']} | {dic['i']}")
    
    escolhas.remove(escolha_computador)
    escolhas.remove(escolha_jogador)
