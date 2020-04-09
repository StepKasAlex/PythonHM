# 6. Реализовать два небольших скрипта:
# а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
# б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.

import itertools

# a)
def inf_int_numbers(start_n):
	for i in itertools.count(start_n):
		print(i, end=',')


print(inf_int_numbers(1))


# b)
def inf_rep_numbers(list_1):
	for j in itertools.cycle(list_1):
		print(j, end=' ,')


print(inf_rep_numbers([1, 5, 6]))