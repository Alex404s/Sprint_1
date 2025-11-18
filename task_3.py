world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}

world_champions[2022] = 'Аргентина'

for champion in world_champions:
    print(champion, '-', world_champions[champion])

country = 'Италия'
is_italy_win = False

for winners in world_champions.values():
    if winners == country:
        is_italy_win = True
        print('Италия cтановилась чемпионом мира по футболу в 21 веке!')

if is_italy_win == False:
    print('Италия не выигрывала чемпионат мира по футболу в 21 веке.')
