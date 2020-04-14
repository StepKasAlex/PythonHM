 # Создать (программно) текстовый файл, записать в 
 # него программно набор чисел, разделенных пробелами. 
 # Программа должна подсчитывать сумму 
 # чисел в файле и выводить ее на экран.


with open('five.txt', 'w+', encoding='utf8') as f:
	inFile = list(map(int, input().split()))
	for num in inFile:
		print(num, file=f)
	sum_ = 0
	f.seek(0)
	for line in f.readlines():
		sum_ += int(line)
	print(sum_)
