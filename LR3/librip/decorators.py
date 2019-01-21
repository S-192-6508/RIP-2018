# Здесь необходимо реализовать декоратор, print_result который принимает на вход функцию,
# вызывает её, печатает в консоль имя функции, печатает результат и возвращает значение
# Если функция вернула список (list), то значения должны выводиться в столбик
# Если функция вернула словарь (dict), то ключи и значения должны выводить в столбик через знак равно
def print_result(func_to_decorate):
    def decorated_func(*args):
        print(func_to_decorate.__name__)
        if type(func_to_decorate(*args)) == list:
            for j in func_to_decorate(*args):
                print(j)
        elif type(func_to_decorate(*args)) == dict:
            for i,j in func_to_decorate(*args).items():
                print(i,"=",j)
        else:
            print(func_to_decorate(*args))
        print("\n")
        return func_to_decorate(*args)
    return decorated_func


