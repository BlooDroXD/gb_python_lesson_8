# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно
# обработать эту ситуацию и не завершиться с ошибкой.

class DivisionByZero(Exception):
    def __init__(self, dividend, divisor):
        self.dividend = dividend
        self.divisor = divisor
    def __str__(self):
        return f"Division by zero! dividend is:{self.dividend} divisor is:{self.divisor}"
dividend = float(input("Input dividend: "))  # делимое
divisor = float(input("Input divisor: "))  # делитель
if divisor == 0:
    raise DivisionByZero(dividend, divisor)
try:
    print(f'{dividend} / {divisor} = {dividend/divisor}')

except DivisionByZero as exception:
    print(exception(dividend, divisor))