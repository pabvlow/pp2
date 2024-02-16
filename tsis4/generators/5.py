n = int(input())
def ret(n):
    while n >= 0:
        yield n
        n -= 1
for elements in ret(n):
    print(elements)