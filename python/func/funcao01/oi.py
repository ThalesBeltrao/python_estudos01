def contador():
    x = 0
    while x < 3:
        yield x
        x += 1


g = contador()
print(next(g))
print(next(g))
print(next(g))
