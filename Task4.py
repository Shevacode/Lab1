a = int(input("Введіть перше ціле число: "))
b = int(input("Введіть друге ціле число: "))
c = int(input("Введіть третє ціле число: "))
N = int(input("Введіть значення N: "))

numbers_in_range = [num for num in [a, b, c] if 1 <= num <= N]

if numbers_in_range:
    print("Числа, що належать інтервалу [1, N]:", ", ".join(map(str, numbers_in_range)))
else:
    print("Жодне з введених чисел не належить інтервалу [1, N]")