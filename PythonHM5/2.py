# Создать текстовый файл (не программно), 
# сохранить в нем несколько строк, выполнить 
# подсчет количества строк, количества 
# слов в каждой строке.


with open('second.txt', 'r') as f:
	count_lines = 0
	count_in_line = 0
	for line in f.readlines():
		count_lines += 1
		count_in_line = len(line)
		print(count_in_line)
	print(count_lines)

