##Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
##Пример:*
#- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
import math
num = int(input("Введите число: "))
mass = []
for i in range (1, num+1, 1):
    if i == 1:
       i = i 
       mass.append(i)
    else :       
        i = i* math.factorial(i - 1)
        mass.append(i)
print(f"Произведения чисел от 1 до {num}:  {mass}")