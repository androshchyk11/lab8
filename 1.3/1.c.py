import numpy as np

array1 = np.zeros((3, 3), dtype=int)  # Оголошуємо першу матрицю та заповнюємо її нулями
array2 = np.zeros((3, 3), dtype=int)  # Оголошуємо другу матрицю та заповнюємо її нулями
result = np.zeros((3, 3), dtype=int)  # Оголошуємо третю матрицю та заповнюємо її нулями

for i in range(3):
    for j in range(3):
        x = int(input(f"array1[{i}][{j}] = "))  # Поелементно заповнюємо першу матрицю
        array1[i][j] = x

for i in range(3):
    for j in range(3):
        x = int(input(f"array2[{i}][{j}] = "))  # Поелементно заповнюємо другу матрицю
        array2[i][j] = x

# Виконуємо множення матриць за допомогою вкладених циклів
for i in range(3):
    for j in range(3):
        for k in range(3):
            result[i][j] += array1[i][k] * array2[k][j]
print(result)
