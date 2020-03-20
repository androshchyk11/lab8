import numpy as np

array = np.zeros((4, 4), dtype=int)  # Оголошуємо матрицю та заповнюємо її нулями

for i in range(4):
    for j in range(4):
        x = int(input(f"array[{i}][{j}] = "))  # Поелементно заповнюємо матрицю
        if (x < 0):  # Якщо елемент від'ємний, то одразу міняємо його на 0
            array[i][j] = 0
        else:
            array[i][j] = x  # Якщо елемент невід'ємний то записуємо його у матрицю
print(array)
