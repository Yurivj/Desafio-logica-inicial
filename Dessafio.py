nome = input("Digite o seu nome: ")
xp_heroi = input("Digite a sua quantidade de experiência: ")

nivel = ""

if xp_heroi < 1000:
    nivel = 'Ferro'
    print(f'Seu nome é {nome} e seu nível é {nivel}')
if 1.001 <= xp_heroi < 2.000:
    nivel = 'Bronze'
    print(f'Seu nome é {nome} e seu nível é {nivel}')
if 2.001 <= xp_heroi <= 5.000:
    nivel = 'Prata'
    print(f'Seu nome é {nome} e seu nível é {nivel}')
if 6.001 <= xp_heroi <= 7.000:
    nivel = 'Ouro'
    print(f'Seu nome é {nome} e seu nível é {nivel}')
if 7.001 <= xp_heroi <= 8.000:
    nivel = 'Platina'
    print(f'Seu nome é {nome} e seu nível é {nivel}')
if 8.001 <= xp_heroi <= 9.000:
    nivel = 'Ascendente'
    print(f'Seu nome é {nome} e seu nível é {nivel}')
if 9.001 <= xp_heroi < 10.000:
    nivel = 'Imortal'
    print(f'Seu nome é {nome} e seu nível é {nivel}')
if xp_heroi >= 10.001:
    nivel = 'Radiante'
    print(f'Seu nome é {nome} e seu nível é {nivel}')