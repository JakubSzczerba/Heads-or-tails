# Orzeł i reszka

import time
import random

print('*** Symulacja rzutu monetą ***')

gracz = 0
computer = 0


while True:
    x = input('Wybierz r (reszka), albo o (orzeł): ')

    if x == '0':
        break
    elif x == 'r':
        x = 'reszka'
    elif x == 'o':
        x = 'orzeł'
    else:
        print('0 --> exit\nr --> reszka\no --> orzeł')
        continue

    y = random.choice(["orzeł", "reszka"])
    print('Moneta zostala rzucona')
    for i in range (1, 4):
        print(4 - i)
        time.sleep(1)

    print(f'Wynik: {y}')

    if y == x:
        gracz = gracz + 1

    else:
        computer = computer + 1

    print(f'Podsumowanie\nGracz: {gracz}\nKomputer: {computer}')

