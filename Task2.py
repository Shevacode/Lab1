import math

x = float(input("Введіть значення x: "))
t = float(input("Введіть значення t: "))

Z = ((9 * math.pi * t + 10 * math.cos(x)) / math.sqrt(t) - abs(math.sin(t))) * math.exp(x)

print(f"Z = {Z:.2f}")