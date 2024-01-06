nome = 'Yuri'
xp_heroi = 8000

nivel = ""

if xp_heroi <= 1000:
    nivel = 'Ferro'
    print(f'Seu nome é {nome} e seu nível é {nivel}')
if 1001 <= xp_heroi <= 2000:
    nivel = 'Bronze'
    print(f'Seu nome é {nome} e seu nível é {nivel}')
if 2001 <= xp_heroi <= 6000:
    nivel = 'Prata'
    print(f'Seu nome é {nome} e seu nível é {nivel}')
if 6001 <= xp_heroi <= 7000:
    nivel = 'Ouro'
    print(f'Seu nome é {nome} e seu nível é {nivel}')
if 7001 <= xp_heroi <= 8000:
    nivel = 'Platina'
    print(f'Seu nome é {nome} e seu nível é {nivel}')
if 8001 <= xp_heroi <= 9000:
    nivel = 'Ascendente'
    print(f'Seu nome é {nome} e seu nível é {nivel}')
if 9001 <= xp_heroi <= 10000:
    nivel = 'Imortal'
    print(f'Seu nome é {nome} e seu nível é {nivel}')
if xp_heroi >= 10001:
    nivel = 'Radiante'
    print(f'Seu nome é {nome} e seu nível é {nivel}')