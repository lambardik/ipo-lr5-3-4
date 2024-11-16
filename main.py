string = str(input("Введите строку: ")) 
words = string.split()
rev = [word[::-1] for word in words] 
res  = ' '.join(rev) 
print("Развернутая строка:",res)
