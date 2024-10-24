text = input("Введите строку: ")
reversed_words = [word[::-1] for word in text.split()]
reversed_text = ' '.join(reversed_words)
print(f"Развернутая строка: {reversed_text}")
