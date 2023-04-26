# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 

number_one = int(input("Введите число A: "))
number_two = int(input("Введите число B: "))

def number_sum(number_one, number_two):
    if number_two == 0:
        return number_one
    return(number_sum(number_one + 1, number_two - 1))
print(number_sum(number_one, number_two))