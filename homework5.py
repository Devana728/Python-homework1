#Реализуйте алгоритм перемешивания списка.
from random import randint, sample
from random import shuffle

N = int(input("Введите число N: "))
mass = []

for i in range (2*N+1):
    mass.append(randint(-N, N))
print(f"Последовательность 2N+1 чисел от {-N} до {N}:  {mass}")
b = sample(mass, len(mass))
print(f"перемешанный список {b}")



