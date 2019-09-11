# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do CAMPEONATO BRASILEIRO DE FUTEBOL, na ordem de
# colocação. Depois mostre:

# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ORDEM ALFÁBETICA.
# D) Em que posição na tabela está o time da CHAPECOENSE.

times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético-MG', 'Athletico-PR', 'Cruzeiro',
         'Botafogo', 'Santos', 'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará', 'Vasco', 'Sport',
         'América-MG', 'Vitória', 'Paraná')
print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[16:20]}')
print(f'-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O Chapecoense está na posição {times.index("Chapecoense") + 1}.')


