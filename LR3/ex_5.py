from time import sleep
from librip.ctxmngrs import timer

with timer() as test:
    print(test)
    sleep(5.5)
