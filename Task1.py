#  Напишите программу, которая на вход принимает два числа A и B, 
#  и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

number_one = int(input("Введите число A: "))
number_two = int(input("Введите число B: "))

def number_degree(number_one, number_two):
    if number_two == 0:
        return 1
    return (number_one * number_degree(number_one, number_two - 1))
print(number_degree(number_one, number_two))