class CheckingTypeExcepion(Exception):  # Исключение будет проверять тип у параметра Количество
    def __init__(self):  # и если он str будет выдавать ошибку и НЕ записывать товар на склад;
        pass

    def __str__(self):
        return f"ОШИБКА!!! Проверьте параметр 'Количество' = int!"


class Warehouse:  # склад
    departments = {'0': 'Склад', '1': 'Отдел финансов', '2': 'Отдел кадров'}

    def __init__(self):
        self.warehouse_0 = []
        self.warehouse_1 = []
        self.warehouse_2 = []

    def coming_equipment(self, item):  # метод приема оргтехники на склад
        try:
            if type(item.quantity) == int:
                self.warehouse_0.append(item)
                return f"На склад поступил товар: [{item}]"
            else:
                raise CheckingTypeExcepion()
        except CheckingTypeExcepion as error:
            print(error)
        return f"Товар: [{item}] не добавлен на склад!"

    def outgoing_equipment(self, item):  # метод передачи оргтехники в подразделение компании
        user_input = input("Введите номер отдела для передачи товара: 1 - Отдел финансов, 2 - Отдел кадров >>> ")
        if user_input == '1':
            self.warehouse_1.append(item)
            self.warehouse_0.remove(item)
            return f"В отдел финансов поступил {len(self.warehouse_1)} товар."
        elif user_input == '2':
            self.warehouse_2.append(item)
            self.warehouse_0.remove(item)
            return f"В отдел кадров поступил {len(self.warehouse_2)} товар."
        else:
            return f"Неверный номер отдела!"

    def report(self):
        num = len(self.warehouse_0)
        num1 = len(self.warehouse_1)
        num2 = len(self.warehouse_2)
        if num == 1:
            print(f"На складе храниться {num} оргтехника:")
        else:
            print(f"На складе храниться {num} оргтехники:")
        for item in self.warehouse_0:
            print(item)
        if num1 == 1:
            print(f"В отделе финансов храниться {num1} оргтехника:")
        else:
            print(f"В отделе финансов храниться {num1} оргтехники:")
        for item in self.warehouse_1:
            print(item)
        if num2 == 1:
            print(f"В отделе кадров храниться {num2} оргтехника:")
        else:
            print(f"В отделе кадров храниться {num2} оргтехники:")
        for item in self.warehouse_2:
            print(item)


class OfficeEquipment:  # оргтехника
    type_equipment: str  # тип техники
    brand: str  # производитель
    price: int  # цена
    quantity: int  # количество

    def __init__(self, type_equipment, brand, price, quantity):
        self.type_equipment = type_equipment
        self.brand = brand
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Тип: {self.type_equipment}, Производитель: {self.brand}," \
               f" Цена: {self.price}, Количество: {self.quantity}"


class Printer(OfficeEquipment):
    paper_size: str  # размер бумаги

    def __init__(self, type_equipment, brand, price, quantity, paper_size):
        super().__init__(type_equipment, brand, price, quantity)
        self.paper_size = paper_size

    def __str__(self):
        return f"Тип: {self.type_equipment}, Производитель: {self.brand}, Цена: {self.price}, " \
               f"Количество: {self.quantity}, Размер бумаги: {self.paper_size}"


class Scaner(OfficeEquipment):
    resolution: int  # разрешение

    def __init__(self, type_equipment, brand, price, quantity, permission):
        super().__init__(type_equipment, brand, price, quantity)
        self.resolution = permission

    def __str__(self):
        return f"Тип: {self.type_equipment}, Производитель: {self.brand}, Цена: {self.price}," \
               f" Количество: {self.quantity}, Разрешение: {self.resolution}"


class Copy(OfficeEquipment):
    format: str  # формат А4 или А3

    def __init__(self, type_equipment, brand, price, quantity, format):
        super().__init__(type_equipment, brand, price, quantity)
        self.format = format

    def __str__(self):
        return f"Тип: {self.type_equipment}, Производитель: {self.brand}, Цена: {self.price}," \
               f" Количество: {self.quantity}, Формат: {self.format}"


sklad = Warehouse()

p = Printer("Принтер", "Epson 200", 25000, 1, "A4")
s = Scaner("Сканер", "Mustek 1500", 15000, 1, 1200)
c = Copy("Копир", "Xerox 2021", 30000, 1, "A3")
y = Printer("Принтер", "Canon 450", 13000, "Error", "A4")
# вызов метода приема оргтехники на склад
print("1. Работа метода приема товара на склад:")
print(sklad.coming_equipment(p))
print(sklad.coming_equipment(s))
print(sklad.coming_equipment(c))
print(sklad.coming_equipment(y))
print()

print("2. Работа метода передачи оргтехники в подразделение компании:")
sklad.report()
print()
# вызов метода передачи оргтехники в подразделение компании
print(sklad.outgoing_equipment(p))
print(sklad.outgoing_equipment(s))
print()
# отчет оргтехника на складах
sklad.report()