# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. 
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def two_division(dividend, divider):
    try:
        answer = dividend / divider
        return answer
    except ZeroDivisionError:
        return "делитель не может быть 0"


print(two_division(int(input("Введи делимое = ")), int(input("Введи делитель = "))))
