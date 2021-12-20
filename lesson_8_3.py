# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список только числами. Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список с числами выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.

class CheckNumberException(Exception):
    def __init__(self, errors):
        self.error_text = errors

    def __str__(self):
        return self.errors


output_list = []
print("Остановить программу можно написав: стоп")
print(f"*" * 40)
while True:
    user_input = input("Введите данные: число или слово >>>> ")

    if user_input in("стоп","stop"):
        print(f"Список чисел: {output_list}")
        break

    try:
        if not user_input.isnumeric():
            raise CheckNumberException(f"Введенное слово [{user_input}] будет пропущено!")
        output_list.append(user_input)
    except CheckNumberException as error:
        print(error.error_text)