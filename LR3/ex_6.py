#!/usr/bin/env python3
import json
import sys
from librip.ctxmngrs import timer
from librip.decorators import print_result
from librip.gens import field, gen_random
from librip.iterators import Unique as unique
import random
import os

path = os.path.join('data_light.json')

# Здесь необходимо в переменную path получить
# путь до файла, который был передан при запуске

with open(path,  'r', encoding='utf-8') as f:
    data = json.load(f)

# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Важно!
# Функции с 1 по 3 дожны быть реализованы в одну строку
# В реализации функции 4 может быть до 3 строк
# При этом строки должны быть не длиннее 80 символов



@print_result
def f1(args):
    return list(sorted(set([args[prof_el]["job-name"].lower() for prof_el in range(len(args))])))

@print_result
def f2(args):
    return list(filter(lambda x: x.startswith("программист"),args))

@print_result
def f3(args):
    return list(map(lambda x: x+" с опытом Python",args))

@print_result
def f4(args):
    SalArr=[", зарплата "+str(random.randint(100000, 200000))+" руб." for x in range(len(args))]
    return list(zip(args,SalArr))

with timer():
    f4(f3(f2(f1(data))))