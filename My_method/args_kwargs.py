""" Посмотрим на типичную функцию, которая использует два аргумента """

# def multiply(x, y):
#     print(x * y)
#
#
# multiply(5, 4)
"""В коде выше создается функция с аргументами х и y, и затем при вызове функции нам нужно использовать числа соответствующие х и y. 
В данном случае мы передаем числа типа integer — 5 для х и 4  для у:"""

# def multiply(x, y):
#     print(x * y)
#
#
# multiply(5, 4, 3)
"""TypeError: multiply() takes 2 positional arguments but 3 were given"""


# def multiply(*args):
#     z = 1
#     for num in args:
#         z *= num
#     print(z)
#
#
# multiply(4, 5)
# multiply(10, 9)
# multiply(2, 3, 4)
# multiply(3, 5, 10, 6)

"""По сути, мы можем создать ту же функцию и код, которые показали в первом примере, убрав x и y 
как параметры функции и вместо этого заменив их на *args:"""


def print_kwargs(**kwargs):
    print(kwargs)


print_kwargs(kwargs_1="Shark", kwargs_2=4.5, kwargs_3=True)


"""Как и *args, **kwargs может принимать столько аргументов, сколько вам нужно. Однако **kwargs отличается от *args тем, 
что здесь требуется назначить ключевые слова."""


def print_values(**kwargs):
    for key, value in kwargs.items():
        print("Значение для {} является {}".format(key, value))


print_values(
    name_1="Alex",
    name_2="Gray",
    name_3="Harper",
    name_4="Phoenix",
    name_5="Remy",
    name_6="Val"
)
"""Мы также можем изменить программу выше для итерации списка с другим названием переменной. 
Давайте также объединим синтаксис *args с именованным параметром:"""

def some_args(arg_1, arg_2, arg_3):
    print("arg_1:", arg_1)
    print("arg_2:", arg_2)
    print("arg_3:", arg_3)


my_list = [2, 3]
some_args(1, *my_list)

""""""
""""""
""""""
