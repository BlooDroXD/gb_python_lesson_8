# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
# выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumbers:
    real_number: int
    fake_number: int

    def __init__(self, real_number: int, fake_number: int):
        self.real_number = real_number
        self.fake_number = fake_number

    def __str__(self):
        return f"Результат операции: " \
               f"({self.real_number}{'+' if self.fake_number > 0 else ''}{self.fake_number}i)"

    def __add__(self, other: 'ComplexNumbers'):
        print(f"Первое комплексное число: ({self.real_number}+{self.fake_number}i)")
        print(f"Второе комплексное число: ({other.real_number}+{other.fake_number}i)")

        r = self.real_number + other.real_number
        f = self.fake_number + other.fake_number

        return ComplexNumbers(r, f)

    def __mul__(self, other: 'ComplexNumbers'):
        print(f"Первое комплексное число: ({self.real_number}+{self.fake_number}i)")
        print(f"Второе комплексное число: ({other.real_number}+{other.fake_number}i)")

        r1 = self.real_number * other.real_number
        r2 = self.fake_number * other.fake_number * -1  # j*j = -1.

        i1 = self.real_number * other.fake_number
        i2 = self.fake_number * other.real_number

        r = r1 + r2
        f = i1 + i2

        return ComplexNumbers(r, f)


a = ComplexNumbers(26, 12)
b = ComplexNumbers(26, 8)
# Как складываются комплексные числа: (26+12i)+(26+8i)=(26+26)+(12+8)i=(52+20i)
print(a + b)
print()
# Как перемножаются комлексные числа: (26+12i)*(26+8i)=(26*26-12*8)+(12*26+26*8)=(676-96)+(312+208)i=(580+520i)
print(a * b)