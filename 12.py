class Hotel:
    def __init__(self, name: str, total_rooms: int, daily_rate: float):
        self.__name = name              # Название гостиницы (приватное)
        self.__occupied_rooms = 0       # Число заселенных мест (приватное)
        self.__total_rooms = total_rooms  # Общее число мест (приватное)
        self.__daily_rate = daily_rate  # Оплата за день проживания (приватное)
    
    # Свойства (геттеры)
    @property
    def name(self):
        return self.__name
    
    @property
    def occupied_rooms(self):
        return self.__occupied_rooms
    
    @property
    def total_rooms(self):
        return self.__total_rooms
    
    @property
    def daily_rate(self):
        return self.__daily_rate
    
    # Свойства только для записи
    @property
    def name_writable(self):
        raise AttributeError("Это свойство только для записи")
    
    @name_writable.setter
    def name_writable(self, new_name):
        self.__name = new_name
    
    @property
    def daily_rate_writable(self):
        raise AttributeError("Это свойство только для записи")
    
    @daily_rate_writable.setter
    def daily_rate_writable(self, new_rate):
        if new_rate > 0:
            self.__daily_rate = new_rate
    
    # Методы для управления заселением
    def check_in(self, rooms=1):
        """Заселение гостей"""
        if self.__occupied_rooms + rooms <= self.__total_rooms:
            self.__occupied_rooms += rooms
            return True
        return False
    
    def check_out(self, rooms=1):
        """Выселение гостей"""
        if self.__occupied_rooms - rooms >= 0:
            self.__occupied_rooms -= rooms
            return True
        return False
    
    # Метод для подсчета общей выручки
    def calculate_revenue(self, days):
        """Подсчет выручки за указанное количество дней"""
        return self.__occupied_rooms * self.__daily_rate * days
    
    # Информация о гостинице
    def display_info(self):
        """Отображение информации о гостинице"""
        print(f"Гостиница: {self.__name}")
        print(f"Занято мест: {self.__occupied_rooms}/{self.__total_rooms}")
        print(f"Стоимость в день: {self.__daily_rate} руб.")
    
    def __str__(self):
        return f"Hotel(name={self.__name}, occupancy={self.__occupied_rooms}/{self.__total_rooms})"


# Пример использования
def main():
    # Создание гостиницы
    hotel = Hotel("Гранд Отель", 100, 2500.0)
    
    # Вывод информации
    hotel.display_info()
    print()
    
    # Заселение гостей
    hotel.check_in(5)
    hotel.check_in(3)
    print(f"После заселения: {hotel.occupied_rooms} занято")
    
    # Выселение гостей
    hotel.check_out(2)
    print(f"После выселения: {hotel.occupied_rooms} занято")
    print()
    
    # Расчет выручки за 7 дней
    revenue = hotel.calculate_revenue(7)
    print(f"Выручка за 7 дней: {revenue} руб.")
    
    # Использование свойств только для записи
    hotel.name_writable = "Люкс Отель"
    hotel.daily_rate_writable = 3000.0
    
    print(f"\nПосле обновления:")
    hotel.display_info()


if __name__ == "__main__":
    main()
