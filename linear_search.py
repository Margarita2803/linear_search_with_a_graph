import random

def linear_search(arr, value):
    for index in range(len(arr)):
        if arr[index] == value:
            return index
    return -1

arr = [random.randint(1, 100) for _ in range(100)] #генерируем список из 100 случайных чисел
a, b, c = 45, 89, 3

print('Индекс искомого элемента:', linear_search(arr, a), linear_search(arr, b), linear_search(arr, c))




