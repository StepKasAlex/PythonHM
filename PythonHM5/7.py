# Создать (не программно) текстовый файл, в котором каждая строка должна 
# содержать данные о фирме: название, форма собственности, выручка, издержки.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, 
# а также среднюю прибыль. Если фирма получила убытки, 
# в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, 
# а также словарь со средней прибылью. Если фирма получила убытки, 
# также добавить ее в словарь (со значением убытков).
# Итоговый список сохранить в виде json-объекта в соответствующий файл.

with open('seven.txt', 'r', encoding='utf8') as f:
	income = []
	num = 1 # просто для красоты вывода
	ind = 0 # тоже для красоты
	for line in f.readlines():
		file = line.split()
		file = list(map(int, file[2:]))
		income.append(file[0] - file[1])
		print('firm {} income = {}'.format(num, income[ind]))
		num += 1
		ind += 1
	average_profit = 0
	for i in income:
		if i > 0:
			average_profit += i
	average_profit /= 2
	print(f'middle income: {average_profit}')
	my_list = []
	time_dict = {}
	ind1 = 0
	f.seek(0)
	for line in f.readlines():
		file = line.split()
		time_dict[file[0]] = income[ind1]
		my_list.append(time_dict.copy())
		ind1 += 1
		time_dict.clear()
	av_dict = {}
	av_dict['average_profit'] = average_profit
	my_list.append(av_dict)
	print(my_list)
