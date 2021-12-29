
def greeting():
    print('--------------------')
    print('  Добро пожаловать  ')
    print('       в игру       ')
    print('  крестики-нолики   ')
    print('--------------------')
    print('Ввод данных         ')
    print('по форме: a b       ')
    print('где а - строки      ')
    print('    b - столбцы     ')
    print('--------------------')
    print('Чтобы закончить игру')
    print('  Введите букву: E  ')

def form_out():
    print('-----------------')
    print(' № | 0 | 1 | 2 |')
    print('-----------------')
    for i, row in enumerate(form):
        print(f" {i} | {' | '.join(row)} |")
        print('-----------------')
    print()

def invite():
    global count
    while True:
        sequence = input('Введите координаты: ').split()

        if sequence[0] == 'E':

            return -1, -1




        if len(sequence) == 2:
            a, b = sequence
            if (a.isdigit()) and (b.isdigit()):
                a, b = int(a), int(b)
                if 0 <= a <= 2 and 0 <= b <= 2:
                    if form[a][b] == " ":
                        return a, b
                    else:
                        print(' Клетка уже занята!!!')

                else:
                    print('Введите координаты')
                    print('от 1 до 3! ')
                    continue
            else:
                print('Введите числа!')
                continue
        else:
            print('Введите две координаты!')
            continue

def victory_condition():
    victiry_sequence = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                        ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
                        ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)))
    for sequence in victiry_sequence:
        sign = []
        for x in sequence:
            sign.append(form[x[0]][x[1]])
        if sign == ["0", "0", "0"]:
            print('!!!Выиграл игрок!!!')
            print('!!!! с ноликами !!!')
            return True
        if sign == ["X", "X", "X"]:
            print('!!!Выиграл игрок!!!')
            print('!!!с крестиками !!!')
            return True
    return False


greeting()
form = [[" "]*3  for i in range(3)]
count = 0
form_out()
while True:
    count += 1


    if count % 2 == 0:
        print('Ход игрока с ноликами')
    else:
        print('Ход игрока с крестиками')

    a, b = invite()
    if a == -1 and b == -1:
        print('Закончить игру')
        break
    if count % 2 == 0:
        form[a][b] = "0"
    else:
        form[a][b] = "X"
    form_out()
    if victory_condition():
        break

    if count == 9:
        print(' Свободных клеток ')
        print('    не осталось,')
        print('  победила дружба!')
        break









