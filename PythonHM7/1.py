# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), 
# который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов 
# класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.

class Matrix:
	def __init__(self, list_of_lists):
		self.list_of_lists = list_of_lists
		self.gor_dimension = len(list_of_lists[0])
		self.ver_dimension = len(list_of_lists)

	def __str__(self):
		return '\n'.join(' '.join(map(str, number)) for number in self.list_of_lists)

	def __add__(self, other):
		if self.gor_dimension == other.gor_dimension and self.ver_dimension == other.ver_dimension:
			time_list = []
			result = []
			for i in range(len(self.list_of_lists)):
				for j in range(len(self.list_of_lists[0])):
					sum_num = self.list_of_lists[i][j] + other.list_of_lists[i][j]
					time_list.append(sum_num)
				result.append(time_list)
				time_list = []
			return Matrix(result)
		else:
			return 'Matrices are not equals'


matrix = Matrix([[1, 2, 3], [5, 6, 7], [8, 9, 10]])
matrix1 = Matrix([[9, 8, 7], [5, 4, 3], [2, 1, 0]])
new_matrix = matrix + matrix1
print(matrix)
print(new_matrix)
new_matrix1 = matrix + new_matrix
print(new_matrix1)






