# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: 
# speed, color, name, is_police (булево).  А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда). 
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. 
# Добавьте в базовый класс метод show_speed, который должен показывать текущую 
# скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение 
# о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к 
# атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
	def __init__(self, speed, color, name, is_police):
		self.atr_speed = speed
		self.atr_color = color
		self.atr_name = name
		self.atr_is_police = is_police

	def go(self):
		print('car is going')

	def stop(self):
		print('car is standing')

	def turn(self, direction):
		print(f'Car turned {direction}')

	def show_speed(self):
		print(f'Car speed is {self.atr_speed}')

class TownCar(Car):
	def show_speed(self):
		if self.atr_speed > 60:
			print('You violated speed limits')

class WorkCar(Car):
	def show_speed(self):
		if self.atr_speed > 40:
			print('You violated speed limits')

class SportCar(Car):
	def __init__(self, speed, color, name, is_police):
		super().__init__(speed, color, name, is_police)

	def show_speed(self):
		if self.atr_speed > 140:
			print('You are cool!!!')

class PoliceCar(Car):
	def show_police(self):
		if self.atr_is_police == True:
			print('VIU VIU VIU VIU, Stop the car, please')

car = Car(50, 'red', 'Lada', False)
car.go()
car.stop()
car.turn('right')
car.show_speed()

towncar = TownCar(70, 'white', 'Reno', False)
towncar.show_speed()
print(towncar.atr_is_police)

sportcar = SportCar(150, 'blue', 'Lexus', False)
sportcar.show_speed()

policecar = PoliceCar(200, 'white-blue', 'Chevrolete', True)
policecar.show_police()
