from functools import reduce

# Задача №1
def str_to_int(x: list):
    return int(x)

str_lst = ['1', '20', '300']

int_lst = map(str_to_int, str_lst)

print(list(int_lst))

# Задача №2
def is_even(x: list):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = filter(is_even, numbers)

print(list(even_numbers))

# Задача №3
def square(x: list):
    return x ** 2

numbers = [1, 2, 3, 4]

squared_numbers = map(square, numbers)

print(list(squared_numbers))

# Задача №4
def three_symbols_rule(x: list):
    return len(x) > 3

words = ['cat', 'elephant', 'dog', 'tiger']

filtered_list = filter(three_symbols_rule, words)

print(list(filtered_list))

# Задача №5
numbers = [1, 2, 3, 4, 5]
print(reduce(lambda x, y: x*y, numbers))

# Задача №6
words = ['hello', 'world', 'Python']
print(list(map(lambda x: len(x), words)))

# Задача №7
words = ["apple", "banana", "pear", "strawberry"]
print(len(reduce(lambda x,y: x if len(x) > len(y) else y, words)))

# Задача №8
words = ["hello", "world"]
print(list(map(lambda x: x.upper(), words)))

# Задача №9
words = ["1", "2", "3", "4"]
print(list(filter(is_even, map(square, map(str_to_int, words)))))

# Задача №10
numbers = [-2, 3, -4, 5, 6]
print(reduce(lambda x,y: x*y, filter(lambda x: x >= 0, numbers)))

# Задача №11
#-

# Задача №12
words = ["racecar", "hello", "level", "world"]
print(list(filter(lambda x: x == x[::-1], map(lambda x: x[::-1], words))))

# Задача на создание Функций-Генераторов

# Задача №1.1
def five_multiples_generator():
    x = 5
    while True:
        yield x
        x += 5

# Задача №1.2
def squares_generator():
    x = 1
    while True:
        yield x ** 2
        x += 1

# Задача №1.3
def without_3_multiples_generator(n):
    for i in range(1, n):
        if i % 3 != 0:
            yield i

# Задача №1.4
def count_substrings_generaotr(word, lenght):
    while len(word) >= lenght:
        yield word[0:lenght:1]
        word = word[1::]

# Задача №1.5
def doubled_in_range(a, b):
    for i in range(a, b + 1, 2):
        yield i

print(list(doubled_in_range(1, 10)))