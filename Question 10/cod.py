import math
import itertools

global possible_numbers
possible_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
global highest
highest = 0
global lowest
lowest = 307389

def find_area_of_triangle(a, b, c):
    # Returns Heron's formula
    s = (a + b + c) / 2
    minus_check = s * (s - a) * (s - b) * (s - c)
    if minus_check <= 0:
        return "na"
    else:
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

def find_highest_lowest(value):
    global highest
    global lowest
    if int(value) > highest:
        highest = value
        print("High: ", highest)
    if int(value) < lowest:
        lowest = value
        print("Low: ", value)

def main():
    for x in range(len(possible_numbers) + 1):
        for subset in itertools.permutations(possible_numbers, x):
            if len(subset) == 9:
                num1 = int(str(subset[0]) + str(subset[1]) + str(subset[2]))
                num2 = int(str(subset[3]) + str(subset[4]) + str(subset[5]))
                num3 = int(str(subset[6]) + str(subset[7]) + str(subset[8]))
                if find_area_of_triangle(num1, num2, num3) != "na":
                    find_highest_lowest(find_area_of_triangle(num1, num2, num3))


main()
print("Solved, highest:  ", highest, "  lowest:  ",lowest)
print("Highest / Lowest (P/Q)", highest / lowest)

