# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369
def numbers():
    while True:
        try:
            n = int(input('Введите число: '))
            number = str(n) # перевожу число в строку, чтобы цифры просто писались подряд, а не складывались.
            number1 = number + number
            number2 = number + number + number
            summ = int(number) + int(number1) + int(number2) # перевожу все обратно в цифры, чтобы сложить
        except ValueError:
            print("Вы ввели не число. Попробуйте еще раз!")
        else:
            print('Результат равен: ', summ)
            break
numbers()


