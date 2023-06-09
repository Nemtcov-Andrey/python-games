# Игра - считалка.
# N человек, пронумерованных числами от 1 до N, стоят в кругу. 
# Они начинают играть в считалку на выбывание, где каждый K-й по счёту человек выбывает из круга, после чего счёт продолжается со следующего за ним человека.
# На вход подаётся количество человек N и номер K. 
# Программа выводит число от 1 до N — это номер человека, который останется в кругу последним.

num = int(input('Кол-во человек: '))
number = int(input('Какое число в считалке?: '))
print('Значит, выбывает каждый', number, '-й человек')

people_list = list(range(1, num + 1))
count = 0

while len(people_list ) > 1:
  print('\nТекущий круг людей:', people_list)
  print('Начало счёта с номера', people_list[count])
  count = (count + number - 1) % len(people_list)
  if people_list[count] == people_list[-1]:
    print('Выбывает человек под номером', people_list.pop(count))
    count = 0
  else:
    print('Выбывает человек под номером', people_list.pop(count))
    
print('\nОстался человек под номером', people_list[0])
