def word_frequency(string):
    words = string.split()
    return {string: words.count(string) for string in set(words)}
string = str(input())
result = word_frequency(string)
print(result)