import math

class Point:
    def __init__(self, x, y):
        """Инициализация координат точки."""
        self.x = x
        self.y = y

    def distance_to(self, other_point):
        """Вычисление расстояния до другой точки."""
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        dist = math.sqrt(dx**2 + dy**2)
        return dist

    def get_coordinates(self):
        """Получение координат."""
        return self.x, self.y

    def set_coordinates(self, x, y):
        """Изменение координат."""
        self.x = x
        self.y = y

# Пример использования:
point1 = Point(3, 4)
point2 = Point(6, 8)
dist = point1.distance_to(point2)
print("Расстояние:", dist) # Печатает: Расстояние: 5.0

coords = point1.get_coordinates()
print("Координаты точки 1:", coords) # Печатает: Координаты точки 1: (3, 4)

point1.set_coordinates(1, 2)
new_coords = point1.get_coordinates()
print("Новые координаты точки 1:", new_coords) # Печатает: Новые координаты точки 1: (1, 2)