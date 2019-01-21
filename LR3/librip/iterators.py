# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self,a,IsRegSame):
        self.DataArrary = []
        for i in a:
            if IsRegSame:
                i = str(i).lower()
            self.IsUnique = True
            for j in self.DataArrary:
                if i == j:
                    self.IsUnique = False
            if self.IsUnique:
                self.DataArrary.append(i)
        self.NumOfElem = len(self.DataArrary)-1
        self.i = -1

    def __next__(self):
        if self.NumOfElem>self.i:
            self.i = self.i + 1
            return self.DataArrary[self.i]
        else:
            raise StopIteration

    def __iter__(self):
        return self

