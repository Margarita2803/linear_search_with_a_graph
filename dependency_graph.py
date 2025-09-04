import random
import timeit
import matplotlib.pyplot as plt

def linear_search(arr, value):
    for index in range(len(arr)):
        if arr[index] == value:
            return index
    return -1

sizes = [10, 100, 1000, 5000, 10000]
times = []

for size in sizes:
    arr = [random.randint(1, size * 10) for _ in range(size)]
    value = arr[-1]  # Элемент в конце списка — худший случай

    # Замер времени выполнения функции linear_search через timeit
    stmt = f"linear_search(arr, value)"
    setup = (
        "from __main__ import linear_search\n"
        f"arr = {arr}\n"
        f"value = {value}\n"
    )

    # Запускаем timeit с 1000 повторениями
    t = timeit.timeit(stmt=stmt, setup=setup, number=1000)
    avg_time = t / 1000  # среднее время одного запуска
    times.append(avg_time)
    print(f"Размер списка: {size}, среднее время: {avg_time:.8f} секунд")

# Построение графика
plt.plot(sizes, times, marker='o')
plt.title("Среднее время линейного поиска (timeit) в зависимости от размера списка")
plt.xlabel("Размер списка")
plt.ylabel("Время, сек")
plt.grid(True)
plt.show()