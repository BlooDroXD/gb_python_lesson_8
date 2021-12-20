# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
# (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, date: str):
        self.date = date
    def __str__(self):
        return f"Date is {self.date}"
    @classmethod
    def extract_date(cls, date):
        temp_date = date.split("-")
        cls.days = int(temp_date[0])
        cls.month = int(temp_date[1])
        cls.year = int(temp_date[2])
        return f"Date in integer {cls.days} {cls.month} {cls.year}"
    @staticmethod
    def data_validation(days: int, months: int, years: int):

        if days > 31:
            return f"Invalid day: {days}"
        elif months > 12:
            return f"Invalid month: {months}"
        elif not isinstance(years, int):
            return f"Invalid year: {years}"
        else:
            return f"Date is valid : {days} {months} {years}"


date = Date("12-12-2012")
print(date.extract_date("1997-23-06"))
print(Date.data_validation(12, 12, 1995))
print(Date.data_validation(12, 13, 1995))
