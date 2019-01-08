import tester
import statistics

def second(a, b, c):
    return b

def correct(a, b, c):
    return statistics.median([a, b, c])

print(tester.is_median(second))
print(tester.is_median(correct))
