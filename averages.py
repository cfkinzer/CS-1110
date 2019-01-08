def mean(a, b, c):
    return (a + b + c) / 3


def median(a, b, c):
    if a <= b <= c or c <= b <= a:
        return b
    if b <= a <= c or c <= a <= b:
        return a
    if a <= c <= b or b <= c <= a:
        return c


def rms(a, b, c):
    return mean(a ** 2, b ** 2, c ** 2) ** .5


def middle_average(a, b, c):
    x = mean(a, b, c)
    y = median(a, b, c)
    z = rms(a, b, c)
    return median(x, y, z)
