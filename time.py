# Пользователь вводит время в секундах. Переведите время в часы, минуты и
# секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
def times():
    while True:
        try:
            time = int(input('Введите время в секундах: '))
            hours = (time // 3600) % 24 # в часе 3600 сек, и + 24-часовой формат, поэтому так написал.
            minutes = (time // 60) % 60 # в минуте 60 сек, по аналогии с часами
            second = time % 60
            if minutes < 10:
                minutes = '0' + str(minutes) # нашел самый простой способ. все перевсти в строку и дописать 0
            else:
                minutes = str(minutes)
            if second < 10:
                second = '0' + str(second)
            else:
                second = str(second)
            if hours < 10:
                hours = '0' + str(hours)
            else:
                hours = str(hours)
        except ValueError:
            print("Вы ввели не число. Попробуйте еще раз!")
        else:
            print('Вы ввели время: ' + str(hours) + ':' + str(minutes) + ':' + str(second))
            break
times()
# ч/з f-функцию не пробовал, программа не особо большая, поэтому памяти не сожрет много