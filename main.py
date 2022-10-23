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
            while dalnost < 1:              #проверка на вводимое число
                dalnost = int(input("Расстояние может быть только положительным ненулевым числом! Введите число: "))
        mas_dalnost.append([dalnost, i + 1])
    mas_dalnost.sort(reverse=True)

    mas_tarif = []
    for i in range(0, n):
        tarif = int(input("Введите тариф в рублях за проезд одного километра в такси: "))
        if tarif < 1:
            while tarif < 1:            #проверка на вводимое число
                tarif = int(input("Тариф может быть только положительным ненулевым числом! Введите число: "))
        mas_tarif.append([tarif, i+1])
    mas_tarif.sort()

    mas_sotv = []
    mas1 = []
    mas2 = []
    for j in mas_dalnost:
        mas1.append(j[1])
    for k in mas_tarif:                 #добавление порядковых номеров в отдельные массивы
        mas2.append(k[1])

    for i in range(0, n):
        mas_sotv.append([mas1[i], mas2[i]])            #соотношение сотрудника и такси

    mas_sotv.sort()
    for i in range(0, n):
        print(mas_sotv[i][0], "сотруднику необходимо", mas_sotv[i][1], "такси")

    summa = 0
    for i in range(0, n):           #подсчет суммы
        summa = mas_dalnost[i][0] * mas_tarif[i][0] + summa

        # код из второй лабораторной работы
    desatki1a = ["один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    desatki1b = ["одна", "две", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    desatki2 = ["одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать",
                "восемнадцать", "девятнадцать"]
    desatki3 = ["десять", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят",
                "девяносто"]
    desatki4 = ["сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]
    desatki5 = ["тысяча", "тысячи", "тысяч"]
    desatki6 = ["рубль", "рубля", "рублей"]

    cifra1 = summa // 100000
    cifra2 = (summa // 10000) % 10
    cifra3 = (summa // 1000) % 10
    cifra4 = (summa // 100) % 10
    cifra5 = (summa // 10) % 10
    cifra6 = summa % 10

    slova = ""
    if cifra1 != 0:
        i1 = cifra1 - 1
        slova += desatki4[i1] + " "

    if cifra2 == 1 and cifra3 == 0:
        slova += desatki3[0] + " "
    if cifra2 != 1:
        if cifra2 != 0:
            i2 = cifra2 - 1
            slova += desatki3[i2] + " "

    if cifra3 != 0:
        if cifra2 == 1:
            i3 = cifra3 - 1
            slova += desatki2[i3] + " " + desatki5[2] + " "
        else:
            i3 = cifra3 - 1
            slova += desatki1b[i3] + " "
            if cifra3 == 1:
                slova += desatki5[0] + " "
            elif 1 < cifra3 < 5:
                slova += desatki5[1] + " "
            else:
                slova += desatki5[2] + " "
    if (cifra3 == 0) and (cifra2 or cifra1 != 0):
        slova += desatki5[2] + " "

    if cifra4 != 0:
        i4 = cifra4 - 1
        slova += desatki4[i4] + " "

    if cifra5 == 1 and cifra6 == 0:
        slova += desatki3[0] + " "
    if cifra5 != 1:
        if cifra5 != 0:
            i5 = cifra5 - 1
            slova += desatki3[i5] + " "

    if cifra6 != 0:
        if cifra5 == 1:
            i6 = cifra6 - 1
            slova += desatki2[i6] + " " + desatki6[2]
        else:
            i6 = cifra6 - 1
            slova += desatki1a[i6] + " "
            if cifra6 == 1:
                slova += desatki6[0] + " "
            elif 1 < cifra6 < 5:
                slova += desatki6[1] + " "
            else:
                slova += desatki6[2] + " "

    if (cifra6 == 0) and (cifra5 or cifra4 or cifra3 or cifra2 or cifra1 != 0):
        slova += desatki6[2]

    print("Сумма в рублях, которую необходимо заплатить за просчитанный вариант:", summa, "- " + slova)