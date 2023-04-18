# Игра Блек-джек.

# Блек-джек также известен как 21. Суть игры проста: нужно или набрать ровно 21 очко, или набрать очков больше, чем в руках у дилера, но ни в коем случае не больше 21. 
# Если игрок собирает больше 21, он «сгорает». В случае ничьей игрок и дилер остаются при своих.
# Карты имеют такие «ценовые» значения: от двойки до десятки — от 2 до 10 соответственно, у туза — 1 или 11 (11 пока общая сумма не больше 21, далее 1), у короля, дамы, вальта — 10.
# Программа вначале случайным образом выдаёт пользователю и компьютеру по две карты и затем запрашивает у пользователя действие: взять карту или остановиться. 
# На экран выводится информация о картах пользователя. После того как игрок останавливается, выводится победитель.

import random
random.seed()

class BlackJack:
    def __init__(self):  # конструктор класса
        self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace'] * 4
        self.score = 0
        self.bot_score = 0

    def print_card(self, current, score, bot):
        if not bot:
            print(f'Вам попалась карта {current}. У вас {score} очко(в).')
        else:
            print(f'Крупье попалась карта {current}. У компьютера {score} очко(в)')

    def random_card(self, score, bot):
        current = self.deck.pop()
        if type(current) is int:
            score += current
        elif current == 'Ace':
            if score <= 10:
                score += 11
            else:
                score += 1
        else:
            score += 10
        self.print_card(current, score, bot)
        return score

    def choice(self):
        score = self.random_card(self.score, False)
        bot_score = self.random_card(self.bot_score, True)
        while True:
            choice = input('Будете брать карту? y/n: \n')
            if choice == 'y'.lower():
                score = self.random_card(score, False)
                if bot_score < 19 and score <= 21:
                    bot_score = self.random_card(bot_score, True)
                if score > 21 or bot_score == 21:
                    print('Увы..., вы проиграли')
                    break
                elif score == 21 and bot_score == 21:
                    print('Ничья')
                elif score == 21 or bot_score > 21:
                    print('Ура! Вы победили!')
                    break
            elif choice == 'n':
                if score > bot_score and bot_score < 19:
                    while bot_score < 19:
                        bot_score = self.random_card(bot_score, True)
                if score < bot_score <= 21:
                    print(f'Вы проиграли, у вас {score} очко(в), у компьютера {bot_score} очко(в)')
                else:
                    print(f'Вы победили, у вас {score} очко(в), у компьютера {bot_score} очко(в)')
                break

    def start(self):
        random.shuffle(self.deck)
        print('Да начнутся голодные игры!\n')
        self.choice()

        print('До новых встреч!')

game = BlackJack()
game.start()
