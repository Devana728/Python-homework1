#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print('введите значения Х, Y, Z через пробел')
c = input().split()
x = c[0]
y = c[1]
z = c[2]


if (not (x or y or z)) == (not x and not y and not z):
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")