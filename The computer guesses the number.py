# Игра «Компьютер угадывает число».
# Программа с помощью цепочки вопросов и ответов угадывает число.

num_of_boy = int(input('Вы загадываете число от 1 до 100: '))
first_num, last_num = 1, 100
count = 0 # счетчик кол-ва попыток угадывания
while True: # запускаем бесконечный цикл
  full = (first_num + last_num) // 2
  print('Ваше загаданное число равно, меньше или больше, чем число:', full, '?')
  answer_mashine = int(input('Мое число (1 - равно, 2 - больше, 3 - меньше): '))
  count += 1
  if answer_mashine == 3:
    last_num = full
  elif answer_mashine == 2:
    first_num = full
  else:
    break
print('\nЧисло отгадано!')
print('Количество попыток угадывания числа компьютером:', count)
