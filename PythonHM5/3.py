# Создать текстовый файл (не программно), 
# построчно записать фамилии сотрудников и 
# величину их окладов. Определить, кто из 
# сотрудников имеет оклад менее 20 тыс., 
# вывести фамилии этих сотрудников. 
# Выполнить подсчет средней величины дохода сотрудников.

with open('third.txt', 'r') as f:
	money = []
	less_20 = []
	for line in f.readlines():
		line = line.split()
		money.append(line[1])
		if int(line[1]) < 20000:
			print('Less than 20k get {}'.format(line[0]))
	money = list(map(int, money))
	print('Middle wage is {}'.format(sum(money) / 2))

