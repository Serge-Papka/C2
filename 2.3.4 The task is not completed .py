# Создать вычисляемое свойство для класса Square. Сделайте метод по вычислению площади свойством.
# Сделайте сторону квадрата свойством, которое можно установить только через сеттер. В сеттере добавьте проверку
# условия, что сторона должна быть неотрицательной.
class Square:
    _a = None
    def __init__(self, a):
        self.a = a
    @property
    def a(self):
        return self._a
    @a.setter
    def a(self, value):
        if value > 0:
            self._a = value
    @property
    def area(self):
        return self.a**2