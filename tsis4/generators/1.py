n = int(input())
def generator(n):
    for i in range(1, n + 1):
        yield i ** 2
squares = generator(n)
for square in squares:
    print(square)