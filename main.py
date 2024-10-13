def reverse_words(text):

  words = text.split()
  reversed_words = [word[::-1] for word in words]
  return ' '.join(reversed_words)

text = input("Введите строку: ")
reversed_text = reverse_words(text)
print(f"Развернутая строка: {reversed_text}")
