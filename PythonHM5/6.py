# Необходимо создать (не программно) текстовый файл, 
# где каждая строка описывает учебный предмет и 
# наличие лекционных, практических и лабораторных 
# занятий по этому предмету и их количество. 
# Важно, чтобы для каждого предмета не обязательно 
# были все типы занятий. Сформировать словарь, 
# содержащий название предмета и общее количество 
# занятий по нему. Вывести словарь на экран.

with open('six.txt', 'r', encoding='utf8') as f:
	list_all = []
	for line in f.readlines():
		subject, lecture, practice, lab = line.split()
		list_ = [subject[:-1], lecture, practice, lab]
		list_all.append(list_)
	my_dict = {}
	for list_1 in list_all:
		for i in list_1:
			if i == '-':
				list_1.remove('-')
	time_list = []
	for list_2 in list_all:
		time_list.append(list_2[0])
		list_2 = list(map(int, list_2[1:]))
		time_list.append(sum(list_2))
		my_dict[time_list[0]] = time_list[1]
		time_list.clear()
	print(my_dict)















	# 	list_sub.append(subject[:-1])
	# 	list_lecture.append(lecture)
	# 	list_prac.append(practice)
	# 	list_lab.append(lab)
	# all_lists = []
	# all_lists.append(list_lecture)
	# print(list_lecture)
	# all_lists.append(list_prac)
	# print(list_prac)
	# all_lists.append(list_lab)
	# print(list_lab)
	# print(all_lists)
	# for list_ in all_lists:
	# 	for number in list_:
	# 		if number == '-':
	# 			list_.remove(number)
	# 	for number1 in list_:
	# 		number1 = int(number1)
	# 		print(type(all_lists[0][0]))
	# print(all_lists)
	# # my_dict = {}
	# # ind = 0
	# # for i in list_sub:
	# # 	calc = sum(all_lists[ind])
	# # 	my_dict.update([i, ])
	# # 	ind += 1
