# игра. Крестики-нолики.

class Cell: # класс клетки
    # статический атрибут класса клетки:
    busy = '-' # занятая клетка

    def __init__(self, numb_cell): # конструктор класса клетки
        self.numb_cell = numb_cell

    def run(self, sym):
        self.busy = sym

class Broad: # класс поля

    def __init__(self): # конструктор класса поля
        self.board = [Cell(i) for i in range(1, 10)] # пройдемся по клеткам

    def take_input(self, sym): # метод ввода
        valid = False
        while not valid:
            self.draw_board()
            player_answer = input('На какую клетку поставим ' + sym + '?')
            try:
                player_answer = int(player_answer)
            except:
                print('Некорректный ввод. Повторите')
                continue
            if 1 <= player_answer <= 9:
                if self.board[player_answer - 1].busy == '-':
                    self.board[player_answer - 1].run(sym)
                    valid = True
                else:
                    print('Эта клетка уже занята!')
            else:
                print('Некорректный ввод. Введите число от 1 до 9.')

    def draw_board(self): # метод рисования поля
        print("-" * 13)
        for i in range(3):
            print('|', self.board[0+i*3].busy, '|', self.board[1+i*3].busy, '|', self.board[2+i*3].busy, '|')
            print('-' * 13)

    def win(self): # метод выйгрыша
        # выйгрышные комбинации:
        win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for each in win_coord: # пройдемся по каждой координате
            if self.board[each[0]].busy == self.board[each[1]].busy == self.board[each[2]].busy:
                return self.board[each[0]].busy
        return False

class Player: # класс игрока
    # статический атрибут класса игрока
    hand = list() # создадим список

    def __init__(self, name): # конструктор класса игрока
        self.name = name

    def hand_add(self, cell): # метод добавления клетки в список
        self.hand.append(cell)

board = Broad()

player1 = Player('Игрок 1')
player2 = Player('Игрок 2')

counter = 0 # счетчик
win = False
while not win: # цикл когда нет выйгрыша
    if counter % 2 == 0:
        board.take_input('X')
    else:
        board.take_input('O')
    counter += 1
    if counter > 4:
        tmp = board.win()
        if tmp == 'X':
            print(player1.name, 'выиграл!')
            win = True
            break
        elif tmp == 'O':
            print(player2.name, 'выиграл!')
            win = True
            break
    if counter == 9:
        print('Ничья!')
        break
