# 0(n)
def numberOfSteps(num):
    a = 0                         # счетчик
    while num > 0:                # пока число больше нуля
        if num % 2 == 0:          # если число четное
            num /= 2              # делим число на два
            a += 1                # добавляется шаг
        else:                     # если число нечётное
            num -= 1              # отнимаем от числа единицу
            a += 1                # добавляется шаг
    return a                      # возвращаем кол-во шагов