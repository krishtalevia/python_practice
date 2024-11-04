# Задача №1.1
def reverse_generator(a: int, b: int):
    for i in range(a, b - 1, -1):
        yield i

# Задача №1.2
def five_divisible_fibonacci_generator():
    a, b = 0, 1
    while True:
        if b % 5 == 0:
            yield b

        a, b = b, b + a

# Задача №1.3
def factorial_generator():
    n = 1
    curr_factorial = 1
    while True:
        yield curr_factorial
        n += 1
        curr_factorial *= n

# Задача №1.4
# -

# Задача №1.5
def unique_words_generator(line: str):
    line = line.split(' ')
    for word in line:
        if is_unique(word, line) == True:
            yield word

def is_unique(word, line_list: list):
    word_count = 0
    for i in line_list:
        if i == word:
            word_count += 1
        
        if word_count > 1:
            return False
        
    return True

# Задача №1.6
def above_k_letters_generator(line: str, k: int):
    line = line.replace(',', '')
    line = line.split(' ')

    line = sort(line)

    for word in line:
        if word > k:
            yield word


def sort(lst, order_by = lambda x, y: x > y):
    for i in range(0, len(lst), 1):
        for j in range(0, len(lst) - i - 1, 1):
            if order_by(lst[j], lst[j + 1]):
                lst[j], lst[j + 1] = lst[j+ 1], lst[j]
    
    return lst

# Задача №2
open_zones = ['Lobby', 'Cafeteria']

access_granted = []
access_denied = []

def requires_access(f):
    def wrapper(employee, zone):
        if zone in open_zones or zone in employee.access_zones:
            return f(employee, zone)
        else:
            f'Для {employee.__name} в {zone} доступ запрещен.'

    return wrapper

def log_access(f):
    def wrapper(employee, zone):
        result = f(employee, zone)

        if 'доступ разрешен' in result.lower():
            access_granted.append(employee.__name)
        else:
            access_denied.append(employee.__name)

        return None

    return wrapper

class Employee():
    def __init__(self, name: str, access_zones: list) -> None:
        self.__name = name
        self.__access_zones = access_zones

class SecuritySystem:
    @requires_access
    @log_access
    def enter_zone(employee, zone):
        return f'{employee.__name} входит в {zone}. Доступ разрешен.'
