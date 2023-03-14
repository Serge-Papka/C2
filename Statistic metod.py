# Напишите класс SquareFactory с одним статическим методом, принимающим единственный аргумент — сторону квадрата.
# Данный метод должен возвращать объект класса Square с переданной стороной.

class Square:
    def __init__(self, side):
        self.side = side
class SquareFactory:
    @staticmethod
    def klass(side):
        return Square(side)
SquareFactory()





sq1 = SquareFactory.klass(34)
print(sq1.side)
