import unittest
class TestCutRectangle(unittest.TestCase):

    def test_one_square(self):
        self.assertEqual(cut_rectangle(5, 5), 1)
def cut_rectangle(a, b):
    if a == b: # базовый случай, когда можно получить только один квадрат
        print("Длина стороны квадрата:", a)
        return 1
    elif a > b: # находим максимально возможный размер квадрата
        print("Длина стороны квадрата:", b)
        return 1 + cut_rectangle(a-b, b) # рекурсивный вызов для оставшейся части прямоугольника
    else:
        print("Длина стороны квадрата:", a)
        return 1 + cut_rectangle(a, b-a) # рекурсивный вызов для оставшейся части прямоугольника

# пример использования функции
a = int(input("Введите длину прямоугольника: "))
b = int(input("Введите ширину прямоугольника: "))
num_squares = cut_rectangle(a, b)
print("Количество квадратов:", num_squares)

