from time import perf_counter

depth = 128 # this number was initially done to 2^69, but 2^7 is the minimum floating point32 for the highest accuracy
print("Total depth", (2**depth)*8)

start =perf_counter()
def calculate_p(depth):
    x = 2
    p = 1
    while x < (2**depth):
        p = p + (1 / x)
        p = p - (1 / (x * 2))
        p = p - (1 / (x * 4))
        x = (((x * 2) * 2) * 2)
    return p


def calculate_q(depth):
    x = 2
    q = 1
    while x < (2**depth):
        q = q - (1 / x)
        q = q + (1 / (x * 2))
        q = q + (1 / (x * 4))
        x = (((x * 2) * 2) * 2)
    return q


output_p = calculate_p(depth)
output_q = calculate_q(depth)
output = output_p / output_q

end = perf_counter()

print(output)
print("Solved in", (end - start), "seconds"))
