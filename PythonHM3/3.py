# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.


def my_func(number1, number2, number3):
	list_1 = [number1, number2, number3]
	minimum_in_list = min(list_1)
	list_1.remove(minimum_in_list)
	solution = sum(list_1)
	return solution


print(my_func(4, -1, 20))
