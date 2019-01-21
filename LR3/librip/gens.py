import random


# Генератор вычленения полей из массива словарей
# Пример:
# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

def field(a, *args):
    for k in a:
        s = []
        for t,w in k.items():
            for el in args:
                if len(args) == 1:
                    if el == t:
                         yield w
                elif len(args) > 1:
                    if el == t and w is None:
                            yield [t,w]


# Генератор списка случайных чисел
# Пример:
# gen_random(1, 3, 5) должен выдать примерно 2, 2, 3, 2, 1
# Hint: реализация занимает 2 строки
def gen_random1(a, b, c):
    i = 0
    s = []
    while i < c:
        s.append(random.randint(a, b))
        i += 1
    yield s

def gen_random(a, b, c):
    i = 0
    while i < c:
        yield random.randint(a, b)
        i += 1
