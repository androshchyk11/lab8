import numpy as np

array = np.zeros((3,3),dtype=int) #Оголошуємо першу матрицю та заповнюємо її нулями
arrayT = np.zeros((3,3), dtype=int) #Оголошуємо другу матрицю та заповнюємо її нулями

for i in range(3):
    for j in range(3):
        x = int(input(f"array[{i}][{j}] = ")) #Поелементно заповнюємо першу матрицю
        array[i][j] = x

for i in range(3):
    for j in range(3):
        arrayT[j][i] = array[i][j] #Виконуємо транспонування, міняючи рядки на ствопці
print(arrayT)
