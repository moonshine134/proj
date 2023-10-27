def func1(value):
    print("Метров: " + str(value))
    print("Сантиметров: " + str(value * 100))
    print("Миллиметров: " + str(value * 1000))
    print("Километров: " + str(value / 1000))
    print()


def first():
    func1(100)
    func1(1)
    func1(1000)


def second():
    name = input("Введите имя ")
    age = input("Введите возраст ")

    sum = str(len(age) + len(name))

    print(sum + " символов")


def third():
    f_x = int(input("Введите номер строки 1 точки"))
    f_y = int(input("Введите номер столбца 1 точки"))

    s_x = int(input("Введите номер строки 2 точки"))
    s_y = int(input("Введите номер столбца 2 точки"))

    if abs(f_x - s_x) > 1 or abs(f_y - s_y) > 1:
        print("король не может дойти")
        return

    print("Король может дойти")


def fourth():
    first_list = input("Введите список через ,").split(",")
    second_list = input("Введите 2 список через ,").split(",")

    concat_list = []
    i = 0
    while i < min(len(first_list), len(second_list)):
        concat_list.append(first_list[i])
        concat_list.append(second_list[i])
        i += 1

    while i < len(first_list):
        concat_list.append(first_list[i])
        i += 1

    while i < len(second_list):
        concat_list.append(second_list[i])
        i += 1

    print(concat_list)


def calculation(num, num1):
    return num + num1, num - num1


def five():
    print(calculation(5, 1))
    print(calculation(4, 6))
    print(calculation(3, 7))
