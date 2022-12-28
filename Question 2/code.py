import time
import itertools

start = time.perf_counter()

# Initialises the array of possible values for ABCDEFGHIJ
global possible_numbers
possible_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
global out
out = 0

#In a function so the value can be written to a print statement below
def main():
    
    # Finds all of the possible permutations of the array from the itertools module
    for x in range(len(possible_numbers) + 1):
        for subset in itertools.permutations(possible_numbers, x):
            if len(subset) == 10:
                concatenate = [""]
                for y in range(len(subset)):
                    concatenate.append(subset[y])
                    
                # Creates a variable of all of the values as concatenated strings
                out = "".join([str(item) for item in concatenate])
                
                # Checks them against each operation
                # int(out[:1]) returns the integer of the string with the last 1 digit(s) removed
                #The stack stops unnecassary checks by breaking from the stack at the earliest possible
                for z in range(1):
                    if int(out) % 10 == 0:
                        if int(out[:-1]) % 9 == 0:
                            if int(out[:-2]) % 8 == 0:
                                if int(out[:-3]) % 7 == 0:
                                    if int(out[:-4]) % 6 == 0:
                                        if int(out[:-5]) % 5 == 0:
                                            if int(out[:-6]) % 4 == 0:
                                                if int(out[:-7]) % 3 == 0:
                                                    if int(out[:-8]) % 2 == 0:
                                                        if int(out[:-9]) % 1 == 0:
                                                            print("Valid: ", out)
                                                            return out
                    print(out)
                    break   
output = main()
print("")
print("Solved solution:  ", output)
print("Time taken:  ", (time.perf_counter() - start))


