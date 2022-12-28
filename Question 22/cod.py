numbers=[]
highestbase = False
base =1 
for base in range(2,105):
    for ones in range(1,15):
        value=0
        for y in range(0,ones):
            value = value + base ** y
        if value > 10000:
            break
        numbers.append(value)
    print(numbers,"balls")

for x in range(106,9999):
    numbers.append(x)
#print(numbers.count(31))
for x in numbers:
    if numbers.count(x) > 2:
        print(x)
