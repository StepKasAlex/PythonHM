# *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. 
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — 
# номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, 
# единица измерения). Структуру нужно сформировать программно, 
# т.е. запрашивать все данные у пользователя.

list_product = []
condition = input('Чтобы начать, введите "Start", иначе "Stop"')
list_of_titles = []
list_of_prices = []
list_of_quantity = []
list_of_units = []

while condition != 'Stop':
	number = int(input('Введите номер товара: '))
	name = input('Введите название товара: ')
	price = input('Введите цену товара: ')
	quantity = input('Введите количество: ')
	units = input('Введите единицу измерения: ')
	list_of_titles.append(name)
	list_of_prices.append(price)
	list_of_quantity.append(quantity)
	list_of_units.append(units)
	dict_prod = {'title' : name, 'price' : price, 'quantity' : quantity, 'units' : units}
	set_number = (number, dict_prod)
	list_product.append(set_number)
	for product in list_product:
		print(product)
	condition = input('Чтобы закончить, введите "Stop", иначе +: ')

# Необходимо собрать аналитику о товарах. Реализовать словарь, 
# в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.

if list_product: # условие, что список товаров не пуст
	dict_prod_new = {
	'title' : list_of_titles,
	'price' : list_of_prices,
	'quantity' : list_of_quantity,
	'units' : list_of_units
	}
	for key, value in dict_prod_new.items():
		print(key, ':', value, sep='')
else:
	print('У вас нет товаров в списке') 
