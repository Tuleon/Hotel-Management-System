#include <iostream>
#include <string>

class Hotel {
private:
    std::string name;          // Название гостиницы
    int occupiedSeats;         // Число заселенных мест
    int totalSeats;           // Общее число мест
    double dailyPayment;      // Оплата за день проживания

public:
    // Конструктор
    Hotel(const std::string& hotelName, int total, int occupied, double payment)
        : name(hotelName), occupiedSeats(occupied), totalSeats(total), dailyPayment(payment) {
    }

    // Свойства (геттеры)
    std::string getName() const {
        return name;
    }

    int getOccupiedSeats() const {
        return occupiedSeats;
    }

    int getTotalSeats() const {
        return totalSeats;
    }

    double getDailyPayment() const {
        return dailyPayment;
    }

    // Свойства только для записи
    void setName(const std::string& newName) {
        name = newName;
    }

    void setDailyPayment(double newPayment) {
        if (newPayment > 0) {
            dailyPayment = newPayment;
        }
    }

    // Метод для подсчета общей выручки
    double calculateRevenue(int days) const {
        return occupiedSeats * dailyPayment * days;
    }

    void displayInfo() const {
        std::cout << "\n=== Информация о гостинице ===" << std::endl;
        std::cout << "Название: " << name << std::endl;
        std::cout << "Занято мест: " << occupiedSeats << "/" << totalSeats << std::endl;
        std::cout << "Стоимость в день: " << dailyPayment << " руб." << std::endl;
    }
};

int main() {
    setlocale(LC_ALL, "Russian");

    std::string name;
    int totalSeats, occupiedSeats, days;
    double dailyPayment;

    // ПОЛЬЗОВАТЕЛЬ ВВОДИТ ВСЕ ДАННЫЕ
    std::cout << "=== Введите данные о гостинице ===" << std::endl;

    std::cout << "Название гостиницы: ";
    std::getline(std::cin, name);

   
    std::cout << "Общее число мест: ";
    std::cin >> totalSeats;
    
        while (std::cin.fail() or std::cin.peek() != '\n' or 0>totalSeats) {
            std::cin.clear();
            std::cin.ignore((std::numeric_limits<std::streamsize>::max)(), '\n');
            std::cout << "Ошибка: Введите нормальное число\n";
            std::cout << "Общее число мест: ";
            std::cin >> totalSeats;
        }
        
  

   
        std::cout << "Число заселенных мест: ";
        std::cin >> occupiedSeats;
        while (std::cin.fail() or std::cin.peek() != '\n' or occupiedSeats<0) {
            std::cin.clear();
            std::cin.ignore((std::numeric_limits<std::streamsize>::max)(), '\n');
            std::cout << "Ошибка: Введите нормальное число\n";
            std::cout << "Число заселенных мест: ";
            std::cin >> occupiedSeats;
        }
        
    
    // Проверка, чтобы занятых мест не было больше общих
    while (occupiedSeats > totalSeats) {
        std::cout << "Ошибка! Занятых мест не может быть больше общих." << std::endl;
        std::cout << "Число заселенных мест: ";
        std::cin >> occupiedSeats;
    }
    
        std::cout << "Оплата за день проживания (руб.): ";
        std::cin >> dailyPayment;
        while (std::cin.fail() or std::cin.peek() != '\n' or dailyPayment < 0) {
            std::cin.clear();
            std::cin.ignore((std::numeric_limits<std::streamsize>::max)(), '\n');
            std::cout << "Ошибка: Введите нормальное число\n";
            std::cout << "Оплата за день проживания (руб.): ";
            std::cin >> dailyPayment;
        }
        
    
    
        std::cout << "Количество дней для расчета выручки: ";
        std::cin >> days;
        while (std::cin.fail() or std::cin.peek() != '\n' or days < 0) {
            std::cin.clear();
            std::cin.ignore((std::numeric_limits<std::streamsize>::max)(), '\n');
            std::cout << "Ошибка: Введите нормальное число\n";
            std::cout << "Количество дней для расчета выручки: ";
            std::cin >> days;
        }
        
    
    // Создание объекта с пользовательскими данными
    Hotel hotel(name, totalSeats, occupiedSeats, dailyPayment);

    // Вывод информации
    hotel.displayInfo();

    // Подсчет выручки
    double revenue = hotel.calculateRevenue(days);
    std::cout << "\nОБЩАЯ ВЫРУЧКА за " << days << " дней: " << revenue << " руб." << std::endl;

    return 0;
}