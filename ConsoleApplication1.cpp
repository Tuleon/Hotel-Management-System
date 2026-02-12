#include <iostream>
#include <string>

class Hotel {
private:
    std::string name;          // Название гостиницы
    int occupiedRooms;         // Число заселенных мест
    int totalRooms;           // Общее число мест
    double dailyRate;         // Оплата за день проживания

public:
    // Конструктор
    Hotel(const std::string& hotelName, int total, double rate)
        : name(hotelName), occupiedRooms(0), totalRooms(total), dailyRate(rate) {
    }

    // Свойства (геттеры)
    std::string getName() const {
        return name;
    }

    int getOccupiedRooms() const {
        return occupiedRooms;
    }

    int getTotalRooms() const {
        return totalRooms;
    }

    double getDailyRate() const {
        return dailyRate;
    }

    // Свойства только для записи
    void setName(const std::string& newName) {
        name = newName;
    }

    void setDailyRate(double newRate) {
        if (newRate > 0) {
            dailyRate = newRate;
        }
    }

    // Методы для управления заселением
    bool checkIn(int rooms = 1) {
        if (occupiedRooms + rooms <= totalRooms) {
            occupiedRooms += rooms;
            return true;
        }
        return false;
    }

    bool checkOut(int rooms = 1) {
        if (occupiedRooms - rooms >= 0) {
            occupiedRooms -= rooms;
            return true;
        }
        return false;
    }

    // Метод для подсчета общей выручки
    double calculateRevenue(int days) const {
        return occupiedRooms * dailyRate * days;
    }

    // Информация о гостинице
    void displayInfo() const {
        std::cout << "Гостиница: " << name << std::endl;
        std::cout << "Занято мест: " << occupiedRooms << "/" << totalRooms << std::endl;
        std::cout << "Стоимость в день: " << dailyRate << " руб." << std::endl;
    }
};

// ГЛАВНАЯ ФУНКЦИЯ - ОБЯЗАТЕЛЬНО ДЛЯ КОМПИЛЯЦИИ
int main() {
    setlocale(LC_ALL, "RUS");
    // Создание гостиницы
    Hotel hotel("Гранд Отель", 100, 2500.0);

    // Вывод информации
    hotel.displayInfo();
    std::cout << std::endl;

    // Заселение гостей
    hotel.checkIn(0);
    hotel.checkIn(0);
    std::cout << "После заселения: " << hotel.getOccupiedRooms() << " занято" << std::endl;

    // Выселение гостей
    hotel.checkOut(2);
    std::cout << "После выселения: " << hotel.getOccupiedRooms() << " занято" << std::endl;
    std::cout << std::endl;

    // Расчет выручки за 7 дней
    double revenue = hotel.calculateRevenue(7);
    std::cout << "Выручка за 7 дней: " << revenue << " руб." << std::endl;

    // Использование свойств только для записи
    hotel.setName("Люкс Отель");
    hotel.setDailyRate(3000.0);

    std::cout << "\nПосле обновления:" << std::endl;
    hotel.displayInfo();

    return 0;
}