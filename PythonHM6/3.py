# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, 
# position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться
# на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. 
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать 
# методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии 
# (get_total_income). Проверить работу примера на реальных данных (создать экземпляры 
# класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
	def __init__(self, name, surname, position, salary, premium):
		self.name = name
		self.surname = surname
		self.position = position
		self._income = {'salary' : salary ,'premium' : premium}


class Position(Worker):
	def get_full_name(self):
		return (f'Full worker name is {self.name} {self.surname}')

	def get_total_income(self):
		return ('He get: '), self._income.get('salary') + self._income.get('premium')

worker = Worker('Kiselev', 'Alexandr', 'Student', 30000, 15000)
print(worker.name)
print(worker.surname)
print(worker.position)
print(worker._income)
pworker = Position('Kiselev', 'Alexandr', 'Student', 30000, 15000)
print(pworker.get_full_name())
print(pworker.get_total_income())
