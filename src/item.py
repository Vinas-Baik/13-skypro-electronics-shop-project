import csv
import os

CSV_FILE = '..\src\items.csv'

def nice_number_output(number) -> str:
    """
    возвращает красиво номер 100000.011 в виде "100 000.011'
    """
    # 10200300.01          10200300         - исходная
    # 10.00300201          00300201         - переворот строки
    # 01234567890          01234567         - позиция в строке
    # 10.003 002 01        003 002 01       - расcтавляем пробелы
    # 10 200 300.01        10 200 300       - переворачиваем обратно
    result = ''
    str_number = str(number)
    # ищем точку в числе
    if str_number.count('.') > 0:
        is_dot = False                  # переменная - Точка найдена и пройдена
        index_dot = 0                   # позиция точки в строке
        # число преобразуем в строку и переворачиваем строку к виду
        # было '10000.01' -> стало '10.00001' - для удобства работы с числом
        for i, str_n in enumerate(str_number[::-1]):
            result = str_n + result
            if is_dot:
                if (i - index_dot) % 3 == 0:   # ставим пробел после каждого 3го нуля
                    result = ' ' + result
            if str_n == '.':   # найдена . - значит дробная часть закончилась
                is_dot = True
                index_dot = i
    else:
        # точки нет - выводим число с пробелами
        for i, str_n in enumerate(str_number[::-1]):
            result = str_n + result
            if i % 3 == 2:
                result = ' ' + result

    return result

def full_path_name_file(name_file):
    """
    формируем полный путь до файла
    :param name_file: имя файла с указанием подпапки
    :return: полный пусть в UNIX системы
    """
    # return os.getcwd() + '\\' + name_file
    # return os.path.join(*name_file.replace('\\','/').split('/'))
    # cur_path = os.path.dirname(__file__)
    return os.path.realpath(name_file)


class Item:
    """
    Класс для представления товара в магазине.
    """
    # скидка на товар (100% - 15%)
    pay_rate = 0.85
    all = []

    def __init__(self, name: str, price: float, quantity=1) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине, по умолчанию 1
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name[:10]          # обрезаем до 10 символов


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price*self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    def __repr__(self):
        """
        метод __repr___
        """
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """
        метод __str___
        """
        # return f'{self.__name} в количестве {self.quantity} шт ' \
        #        f'по цене {self.price} руб.'
        return f'{self.__name}'


    @classmethod
    def instantiate_from_csv(cls):
        """
        класс-метод, инициализирующий экземпляры класса Item данными из файла items.csv
        """
        cls.all = []
        name_file = full_path_name_file(CSV_FILE)

        with open(name_file, newline='') as file:
            reader = csv.DictReader(file)
                # item1 = my_item.Item("Смартфон", 10000, 20)
                # name, price, quantity

            for row in reader:
                Item(row['name'], int(row['price']), int(row['quantity']))

    @staticmethod
    def string_to_number(text: str):
        """
        статический метод, возвращающий число из числа-строки
        """
        return int(float(text))




# проверяем работу класса
# temp_item = Item('Молоко 3,5%', 95, 5)
# print(repr(temp_item))
# print(f'{temp_item}, Итоговая сумма = {temp_item.calculate_total_price()} руб.')
# print(f'Применяем скидку {int((1-temp_item.pay_rate)*100)}%')
# temp_item.apply_discount()
# print(repr(temp_item))
# print(f'{temp_item}, Итоговая сумма = {temp_item.calculate_total_price()} руб.')
# print(nice_number_output(10000000))
# print(nice_number_output(10000000.0111))

# Item.instantiate_from_csv()
# print(Item.all)
# print(len(Item.all))
# for row in Item.all:
#     print(row)
