class Hotel:
    def __init__(self, name: str, total_seats: int, occupied_seats: int, daily_payment: float):
        self.__name = name
        self.__occupied_seats = occupied_seats
        self.__total_seats = total_seats
        self.__daily_payment = daily_payment
    
    # Свойства (геттеры)
    @property
    def name(self):
        return self.__name
    
    @property
    def occupied_seats(self):
        return self.__occupied_seats
    
    @property
    def total_seats(self):
        return self.__total_seats
    
    @property
    def daily_payment(self):
        return self.__daily_payment
    
    # Свойства только для записи
    @property
    def write_only_name(self):
        raise AttributeError("Это свойство только для записи")
    
    @write_only_name.setter
    def write_only_name(self, new_name):
        self.__name = new_name
    
    @property
    def write_only_payment(self):
        raise AttributeError("Это свойство только для записи")
    
    @write_only_payment.setter
    def write_only_payment(self, new_payment):
        if new_payment > 0:
            self.__daily_payment = new_payment
    
    # Метод для подсчета общей выручки
    def calculate_revenue(self, days):
        return self.__occupied_seats * self.__daily_payment * days
    
    def display_info(self):
        print("\n=== Информация о гостинице ===")
        print(f"Название: {self.__name}")
        print(f"Занято мест: {self.__occupied_seats}/{self.__total_seats}")
        print(f"Стоимость в день: {self.__daily_payment} руб.")


def get_valid_int(prompt, min_value=0, max_value=10000):
    """Функция для проверки ввода целого числа"""
    while True:
        try:
            value = input(prompt)
            # Проверка на пустую строку
            if not value.strip():
                print("Ошибка! Ввод не может быть пустым.")
                continue
            
            value = int(value)
            
            if value < min_value:
                print(f"Ошибка! Значение не может быть меньше {min_value}.")
            elif value > max_value:
                print(f"Ошибка! Значение не может быть больше {max_value}.")
            else:
                return value
        except ValueError:
            print("Ошибка! Введите целое число, а не текст или символы.")


def get_valid_float(prompt, min_value=0.0, max_value=100000.0):
    """Функция для проверки ввода числа с плавающей точкой"""
    while True:
        try:
            value = input(prompt)
            # Проверка на пустую строку
            if not value.strip():
                print("Ошибка! Ввод не может быть пустым.")
                continue
            
            value = float(value)
            
            if value < min_value:
                print(f"Ошибка! Значение не может быть меньше {min_value}.")
            elif value > max_value:
                print(f"Ошибка! Значение не может быть больше {max_value}.")
            else:
                return value
        except ValueError:
            print("Ошибка! Введите число, а не текст или символы.")


def get_valid_name(prompt):
    """Функция для проверки ввода названия (только буквы, пробелы, дефисы)"""
    while True:
        value = input(prompt).strip()
        
        # Проверка на пустую строку
        if not value:
            print("Ошибка! Название не может быть пустым.")
            continue
        
        # Проверка, что строка содержит только буквы, пробелы и дефисы
        valid = True
        for char in value:
            if not (char.isalpha() or char.isspace() or char == '-'):
                valid = False
                break
        
        if not valid:
            print("Ошибка! Название должно содержать только буквы, пробелы и дефисы.")
        else:
            return value


def main():
    print("=== Введите данные о гостинице ===")
    
    # Ввод названия с проверкой
    name = get_valid_name("Название гостиницы: ")
    
    # Ввод общего числа мест с проверкой
    total_seats = get_valid_int("Общее число мест: ", 0, 10000)
    
    # Ввод числа заселенных мест с проверкой
    while True:
        occupied_seats = get_valid_int("Число заселенных мест: ", 0, total_seats)
        if occupied_seats <= total_seats:
            break
        print("Ошибка! Занятых мест не может быть больше общих.")
    
    # Ввод оплаты с проверкой
    daily_payment = get_valid_float("Оплата за день проживания (руб.): ", 0, 100000.0)
    
    # Ввод количества дней с проверкой
    days = get_valid_int("Количество дней для расчета выручки: ", 0, 365)
    
    # Создание объекта с пользовательскими данными
    hotel = Hotel(name, total_seats, occupied_seats, daily_payment)
    
    # Вывод информации
    hotel.display_info()
    
    # Подсчет выручки
    revenue = hotel.calculate_revenue(days)
    print(f"\nОБЩАЯ ВЫРУЧКА за {days} дней: {revenue:,.2f} руб.")


if __name__ == "__main__":
    main()
