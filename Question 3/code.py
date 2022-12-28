import time
import itertools

start = time.perf_counter()
global possible_numbers
possible_numbers = [1, 2, 3, 4, 5, 6]
global highest
highest = 0
global highest_nums
highest_nums = ["", "", ""]


def main(highest):
    for x in range(len(possible_numbers) + 1):
        for subset in itertools.permutations(possible_numbers, x):
            if len(subset) == 6:
                num1 = int(str(subset[0]) + str(subset[1]))
                num2 = int(str(subset[2]) + "5" + str(subset[3]))
                num3 = int(str(subset[4]) + "4" + str(subset[5]))
                if (num2 - num1) == (num3 - num2):
                # Initial incorrect interpretation of an arithmetic sequance said num2 < num3
                    out = num1 * num2 * num3
                    if out > highest:
                        highest = out
                        highest_nums[0] = num1
                        highest_nums[1] = num2
                        highest_nums[2] = num3
    return highest
    
def concatenate():
    string = str(highest_nums[0]) + str(highest_nums[1]) + str(highest_nums[2])
    print("A = ", string[0])
    print("B = ", string[1])
    print("C = ", string[2])
    print("D = ", string[4])
    print("E = ", string[5])
    print("F = ", string[7])


output = main(highest)
print("Solved solution:  ", output)
print("")
print("Time taken:  ", (time.perf_counter() - start))
print("")
concatenate()

