# Игра - текстовый квест. 

# Вы находитесь в квартире, ваша задача — покинуть эту квартиру. Вы можете свободно перемещаться по квартире. 
# В квартире есть три комнаты (спальня, кухня, ванна) и коридор. В ванну можно попасть из коридора и спальни. В спальню можно попасть из ванны и коридора. На кухню можно попасть только из коридора. 
# Коридор связан со всеми комнатами, но в нём дополнительно есть дверь наружу. Если вы попытаетесь выбраться через окно на кухне, то разбиваетесь и проигрываете.

def bathroom():
  print('Вы в ванной. Куда идём?')
  print('1 - в спальню')
  print('2 - в коридор')  
  answer = input('-> ')
  print()
  if answer == '1':
    bedroom()
  elif answer == '2':
    corridor()
  else:
    print('Ошибка ввода!')

def bedroom():
  print('Вы в спальне. Куда идём?')
  print('1 - в ванну')
  print('2 - в коридор')
  answer = input('-> ')
  print()
  if answer == '1':
    bathroom()
  elif answer == '2':
    corridor()
  else:
    print('Ошибка ввода!')
  
def corridor():
  print('Вы в коридоре. Куда идём?')
  print('1 - в спальню')
  print('2 - в ванну')  
  print('3 - на кухню') 
  print('4 - в дверь, на улицу') 
  answer = input('-> ')
  print()
  if answer == '1':
    bedroom()
  elif answer == '2':
    bathroom()
  elif answer == '3':
    kitchen()
  elif answer == '4':
    print('Поздравляю! Вы вышли из квартиры. Игра окончена.')
  else:
    print('Ошибка ввода!')

def kitchen():
  print('Вы на кухне. Куда идём?')
  print('1 - в открытое окно')
  print('2 - в коридор') 
  answer = input('-> ')
  print()
  if answer == '1':
    print('Упс! Вы разбились! Игра окончена.')
  elif answer == '2':
    corridor()
  else:
    print('Ошибка ввода!')

def main_menu():
  start = 0
  while start < 1 or start > 4:
    print('С какой комнаты начнем игру?')
    print('\n1 - в коридоре', '\n2 - в ванной', '\n3 - на кухне', '\n4 - в спальне')
    start = int(input('-> '))
    print()
    if start == 1:
      corridor()
    elif start == 2:
      bathroom()
    elif start == 3:
      kitchen()
    elif start == 4:
      bedroom()
    else:
      print('\nВы ошиблись! Такой комнаты нет!')

main_menu() 
