import random

code1 = [random.randint(0, 9) for _ in range(3)]
code2 = [random.randint(1, 6) for _ in range(4)]

print(f"A 3-digit code where each number is between 0 and 9 : {code1}" )
print(f"A 4-digit code where each number is between 1 and 6 : {code2}" )
