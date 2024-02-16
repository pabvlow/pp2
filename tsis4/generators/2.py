n = int(input())
def generator(n):
    for i in range(0, n + 1):
        if i % 2 == 0 and i != 0:
            yield i
evens = generator(n)
for even in evens:
    print(even)