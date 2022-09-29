#Задайте список из 2N+1 элементов, заполненных числами 
#из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.
from math import prod
from random import randint
N = int(input("Введите число N: "))
mass = []

for i in range (2*N+1):
    
    
    
    mass.append(randint(-N, N))
print(f"Последовательность 2N+1 чисел от {-N} до {N}:  {mass}")
print('Выберите элементы списка: ')

a = list(map(int,input().split()))
prod = 1
for  i  in a :   
    prod *= mass [i]
print(f'Произведение элементов списка: {prod}')
