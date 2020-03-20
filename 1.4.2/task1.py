'''
Для завдання під номером 4, скласти програму, яка здійснювала б розрахунок і
виведення на екран результатів розрахунку потреб магазинів в заданому продукті в
кілограмах:
 для районів міста;
 для всього міста.
При цьому ці дані повинні друкуватися в трьох колонках:
 для тари типу "ТАК";
 для тари типу "НІ";
 всього.
'''
id = 1  # ІД кожного магазину
quantityOfAreas = 3  # кількість районів(можна змінити)
shopsInEachArea = [1, 2, 1]  # кількість магазинів у кожному районі(можна змінити)
productsInEveryShop = {}  # продукти у кожному магазині

yes = []  # массив з елементів де є ТАК
no = []  # массив з елементів де є НІ
all = []  # массив з ісіх продуктів

# Нище заповнюємо словник, який складається з усіх продуктів у магазинах(можна додавати або забирати елементи)
productsInEveryShop[1] = [{1: ["Potato", 30, "Yes"]}, {2: ["Apple", 20, "No"]}, {3: ["Cucumber", 20, "No"]}]
productsInEveryShop[2] = [{1: ["Potato", 15, "Yes"]}, {2: ["Cucumber", 5, "No"]}]
productsInEveryShop[3] = [{1: ["Potato", 50, "Yes"]}, {2: ["Pineapple", 14, "No"]}, {3: ["Watermelon", 20, "Yes"]},
                          {4: ["Cucumber", 45, "No"]}]
productsInEveryShop[4] = [{1: ["Potato", 15, "Yes"]}]

# Потрібно пройтись по елементам для того, щоб розділити на ТАК/НІ для правильного виводу на екран
for i in range(1, len(productsInEveryShop) + 1):  # циклом проходим в 1 до довжини словника+1
    for j in range(
            len(productsInEveryShop.get(i))):  # циклом проходимо по довжині значення в словнику, адже воно є массивом
        if (productsInEveryShop.get(i).__getitem__(j).get(j + 1).__getitem__(2) == "Yes"):  # Перевіряємо на ТАК/НІ
            yes.append(
                productsInEveryShop.get(i).__getitem__(j).get(j + 1))  # якщо критерій підходить то додаємо у массив yes
            all.append(productsInEveryShop.get(i).__getitem__(j).get(j + 1))  # додаємо у массив з усіма елементами
        else:  # крім YES може бути ще No
            no.append(
                productsInEveryShop.get(i).__getitem__(j).get(j + 1))  # якщо не підійшло для першого, то додаємо у no
            all.append(productsInEveryShop.get(i).__getitem__(j).get(j + 1))  # додаємо у массив з усіма елементами

print("All products with YES - ", yes)
print("All products with NO - ", no)
print("All products - ", all)

products = ["Cucumber", "Potato", "Apple", "Pineapple",
            "Watermelon"]  # список всіх можливих продуктів, для перевірки при вводі чи правильно ввів користувач
while True:
    neededProduct = input("Choose the product: ")
    if (neededProduct in products):
        break
    else:
        print("There is no such product")

sumForCity = 0  # к-сть кілограмів для всього міста
sumForShops = []  # к-сть кілограмів у кожному магазині
sumForAreas = []  # к-сть кілограмів у кожному районі

# цикл для знаходження потрібну к-сть кілограмів для міста
for i in range(1, len(productsInEveryShop) + 1):  # знову проходимо по елементам словника
    for j in range(len(productsInEveryShop.get(i))):  # знову проходиом по елементам значення
        if (productsInEveryShop.get(i).__getitem__(j).get(j + 1).__getitem__(
                0) == neededProduct):  # перевіряємо чи цей продукт є шуканим
            sumForCity += productsInEveryShop.get(i).__getitem__(j).get(j + 1).__getitem__(
                1)  # якщо це він, то додаємо у загальну суму для міста

# цикл для знаходження потрібну к-сть кілограмів для кожного магазину
for i in range(1, len(productsInEveryShop) + 1):  # знову проходимо по елементам словника
    for j in range(len(productsInEveryShop.get(i))):  # знову проходиом по елементам значення
        for q in range(len(shopsInEachArea)):  # проходимо стільки разів скільки є районів
            z = 0  # додаємо лічильник, який буде рахувати значення
            for m in range(shopsInEachArea[q]):  # проходиом стільки разівв, скільки є магазинів у кожному районі
                if (productsInEveryShop.get(i).__getitem__(j).get(j + 1).__getitem__(
                        0) == neededProduct):  # перевіряємо чи є введений продукт шуканим
                    z += productsInEveryShop.get(i).__getitem__(j).get(j + 1).__getitem__(1)  # додаємо у лічильник
    sumForShops.append(z)  # додаємо у масив який зберігає кількість кілограмів у кожному магазині
# Для знаходження значення на кожному районі я зробив цикл, який буде додавати значення елементів массиву sumForShops поки кількість магазинів у районі не закінчиться
k = 0  # лічильник для проходження по елементам масива sumForShops
for i in range(len(shopsInEachArea)):  # проходимо по елементам масиву, який зберігає кількість маагазинів у місті
    j = 0  # обнуляємо лічильник
    z = 0  # обнуляємо лічильник
    while (j < shopsInEachArea[i]):  # виконуємо дії стільки разів, скільки є магазинів у районі
        z += sumForShops[k]  # додаємо до лічильника значення кілограм у магазині
        j += 1  # збільшуємо лічильник
        k += 1  # збільшуємо лічильник
    sumForAreas.append(z)  # додажмо значення до массиву який зберігає кулькість кілограм по району

# Виведення відповідей
for i in range(len(sumForAreas)):
    print(f"In area {i}: {sumForAreas[i]} kilos of {neededProduct}")
print(f"In city: {sumForCity} kilos of {neededProduct}")
