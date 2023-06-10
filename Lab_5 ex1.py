#итератор, возвращающий генератор трибоначчи
class Tribonacci:
    def __init__(self, n):
        self.n = n
    
    def __iter__(self):
        return self.tribonacci_generator()
    
    def tribonacci_generator(self):
        a, b, c = 0, 0, 1
        for i in range(self.n):
            yield c
            a, b, c = b, c, a + b + c

tribonacci_iterator = iter(Tribonacci(35))

for i in tribonacci_iterator:
    print(i)
