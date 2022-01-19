from random import randint

class BoardException(Exception):
    pass

class BoardOutException(BoardException):
    def __str__(self):
       return 'Введены координаты превышающие \r\nграницы игрового поля'

class BoardShotException(BoardException):
    def __str__(self):
       return 'В эту клетку уже стреляли'

class BoardShipBadException(BoardException):
    pass

class Dot:

    def __init__(self, x,y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Dot({self.x}, {self.y})"

class Ship:

    def __init__(self, lenght, bow, direction):
        self.lenght = lenght
        self.bow = bow
        self.direction = direction
        self.number_lives = lenght

    @property
    def dots(self):
        ship_dots = []
        for i in range(self.lenght):
            act_x = self.bow.x
            act_y = self.bow.y

            if self.direction == 0:
                act_x += i
            elif self.direction == 1:
                act_y += i

            ship_dots.append(Dot(act_x,act_y))
        return ship_dots

    def shots(self, shot):
        return shot in self.dots


class Board:
    def __init__(self, hid=False, size=6):
        self.size = size
        self.hid = hid

        self.destr_ship = 0
        self.taken = []
        self.ships = []

        self.field = [["."] * size for _ in range(size)]

    #
    def contour(self, ship, view = False):

        st = list(zip([a for a in range(-1, 2) for b in range(3)],
                      [b for a in range(3) for b in range(-1, 2)]))

        for dot in ship.dots:
            for x, y in st:
                curs = Dot(dot.x + x, dot.y + y)
                if curs not in self.taken and not(self.output_limit(curs)):
                    if view:
                        self.field[curs.x][curs.y] = "X"
                    self.taken.append(curs)

    def add_ship(self, ship):

        for dot in ship.dots:
            if self.output_limit(dot) or dot in self.taken:
                raise BoardShipBadException()
        for dot in ship.dots:
            self.field[dot.x][dot.y] = "H"
            self.taken.append(dot)

        self.ships.append(ship)
        self.contour(ship)

    def output_limit(self, dot):
        return not((0 <= dot.x < self.size) and (0 <= dot.y < self.size))

    def __str__(self):

        result = '    '
        result += ' '.join([f'{i + 1} |' for i in range(self.size)])
        for i, row in enumerate(self.field):
            result += f"\n{i + 1} | " + " | ".join(row) + " |"

        if self.hid:
            result = result.replace("H", ".")

        return result

    def shot(self, dot):

        if dot in self.taken:
            raise BoardShotException()

        if self.output_limit(dot):
            raise BoardOutException()
        self.taken.append(dot)

        for ship in self.ships:
            if dot in ship.dots:
                ship.number_lives -= 1
                self.field[dot.x][dot.y] = "W"
                if ship.number_lives == 0:
                    self.destr_ship += 1
                    self.contour(ship, view=True)
                    print("Уничтожен!")
                    return False
                else:
                    print("Задел!")
                    return True

        self.field[dot.x][dot.y] = "X"
        print("Промах!")
        return False

    def begin(self):
        self.taken = []


class Player:
    def __init__(self, board, enemy):
        self.board = board
        self.enemy = enemy

    def ask(self):
        raise NotImplementedError()

    def step(self):
        while True:
            try:
                target = self.ask()
                repeat = self.enemy.shot(target)
                return repeat
            except BoardException as e:
                print(e)


class AI(Player):
    def ask(self):
        d = Dot(randint(0, 5), randint(0, 5))
        print(f"Ход компьютера: {d.x + 1} {d.y + 1}")
        return d


class User(Player):
    def ask(self):
        while True:
            cords = input("Ваш ход: ").split()

            if len(cords) != 2:
                print(" Введите 2 координаты! ")
                continue

            x, y = cords

            if not (x.isdigit()) or not (y.isdigit()):
                print(" Введите числа! ")
                continue

            x, y = int(x), int(y)

            return Dot(x - 1, y - 1)


class Game:

    def __init__(self):
        self.welcome()
        self.set_board_size()
        gamer = self.random_board()
        comp = self.random_board()
        comp.hid = True

        self.ai = AI(comp, gamer)
        self.us = User(gamer, comp)
        self.loop()

    def random_board(self):
        board = None
        while board is None:
            board = self.random_place()
        return board

    def random_place(self):

        lens_list = [[3, 2, 2, 1, 1, 1, 1], [3, 2, 2, 2, 1, 1, 1, 1, 1],[3, 3, 2, 2, 2, 1, 1, 1, 1, 1],[4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1],
                     [4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1], [4, 4, 3, 3, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1],
                     [5, 4, 4, 4, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1]]
        for i, j in enumerate(lens_list, start = 6):
            if self.size == i:
                self.lens = j
                break
        board = Board(size=self.size)
        attempts = 0
        for lenght in self.lens:
            while True:
                attempts += 1
                if attempts > 1000:
                    return None
                ship = Ship(lenght, Dot(randint(0, self.size), randint(0, self.size)), randint(0, 1))
                try:
                    board.add_ship(ship)
                    break
                except BoardShipBadException:
                    pass
        board.begin()
        return board

    def welcome(self):
        print("-*-" * 7)
        print("  Добро пожаловать ")
        print("      в игру       ")
        print("    морской бой    ")
        print("-*-" * 7)
        print(" формат ввода: x y ")
        print(" x - номер строки  ")
        print(" y - номер столбца ")
        print("-*-" * 7)

    def set_board_size(self, size = 6):
        self.size = size

        while True:
            size = input("Задайте размер доски от 6 до 12: ")

            if not (size.isdigit()):
                print(" Введите число! ")
                continue

            size = int(size)

            if not (6 <= size <= 12):
                print("Введите число от 6 до 12")
                continue
            self.size = size

            return self.size

    def loop(self):
        num = 0
        while True:
            print("-*-" * 7)
            print("Доска пользователя:")
            print(self.us.board)
            print("-*-" * 7)
            print("Доска компьютера:")
            print(self.ai.board)
            if num % 2 == 0:
                print("-*-" * 7)
                print("Ходит пользователь!")
                repeat = self.us.step()
            else:
                print("-*-" * 7)
                print("Ходит компьютер!")
                repeat = self.ai.step()
            if repeat:
                num -= 1

            if self.ai.board.destr_ship == len(self.lens):
                print("-*-" * 7)
                print("Пользователь выиграл!")
                break

            if self.us.board.destr_ship == len(self.lens):
                print("-*-" * 7)
                print("Компьютер выиграл!")
                break
            num += 1



st = Game()
