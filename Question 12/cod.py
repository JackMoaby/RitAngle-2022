import itertools

possible_numbers = [1, 2, 3, 4, 5, 6]
global solution
solution = []


def left_hand_side(a, b, c, d, e, f, x):
    var = (8 * (x ** 2) + a * x + int(str(2) + str(b))) / (((x ** 2) + 4) *
                                                         ((c * x) + 1))
    return var


def right_hand_side(a, b, c, d, e, f, x):
    var = ((x + d) / (x ** 2 + e)) + (f) / (2 * x + 1)
    return var


def check_calc(possible_numbers):
    global solution

    a = possible_numbers[0]
    b = possible_numbers[1]
    c = possible_numbers[2]
    d = possible_numbers[3]
    e = possible_numbers[4]
    f = possible_numbers[5]
    passed = 1

    for x in range(100):
        lhs = left_hand_side(a, b, c, d, e, f, x + 1)
        rhs = right_hand_side(a, b, c, d, e, f, x + 1)
        if lhs == rhs:
            passed += 1
    if passed > 2:
        print("Solved:  ", a, b, c, d, e, f)
        solution = possible_numbers
        return "True"
    else:
        print("Failed", a, b, c, d, e, f)
        return


def main(possible_numbers):
    for x in range(len(possible_numbers) + 1):
        for subset in itertools.permutations(possible_numbers, x):
            if len(subset) == 6:
                check_calc(subset)


main(possible_numbers)

print("----------")
print("Solved", solution)
print("----------")
