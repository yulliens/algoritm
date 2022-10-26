# O(n)
def numJewelsInStones(jewels, stones):
    d = 0                                # счётчик
    for i in stones:                     # проходимся по камням
        if i in jewels:                  # если камень драгоценный
            d += 1                       # добавляем в счётчик единицу
    return d                             # возвращаем d