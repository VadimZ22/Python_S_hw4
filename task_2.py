

# Напишите функцию принимающую на вход только ключевые параметры и
# возвращающую словарь, где ключ — значение переданного аргумента,
# а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.
from collections.abc import Hashable


def make_dict(**kwargs):
    new_dict = {}
    for key, value in kwargs.items():
        if isinstance(value, Hashable):
            new_dict[value] = key
        else:
            new_dict[str(value)] = key
    return new_dict

dict = {'name': 'Alice', 'age': 20, 'number':2542, 'hobby':['run', 'swimming', 'dance']}
print(make_dict(**dict))