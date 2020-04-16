# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title 
# (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать
# три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов 
# реализовать переопределение метода draw. Для каждого из классов метод должен выводить 
# уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный 
# метод для каждого экземпляра.

class Stationery:
	def __init__(self, title):
		self.art_title = title

	def draw(self):
		print('Start drawing!')

class Pen(Stationery):
	def draw(self):
		print('Pen drawing!')

class Pencil(Stationery):
	def draw(self):
		print('Pencil drawing!')

class Handle(Stationery):
	def draw(self):
		print('Handle drawing!')

stat = Stationery('B1')
stat.draw()

pen = Pen('good pen')
pen.draw()

pencil = Pencil('Good pencil')
pen.draw()

handle = Handle('Good handle')
handle.draw()