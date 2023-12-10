class Car:
    """Класс, описывающий автомобиль"""

    def __init__(self, make: str, model: str, year: int):
        """
        Инициализация объекта Car

        Args:
            make (str): Марка автомобиля
            model (str): Модель автомобиля
            year (int): Год выпуска автомобиля
        """
        if year > 2023:
            raise ValueError("Год выпуска не может быть будущим годом")
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self) -> str:
        """
        Запускает двигатель автомобиля.

        Returns:
            str: Сообщение о том, что двигатель запущен

        Examples:
            >>> car = Car("Toyota", "Camry", 2022)
            >>> car.start_engine()
            'Двигатель запущен'
        """
        return 'Двигатель запущен'

    def drive(self, distance: float) -> str:
        """
        Осуществляет поездку на указанное расстояние

        Args:
            distance (float): Расстояние, которое нужно проехать

        Returns:
            str: Сообщение о пройденном расстоянии

        Examples:
            >>> car = Car("Toyota", "Camry", 2022)
            >>> car.drive(50.5)
            'Проехали 50.5 км'
        """
        return f'Проехали {distance} км'


class Book:
    """Класс, описывающий книгу"""

    def __init__(self, title: str, author: str, pages: int):
        """
        Инициализация объекта Book

        Args:
            title (str): Название книги
            author (str): Автор книги
            pages (int): Количество страниц в книге
        """
        if pages < 0:
            raise ValueError("Количество страниц не может быть отрицательным")
        self.title = title
        self.author = author
        self.pages = pages

    def open_book(self) -> str:
        """
        Открывает книгу для чтения

        Returns:
            str: Сообщение о том, что книга открыта

        Examples:
            >>> book = Book("Война и мир", "Лев Толстой", 1225)
            >>> book.open_book()
            'Книга открыта'
        """
        return 'Книга открыта'

    def close_book(self) -> str:
        """
        Закрывает книгу

        Returns:
            str: Сообщение о том, что книга закрыта

        Examples:
            >>> book = Book("Война и мир", "Лев Толстой", 1225)
            >>> book.close_book()
            'Книга закрыта'
        """
        return 'Книга закрыта'


class Tree:
    """Класс, описывающий дерево"""

    def __init__(self, species: str, age: int, height: float):
        """
        Инициализация объекта Tree

        Args:
            species (str): Вид дерева
            age (int): Возраст дерева
            height (float): Высота дерева в метрах
        """
        if height < 0:  # Предположим, что дерево не может иметь отрицательную высоту
            raise ValueError("Высота дерева не может быть отрицательной")
        self.species = species
        self.age = age
        self.height = height

    def grow(self, growth_rate: float) -> str:
        """
        Увеличивает высоту дерева на указанную величину

        Args:
            growth_rate (float): Величина увеличения высоты дерева

        Returns:
            str: Сообщение о том, на сколько выросло дерево

        Examples:
            >>> tree = Tree("Дуб", 30, 15.5)
            >>> tree.grow(0.5)
            'Дерево выросло на 0.5 метра'
        """
        self.height += growth_rate
        return f'Дерево выросло на {growth_rate} метра'


if __name__ == "__main__":
    import doctest
    doctest.testmod()
