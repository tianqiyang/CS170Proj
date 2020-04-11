"""
generate the three input files as 25.in...
"""
import random
nums = [25, 50, 100]
def genDis():
    a, b, c = generLen(), generLen(), generLen()
    while a + b <= c or b + c <= a or a + c <= b:
        c = generLen()
    return a, b, c

def generLen():
    a = round(random.random() * 100, 3)
    return a if a else generLen()

for num in nums:
    random.seed()
    with open( str(num) + ".in", "w") as file:
        i, k = 0, 0
        file.write(str(num) + '\n')
        while i < num/3:
            dis = genDis()
            for j in range(3):
                if k < num:
                    file.write(str(k) + " ")
                    k = k + 1 if k % 3 != 2 else k - 2
                    file.write(str(k) + " " + str(dis[j]) + "\n")
            if k + 2 < num:
                file.write(str(k + 2) + " " + str(k + 3) + " " + str(generLen()) + "\n")
            k, i = k + 3, i + 1