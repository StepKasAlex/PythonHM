# Необходимо написать программу, открывающую 
# файл на чтение и считывающую построчно данные. 
# При этом английские числительные должны заменяться на русские. 
# Новый блок строк должен записываться в новый текстовый файл.

tr_dict = {
	'One' : 'Odin',
	'Two' : 'Dva',
	'Three' : 'Tri',
	'Four' : 'Chetire'
}

with open('four.txt', 'r', encoding='utf8') as f:
	f2 = open('four2.txt', 'w', encoding='utf8')
	number_normal = 1
	for i in f.readlines():
		i = i.split()
		number = tr_dict[i[0]]
		print(f'{number} — {number_normal}', file=f2)
		number_normal += 1
	f2.close()
