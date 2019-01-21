from librip.decorators import print_result
from librip.iterators import Unique as unique
from librip.gens import gen_random
@print_result
def f1Analog(args):
    JobsArray = []
    for i in args:
        for k,d in i.items():
            if k=="job-name":
                JobsArray.append(d)
    UJ = unique(JobsArray,True)
    UJA=[]
    f = True
    while f:
        try:
            UJA.append(next(UJ))
        except StopIteration:
            f = False
    UJA = sorted(UJA)
    return (UJA)

#@print_result
def f4Analog(args):
    Sal=gen_random(100000, 200000, len(args))
    return list(map(lambda x: x + ", зарплата "+str(next(Sal))+" руб.", args))