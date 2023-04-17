# print(5, 8, 6)

# n = 5
#n = 1.98
#n = 'fddf'  # '' строка 

# n = 'fddf'

# print(type(n)) # type определят тип данных

# n = 'fd\'df' # Вывод ковычек
# print(n) 


# n = 'fd"GFGDFGDF"df' 
# print(n)

# print(5)
# print(5)
# print(5)
# """
# print(5, 8)
# print(5)
# print(5, 9)
# """

# a = 5
# b = 5.89
# c = 'Hello'
# # print(a,' - ',b,' - ',c)  # вывод переменных через -
# # print(f"{a}-{b}-{c}") # f""
# print("{} - {} - {}".format(a,b,c)) # Вывод 

# print('Введите первую строку')
# a = input()
# b = input('Введите второе число: ') # ввод в строку
# print(a, '+' , b, '=', a + b)

# c = 1
# print(c)
# print(type(c)) # тип данных floot
# # n = str(c) # тип данных str
# c = bool(c) # тип данных bool
# print(c)
# print(type(c)) # тип данных int

# v = 'dvdfs'
# v = int(v)

# print('Введите первое число: ')
# a = int(input())
# b = int(input('Введите второе число: '))

# a = 5.995676
# b = 6.5567654
# print(round(a*b, 3))  # round округление

# iter = 2 #
# iter += 3 # iter = iter + 3
# iter -+ 4 # iter = iter - 4
# iter *= 5 # iter = iter  * 5
# iter /= 5 # iter = iter / 5
# iter //= 5 # iter = iter// 5
# iter %= 5 # iter = iter % 5
# iter **= 5 # iter = iter ** 5 Возведение в 5 ую степень

# a = 1 > 4
# print(a)

# a = 1 < 4 and 5 > 2 # Если одно из условий наруеношо то false
# print(a)

# a = 1 == 2
# print(a)

# a = 1 != 2
# print(a)

# a = 'qwe'
# b = 'qwe'
# print( a==b )

# a = 1 < 3 < 5 < 10
# print(a)

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же Маша!')
# elif username == 'Марина':
#     print('Я так ждал вас, Марина')
# elif username == 'Ильнар':
#     print('Ильнар - топ')
# else:
#     print('Привет, ', username)

# i = 0
# while i < 5:
#     # if i == 3:
#     #     break
#     i = i + 1
# else:
#     print('Пожалуй')
#     print('Хватит )')
# print(i)

# n = int(input())
# flag = True
# i = 2
# while flag == True:
#     if n % i == 0: #Если остаток при деление числа n на i равен 0
#         flag = False
#         print(i)
#     elif i > n // 2: # Делитьль числа не может превышать введеное число, деление на 2
#         print(n)
#         flag = False
#     i += 1

# a = 'qwerrt'
# for i in a:
#     print(i)

# line = "" #Пустая перменная line
# for i in range(5): # Генерирует последовательность из 5 чисел, значит цикл будет выполняться 5 раз
#     line = "" #Пустая перменная line
#     for j in range(5): # к ЭТОЙ СТРАКЕ 5 раз прибовляем звездочку
#         line += "*"
#         print(line)

# text = 'СЪЕШЬ еще этих мягких булочек'
# # print(len(text)) # len позваляет узнать длину нашей строки.
# # print('еще' in text) # Ищет есть ли слово 'Еще' в нашей строке
# # print(text.lower()) # lower позволяет привести все буквы в нижний регистр
# # print(text.upper()) # upper обратная функция lower
# print(text.replace('еще','ЕЩЕ')) # replace Заменяет слово или словосочетания 

text = 'СЪЕШЬ еще этих мягких булочек'
# print(text[0])
# print(text[1])
# print(text[len(text)-1])
# print(text[-1])

# print(text[:])
# print(text[:2])
# print(text[:2])
# print(text[20:])
# print(text[2:9])
# print(text[6:-18])
# print(text[0:len(text):6])
# print(text[::6])
text = text[2:9] + text[-5] + text[:2]
print(text)