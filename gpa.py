num = 0
creditcount = 0


def add_course(x, y=3):
    global num
    global creditcount
    credits_have = num * creditcount
    creditcount += y
    credits_have += (x * y)
    num = credits_have / creditcount


def gpa():
    return num


def credit_total():
    return creditcount

add_course(4.0, 3)
print(gpa(), credit_total())
add_course(3.3)
print(gpa(), credit_total())
add_course(2.3, 4)
print(gpa(), credit_total())
