# Задача №1
def count_calls(f):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print (f'Функция была вызвана {count} раз(а)')
        return f(*args, **kwargs)
    
    return wrapper

@count_calls
def greet(name):
    print (f'Привет, {name}!')

greet('Алексей')
greet('Алексей')

# Задача №2
def type_check(*types):

    def decorator(f):

        def wrapper(*args):
            for i in args:
                if not isinstance(i, types):
                    raise TypeError('Неверный тип аргумента "{i}".')
            return f(*args)
        
        return wrapper

    return decorator

@type_check(int, int)
def add(a, b):
    return a + b

print (add(2, 3))
#print (add(2, '3'))

# Задача №3
def validate_range(min_value, max_value):

    def decorator(f):

        def wrapper(*args):
            for i in args:
                if isinstance(i, (int, float)):
                    if i < min_value or i > max_value:
                        raise ValueError(f'Аргумент имеет значение {i}, что выходит за пределы [{min_value}, {max_value}]')

            return f(*args)

        return wrapper

    return decorator

@validate_range(min_value=0, max_value=100)
def set_percentage(value):
    print(f'Установлено значение: {value}%')

set_percentage(50)
#set_percentage(150)

# Задача №4
def trace(f):
    tab_count = 0

    def wrapper(*args):
        nonlocal tab_count
        tab_count += 1
        print('\t'*tab_count, end='')
        print(f"--> Вход в функцию '{f.__name__}' с аргументами {args} \n")

        result = f(*args)

        tab_count -= 1
        print('\t'*tab_count, end='')
        print(f"--> Выход из функцию '{f.__name__}' с результатом {result} \n")

        return result

    return wrapper

@trace
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

factorial(3)


# Задача №5
def uppercase_result(f):

    def wrapper(*args):
        result = f(*args)

        if isinstance(result, str):
            result = result.upper()

        return result

    return wrapper

@uppercase_result
def get_greeting(name):
    return f"Привет, {name}"

print(get_greeting("Алексей"))  # Вывод: ПРИВЕТ, АЛЕКСЕЙ

@uppercase_result
def add_numbers(a, b):
    return a + b

print(add_numbers(2, 3))  # Вывод: 5