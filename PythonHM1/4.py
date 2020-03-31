number = 451876
simple_number = -1

while number > 10: # задаём цикл до того момента, пока у числа 'number' не останется 1 число
	l_number = number % 10 # этим способом мы достаем последнюю цифру числа
	number //= 10 # этим способом мы убираем последнюю цифру числа
	if l_number > simple_number: # мы задаем условие, по которому будет определяться бОльшая цифра
		simple_number = l_number

print(simple_number)
