import timeit

print("1 - Linear search;\n"
      "2 - Binary search;\n"
      "3 - direct substring search.")
flag = int(input("Choose what do you want to use: "))

mysetup = '''
import numpy as np
import random
            '''
if flag == 1:
    mycode = '''
n = int(input("Input quantity of array: "))
a = np.zeros(n, dtype=int)
q = int(input("press 1 if you want to fill array by yourself, press 2 if you want to fill array by random:"))
if (q == 2):
    for i in range(n):
        a[i] = random.randint(-5, 5)
elif q == 1:
    for i in range(n):
        z = int(input())
        a[i] = z
print(a)
x = int(input("What numberr do you want to search: "))
n = len(a)
i = 0
audits = 2
while i < n and a[i] != x:
    i += 1
    audits = i * 2
if i == n:
    print("No such element")
    print(w)
else:
    print(f"Element {x} is found on position {i+1}")
    print(f"there was {audits} audits") 
'''
elif flag == 2:
    mycode = '''
n = int(input("Input quantity of array: "))
a = np.zeros(n, dtype=int)
q = int(input("press 1 if you want to fill array by yourself, press 2 if you want to fill array by random:"))
if (q == 2):
    for i in range(n):
        a[i] = random.randint(-5, 5)
elif q == 1:
    for i in range(n):
        z = int(input())
        a[i] = z
x = int(input("What numberr do you want to search: "))
a = sorted(a)
print(a)
l = 0
r = len(a) - 1
k = 0
flag = False
while l <= r and not flag:
    k = (l + r) // 2
    if a[k] == x:
        flag = True
    elif a[k] < x:
        l = k + 1
    else:
        r = k - 1
if not flag:
    print('Element not found')
else:
    print(f'Element {x} is found at {k + 1} position')
'''
elif flag == 3:
    mycode = '''
string = input()
substring = input()
i = j = 0
lengthS = len(string)  # Довжина стрічки в якій ми шукаєм
lengthX = len(substring)  # Довжина стрічки, яку ми шукаєм
# поки не досягли одного із кінців
while i <= lengthS - lengthX and j < lengthX:
    # якщо зівпали букви то рухаємось по двум строкам
    if string[i + j] == substring[j]:
        j += 1
    # інакше рухаємось по строці(+1), починаючи с 0 символа підстроки
    else:
        i += 1
        j = 0
# якщо дішли до кінца підстроки - знайшли, інакше - ні
if j == lengthX:
    print(f"substring {substring} begins on {i}")
else:
    print("No such substring")
    '''
print(timeit.timeit(setup=mysetup,
                    stmt=mycode,
                    number=1))
