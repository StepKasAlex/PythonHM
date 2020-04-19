# Реализовать проект расчета суммарного расхода ткани на производство одежды. 
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное 
# название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов 
# одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут 
# быть обычные числа: V и H, соответственно. 
# Для определения расхода ткани по каждому типу одежды использовать формулы: 
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих 
# методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные 
# на этом уроке знания: реализовать абстрактные классы для основных классов 
# проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod, ABCMeta

class Clothes():
	__metaclass__ = ABCMeta
	def __init__(self, name_for_coat = None, coat_size = None, name_for_costume = None, costume_height = None):
		self._name_for_coat = name_for_coat
		self._name_for_costume = name_for_costume
		self._coat_size = coat_size
		self._costume_height = costume_height
		self._coat_consumption = None
		self._costume_consumption = None

	@property
	def coat_consumption(self):
		self._coat_consumption = self._coat_size / 6.5 + 0.5
		return self._coat_consumption

	@property
	def costume_consumption(self):
		self._costume_consumption = 2 * self._costume_height + 0.3
		return self._costume_consumption
	
	def all_tissue(self):
		if self._costume_consumption != None and self._coat_consumption != None:
			return self._coat_consumption + self._costume_consumption
		else:
			return 'You need to calculate coat and costume tissue consumption'

	@abstractmethod
	def for_test(self):
		print('abstractmethod is very COOOOL!!!')

clothe = Clothes('Burberry', coat_size=120, name_for_costume='Boss', costume_height=200)
print(clothe.coat_consumption) #  сразу сделал через проперти
print(clothe.costume_consumption)
print(clothe.all_tissue())

class PremiumClothes(Clothes):
	def for_test(self):
		print('You didnt tell us some aspect about abstractmethod')

	def yoy(self):
		print('This clothes are better')

pc = PremiumClothes('Burberry', coat_size=120, name_for_costume='Boss', costume_height=200)
# print(pc.all_tissue()) # не выполняется
pc.yoy()
pc.for_test()
