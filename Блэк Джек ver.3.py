# Задача 8. Блек-джек.

# Костя так и не смог завязать с азартными играми. Но перед тем как в очередной раз всё проиграть, он решил как следует подготовиться. И написать программу, на которой он будет тренироваться играть в блек-джек.
# Блек-джек также известен как 21. Суть игры проста: нужно или набрать ровно 21 очко, или набрать очков больше, чем в руках у дилера, но ни в коем случае не больше 21. Если игрок собирает больше 21, он «сгорает». В случае ничьей игрок и дилер остаются при своих.
# Карты имеют такие «ценовые» значения:
# от двойки до десятки — от 2 до 10 соответственно;
# у туза — 1 или 11 (11 пока общая сумма не больше 21, далее 1);
# у «картинок» (король, дама, валет) — 10.
# Напишите программу, которая вначале случайным образом выдаёт пользователю и компьютеру по две карты и затем запрашивает у пользователя действие: взять карту или остановиться. На экран должна выдаваться информация о руке пользователя. После того как игрок останавливается, выведите на экран победителя.
# Представление карты реализуйте с помощью класса.
# Дополнительно: сделайте так, чтобы карты не могли повторяться.
# Ваши классы в этой задаче могут выглядеть так:

#class Card:
    #  Карта, у которой есть значения
    #   - масть
    #   - ранг/принадлежность 2, 3, 4, 5, 6, 7 и так далее
#class Deck:
    #  Колода создаёт у себя объекты карт
#class Player:
    #  Игрок, у которого есть имя и какие-то карты на руках

import random
from time import sleep

player_victory = 0
computer_victory = 0

n = 1

detect = {'6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 2, 'Q': 3, 'K': 4}

print('Игра "Блэк Джэк"\n')

while True:
    print(f'Раунд {n}-й\n')

    # Инициализация нового раунда
    player_cards = []
    player_sum = 0

    computer_cards = []
    computer_sum = 0

    cards = [(mast, numb) for mast in range(4) for numb in ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']]
    random.shuffle(cards)

    # Раздача карт
    player_cards.append(cards.pop())
    player_cards.append(cards.pop())
    for mast, numb in player_cards:
        if numb == 'A':
            if player_sum + 11 > 21:
                player_sum += 1
            else:
                player_sum += 11
        else:
            player_sum += detect[numb]

    computer_cards.append(cards.pop())
    computer_cards.append(cards.pop())
    for mast, numb in computer_cards:
        if numb == 'A':
            if computer_sum + 11 > 21:
                computer_sum += 1
            else:
                computer_sum += 11
        else:
            computer_sum += detect[numb]

    # Ход игрока
    while True:
        print('Ваши карты: ', end='')
        for mast, numb in player_cards:
            print(numb, ['червы', 'бубны', 'трефы', 'пики'][mast], end='; ')

        print(f'\nСумма очков: {player_sum}')

        if player_sum > 21:
            sleep(2)
            break

        cmd = input('Взять еще одну карту? (y/n) > ')
        if cmd == 'n' or cmd == 'N':
            break
        elif cmd == 'y' or cmd == 'Y':
            card = cards.pop()
            numb = card[1]
            player_cards.append(card)

            if numb == 'A':
                if player_sum + 11 > 21:
                    player_sum += 1
                else:
                    player_sum += 11
            else:
                player_sum += detect[numb]

        print()

    # Ход компьютера
    while True:
        if computer_sum + 5 <= 21:
            card = cards.pop()
            numb = card[1]
            computer_cards.append(card)
            if numb == 'A':
                if computer_sum + 11 > 21:
                    computer_sum += 1
                else:
                    computer_sum += 11
            else:
                computer_sum += detect[numb]
        else:
            break

    print('\nКарты компьютера: ', end='')
    for mast, numb in computer_cards:
        print(numb, ['червы', 'бубны', 'трефы', 'пики'][mast], end='; ')

    print(f'\nСумма очков компьютера: {computer_sum}')

    if (player_sum == computer_sum) or (computer_sum > 21 and player_sum > 21):
        print('\nНичья\n')
        n += 1
        sleep(4)
    elif player_sum > 21 or (player_sum < computer_sum and computer_sum < 22):
        print('\nВ этом раунде победил компьютер\n')
        computer_victory += 1
        n += 1
        sleep(4)
    else:
        print('\nВ этом раунде победил человек\n')
        player_victory += 1
        n += 1
        sleep(4)
    if player_victory == 3:
        print('\nУра! Вы победили!')
        break
    if computer_victory == 3:
        print('\nПобедил компьютер!')
        break
