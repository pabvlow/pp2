import math
n = int(input())
l = int(input())
a = l / (2 * math.tan(180 / n)) 
p = l * n
print((a * p) / 2)