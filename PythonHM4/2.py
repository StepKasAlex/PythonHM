# Представлен список чисел. Необходимо вывести элементы 
# исходного списка, значения которых больше предыдущего элемента.


list_1 = [8, 2, 5, 1, 10, 23, 44, 3, 7]
solution_list = [list_1[number] for number in range(1, len(list_1)) if list_1[number] > list_1[number - 1]]
print(solution_list)
