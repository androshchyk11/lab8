import numpy as np

while True:
    try:
        n = int(input("How many numbers should be in array: ")) #Користувач вводить кількість символів у массиві
        break
    except ValueError as e:
        print(e)
array = np.zeros(n, dtype=int) #Створюємо массив та заповнюємо його нулями

for i in range(n):
    while True:
        try:
            x = int(input()) # Користувач поелементно воодить числа у массив
            array[i] = x
            break
        except ValueError as e:
            print(e)

for i in range(n // 2): # Проходимо по массиву по його центральний індекс
    array[i], array[-i - 1] = array[-i - 1], array[i] # Міняємо місцями протилежні числа
print(array)
