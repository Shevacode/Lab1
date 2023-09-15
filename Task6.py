
text = input("Введіть ваш текст: ")

max_symbols = int(input("Введіть максимальну кількість символів: "))

max_words = int(input("Введіть максимальну кількість слів: "))

words = text.split()
trimmed_text = ' '.join(words[:max_words])
if len(trimmed_text) > max_symbols:
    trimmed_text = trimmed_text[:max_symbols]

print("Обрізаний текст:", trimmed_text)