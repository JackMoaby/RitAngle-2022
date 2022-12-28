import math

values = [0, 0, 0]
fake_depth = 30
depth = fake_depth + 1


def check(values):
    a, b, c = values[0], values[1], values[2]

    if ((a**2) + (b**2) + (c**2)) == 899:
        # print("Passed First", a, b, c)
        if ((a * b) + (a * c) + (b * c)) == 851:
            # print("Passed Second", a, b, c)
            return True
def calculate_heron(values):
    a, b, c = values[0], values[1], values[2]
    sa = math.sqrt(a)
    sb = math.sqrt(b)
    sc = math.sqrt(c)
    
    s = (sa + sb + sc) / 2
    area = math.sqrt(s * (s - sa) * (s - sb) * (s - sc))
    
    return area
    

def main(values, depth):
    for a in range(depth):
        values[0] += 1
        for b in range(depth):
            values[1] += 1
            for c in range(depth):
                values[2] += 1
                if check(values) == True:
                    print("Solved", values)
                    print(calculate_heron(values))
                    break
            values[2] = 0
        values[1] = 0
    values[0] = 0


main(values, depth)
