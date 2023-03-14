# Игра Блек-джек.

# Блек-джек также известен как 21. Суть игры проста: нужно или набрать ровно 21 очко, или набрать очков больше, чем в руках у дилера, но ни в коем случае не больше 21. 
# Если игрок собирает больше 21, он «сгорает». В случае ничьей игрок и дилер остаются при своих.
# Карты имеют такие «ценовые» значения: от двойки до десятки — от 2 до 10 соответственно, у туза — 1 или 11 (11 пока общая сумма не больше 21, далее 1), у короля, дамы, вальта — 10.
# Программа вначале случайным образом выдаёт пользователю и компьютеру по две карты и затем запрашивает у пользователя действие: взять карту или остановиться. 
# На экран выводится информация о картах пользователя. После того как игрок останавливается, выводится победитель.

#class Card:
    #  Карта, у которой есть значения
    #   - масть
    #   - ранг/принадлежность 2, 3, 4, 5, 6, 7 и так далее
#class Deck:
    #  Колода создаёт у себя объекты карт
#class Player:
    #  Игрок, у которого есть имя и какие-то карты на руках

import random

class Card:  # класс карт
    # статические атрибуты карт
    suits = ['пики', 'трефы', 'бубны', 'червы']  # масть
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']  # ранг

    def __init__(self, suit, rank):  # конструктор класса карт
        self.suit = suit
        self.rank = rank

    def card_info(self):  # метод вывода информации о карте
        print(self.rank + ': ' + self.suit)

class Deck:  # класс колоды карт
    def __init__(self):  # генерируем список колоды карт
        self.cards = [(suit, rank) for suit in Card.suits for rank in Card.ranks]

    def shuffle(self):  # метод перемешивания карт в случайном порядке
        random.shuffle(self.cards)

    def deck_info(self):
        for card in self.cards:
            print(card[1] + ': ' + card[0])

class Player:  # метод игрока
    score = 0  # очки игрока

    def __init__(self, name):  # конструктор класса игрока
        self.name = name  # имя игрока
        self.own_cards = []  # карты игрока
        self.score = 0  # очки игрока

    def player_info(self): # метолы вывода информации о кол-ве побед игрока
        print(f'У {self.name} {self.score} побед')

    def own_cards_info(self): # метод вывода информации о картах игрока
        print(f'\nУ {self.name} карты: ')
        for own_card in self.own_cards:
            print(own_card[0] + ': ' + own_card[1])

    def cards_count(self):
        count = 0
        for own_card in self.own_cards:
            if not own_card[1].isdigit():
                if own_card[1] == 'A' and count < 10:
                    count += 11
                elif own_card[1] == 'A' and count > 10:
                    count += 1
                else:
                    count += 10
            else:
                count += int(own_card[1])
        return count

    def cards_count_info(self):
        print(f'У {self.name} количество очков {self.cards_count()}:')

    def score_up(self):
        self.score += 1
        print(f'\n{self.name} ВЫЙГРАЛ!')


BJ_deck = Deck()
BJ_deck.shuffle()

player_1 = Player(input('1 игрок, введите свое имя: '))
player_2 = Player(input('2 игрок, введите свое имя: '))

while True: # запускаем бесконечный цикл игры
    rep = input('\nГотовы играть в БлэкДжэк? y/n: ')
    if rep == 'n':
        player_1.player_info() # вывод информации о 1 игроке
        player_2.player_info() # вывод информации о 2 игроке
        break
    elif rep == 'y':
        # создание новой перетусованной колоды
        if len(BJ_deck.cards) < 20: # если кол-во карт колоды менее 20
            New_BJ_deck = Deck()
            New_BJ_deck.shuffle()
            BJ_deck = New_BJ_deck

        # создание пустых списков карт у игроков
        player_1.own_cards = []
        player_2.own_cards = []

        player_1.own_cards.append(BJ_deck.cards.pop()) # 2 раза добавление последней удаленной карты из колоды карт в список карт 1 игрока
        player_1.own_cards.append(BJ_deck.cards.pop())
        player_1.own_cards_info() # информация о картах 1 игрока
        player_1.cards_count_info() # информация о кол-ве очков карт 1 игрока
        player_2.own_cards.append(BJ_deck.cards.pop()) # 2 раза добавление последней удаленной карты из колоды карт в список карт 2 игрока
        player_2.own_cards.append(BJ_deck.cards.pop())
        player_2.own_cards_info() # информация о картах 2 игрока
        player_2.cards_count_info() # информация о кол-ве очков карт 2 игрока

        if player_1.cards_count() == 21: # если кол-во очков карт 1 игрока = 21, то ему победа
            player_1.score_up()
            break
        elif player_2.cards_count() == 21: # если кол-во очков карт 2 игрока = 21, то ему победа
            player_2.score_up()
            break
        else: # иначе
            while True:
                answer_for_player_1 = input(f'\n{player_1.name}, будете брать еще карту? (y/n): ') # вопрос 1 игроку
                if answer_for_player_1 == 'n'.lower(): # если нет
                    player_1.cards_count_info() # вывод информации о кол-ве очков карт 1 игрока
                    break
                elif answer_for_player_1 == 'y'.lower(): # если да
                    player_1.own_cards.append(BJ_deck.cards.pop()) # добавление последней удаленной карты из колоды карт в список карт 1 игрока
                    player_1.own_cards_info() # информация о картах 1 игрока
                    player_1.cards_count_info() # информация о кол-ве очков карт 1 игрока
                    if player_1.cards_count() == 21: # если кол-во очков карт 1 игрока = 21, то ему победа
                        player_1.score_up()
                        break
                    elif player_1.cards_count() > 21: # если кол-во очков карт 1 игрока > 21, то победа 2 игроку
                        player_2.score_up()
                        break

            while True:
                if player_1.cards_count() >= 21:
                    break
                else:
                    answer_for_player_2 = input(f'\n{player_2.name}, будете брать еще карту? (y/n): ') # вопрос 2 игроку
                    if answer_for_player_2 == 'n'.lower(): # если нет
                        player_2.cards_count() # вывод информации о кол-ве очков карт 2 игрока
                        break
                    elif answer_for_player_2 == 'y'.lower(): # если да
                        player_2.own_cards.append(BJ_deck.cards.pop()) # добавление последней удаленной карты из колоды карт в список карт 2 игрока
                        player_2.own_cards_info() # информация о картах 2 игрока
                        player_2.cards_count_info() # информация о кол-ве очков карт 2 игрока
                        if player_2.cards_count() == 21: # если кол-во очков карт 2 игрока = 21, то ему победа
                            player_2.score_up()
                            break
                        elif player_2.cards_count() > 21: # если кол-во очков карт 2 игрока > 21, то победа 1 игроку
                            player_1.score_up()
                            break
            if player_2.cards_count() == player_1.cards_count(): # если кол-во очков карт игроков равны, то ничья
                print(f'\nНИЧЬЯ!')
            elif player_1.cards_count() < player_2.cards_count() <= 21: # если кол-во очков карт 2 игрока меньше/равно 21 и больше очков карт 1 игрока, то победа 2 игроку
                player_2.score_up()
            elif player_2.cards_count() < player_1.cards_count() <= 21: # если кол-во очков карт 1 игрока меньше/равно 21 и больше очков карт 2 игрока, то победа 1 игроку
                player_1.score_up()
    else:
        print('Неверная команда. Повторите.')

