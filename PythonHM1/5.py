# Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма 
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение. 
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). 
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

revenue = int(input('enter revenue value: '))
costs = int(input('enter cost value: '))

if revenue > costs:
	print('the company works profitably')
	profit = revenue - costs
	rentability = profit / revenue
	print(rentability)
	workers = int(input('enter number of workers: '))
	profit_per_worker = profit / workers
	print(profit_per_worker) 
else:
	print('the company operates at a loss')

