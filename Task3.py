import math

x = float(input("Введіть значення x: "))


if x >= 0:
    f = 0.5 - math.pow(abs(x), 0.25)
else:
    f = math.pow(math.sin(x**2) / abs(x+1), 2)

print(f"f(x) = {f:.2f}")