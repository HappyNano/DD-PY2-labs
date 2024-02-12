from typing import List


class Point:
    """Класс точки с координатами X и Y."""
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Point({self.x}, {self.y})"

    def __repr__(self) -> str:
        return self.__str__()


def get_length(a: Point, b: Point) -> float:
    return ((b.x - a.x) ** 2 + (b.y - a.y) ** 2) ** 0.5


class Figure:
    """Базовый класс для фигуры."""
    def __init__(self, points: List[Point]):
        if len(points) < 3:
            raise ValueError("Not enough points")
        self.points = points

    def calculate_area(self) -> float:
        """Абстрактный метод для вычисления площади фигуры."""
        raise NotImplementedError("Subclasses must implement this method.")

    def calculate_perimeter(self) -> float:
        """Метод для вычисления периметра фигуры"""
        perimeter = 0.0

        n = len(self.points)
        for i in range(n):
            perimeter += get_length(self.points[i], self.points[(i + 1) % n])

        return perimeter

    def __str__(self) -> str:
        return f"{self.__class__.__name__} with points: {', '.join(str(point) for point in self.points)}"

    def __repr__(self) -> str:
        points_repr = ", ".join(repr(point) for point in self.points)
        return f"{self.__class__.__name__}({points_repr})"


class Triangle(Figure):
    """Дочерний класс - Треугольник."""
    def __init__(self, points: List[Point]):
        if len(points) != 3:
            raise ValueError("A triangle requires 3 points")
        super().__init__(points)

    def calculate_area(self) -> float:
        """Перегруженный метод для вычисления площади треугольника."""
        # Формула Герона для вычисления площади треугольника по координатам вершин
        a = ((self.points[1].x - self.points[0].x)**2 + (self.points[1].y - self.points[0].y)**2)**0.5
        b = ((self.points[2].x - self.points[1].x)**2 + (self.points[2].y - self.points[1].y)**2)**0.5
        c = ((self.points[0].x - self.points[2].x)**2 + (self.points[0].y - self.points[2].y)**2)**0.5

        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c))**0.5
        return area


class Polygon(Figure):
    """Дочерний класс - Квадрат."""
    def __init__(self, points: List[Point]):
        super().__init__(points)

    def calculate_area(self) -> float:
        """Перегруженный метод для вычисления площади полигона."""
        n = len(self.points)
        area = 0.0
        for i in range(n):
            j = (i + 1) % n
            area += self.points[i].x * self.points[j].y
            area -= self.points[j].x * self.points[i].y
        area = abs(area) / 2.0
        return area


if __name__ == "__main__":
    # Пример использования классов:
    point1 = Point(0, 0)
    point2 = Point(3, 0)
    point3 = Point(3, 4)

    triangle = Triangle([point1, point2, point3])
    print(triangle)
    print(repr(triangle))
    print(f"Triangle perimeter: {triangle.calculate_perimeter()}")  # 12
    print(f"Triangle area: {triangle.calculate_area()}")  # 6

    point_1 = Point(0, 0)
    point_2 = Point(2, 0)
    point_3 = Point(2, 2)
    point_4 = Point(0, 2)

    polygon = Polygon([point_1, point_2, point_3, point_4])
    print(polygon)
    print(repr(polygon))
    print(f"Polygon perimeter: {polygon.calculate_perimeter()}")  # 8
    print(f"Polygon area: {polygon.calculate_area()}")  # 4
