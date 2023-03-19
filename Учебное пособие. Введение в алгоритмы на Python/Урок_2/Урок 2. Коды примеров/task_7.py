"""Факториал через рекурсию"""


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))

"""
Рекурсивные функции используют так называемый «Стек вызовов». 
Когда программа вызывает функцию, функция отправляется на верх стека вызовов. 
Это похоже на стопку книг, вы добавляете одну вещь за одни раз. 
Затем, когда вы готовы снять что-то обратно, 
вы всегда снимаете верхний элемент.
"""

'''
0 шаг. Вызов функции: fac(5)
1. fac(5) возвращает fac(4) * 5
2. fac(4) => fac(3) * 4
3. fac(3) => fac(2) * 3
4. fac(2) => fac(1) * 2
5. fac(1) => fac(0) * 1 (завершение рекурсивных вызовов)
6. 1 * 1 - возврат в вызов fac(1) (fac(0) * 1 -> 1 * 1)
6. 1 * 2 - fac(2)
7. 2 * 3 - fac(3)
8. 6 * 4 - fac(4)
9. 24 * 5 – fac(5)
10. Возврат в основную ветку программы значения 120
'''
