cikl = 2
while cikl != 0:
    n = int(input("Введите количество ваших сторудников: "))
    if n == 0:
        break       #проверка на выход из программы
    elif n < 1 or n > 1000:
        while n < 1 or n > 1000:
            n = int(input("Введите число от 1 до 1000: "))  #проверка на вводимое число

    mas_dalnost = []
    for i in range(0, n):
        dalnost = int(input("Введите расстояния в километрах от работы до дома сотрудника компании: "))
        if dalnost < 1:
            while dalnost < 1:
                dalnost = int(input("Расстояние может быть только положительным ненулевым числом! Введите число: "))
        mas_dalnost.append([dalnost, i + 1])
    mas_dalnost.sort(reverse=True)

    mas_tarif = []
    for i in range(0, n):
        tarif = int(input("Введите тариф в рублях за проезд одного километра в такси: "))
        if tarif < 1:
            while tarif < 1:
                tarif = int(input("Тариф может быть только положительным ненулевым числом! Введите число: "))
        mas_tarif.append([tarif, i+1])
    mas_tarif.sort()

    mas_sotv = []
    mas1 = []
    mas2 = []
    for j in mas_dalnost:
        mas1.append(j[1])
    for k in mas_tarif:
        mas2.append(k[1])

    for i in range(0, n):
        mas_sotv.append([mas1[i], mas2[i]])

    mas_sotv.sort()
    for i in range(0, n):
        print(mas_sotv[i][0], "сотруднику необходимо", mas_sotv[i][1], "такси")

    summa = 0
    for i in range(0, n):
        summa = mas_dalnost[i][0] * mas_tarif[i][0] + summa
    print("Сумма в рублях, которую необходимо заплатить за просчитанный вариант: ", summa)
