# Здесь необходимо реализовать
# контекстный менеджер timer
# Он не принимает аргументов, после выполнения блока он должен вывести время выполнения в секундах
# Пример использования
# with timer():
#   sleep(5.5)
#
# После завершения блока должно вывестись в консоль примерно 5.5
import time
class timer:
    def __enter__(self):
        self.start = time.monotonic()
        #print('Вход в блок:',self.start)
        return self.start

    def __exit__(self, exp_type, exp_value, traceback):
        self.end = time.monotonic()
        #print('Выход из блока:',self.end)
        print("Время работы:",self.end-self.start)