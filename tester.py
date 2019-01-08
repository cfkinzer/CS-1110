def is_median(func):
    if func(1, 2, 3) != 2:
        return False
    if func(3, 2, 1) != 2:
        return False
    if func(1, 3, 2) != 2:
        return False
    if func(3, 1, 2) != 2:
        return False
    if func(2, 1, 3) != 2:
        return False
    if func(2, 3, 1) != 2:
        return False
    if func(-1, -2, -3) != -2:
        return False
    if func(-3, -2, -1) != -2:
        return False
    if func(-1, -3, -2) != -2:
        return False
    if func(-3, -1, -2) != -2:
        return False
    if func(-2, -1, -3) != -2:
        return False
    if func(-2, -3, -1) != -2:
        return False
    if func(0 + 1, 0 + 2, 0 + 3) != 2:
        return False
    if func(0 - 1, 0 - 2, 0 - 3) != -2:
        return False
    if func(1, 1, 1) != 1:
        return False
    if func(-1, -1, -1) != -1:
        return False
    if func(1.0, 2.0, 3.0) != 2.0:
        return False
    if func(3.0, 2.0, 1.0) != 2.0:
        return False
    if func(1.0, 3.0, 2.0) != 2.0:
        return False
    if func(2.0, 1.0, 3.0) != 2.0:
        return False
    if func(2.0, 3.0, 1.0) != 2.0:
        return False
    if func(3.0, 1.0, 2.0) != 2.0:
        return False
    if func(-1.0, -2.0, -3.0) != -2.0:
        return False
    if func(1, 2, 4) != 2:
        return False
    if func(1, 1, 2) != 1:
        return False
    if func(-1, 1, 1) != 1:
        return False
    if func(0, 0, 0) != 0:
        return False
    if func(2, 4, 6) != 4:
        return False
    if func(1, 3, 5) != 3:
        return False
    if func(-1, -3, -5) != -3:
        return False
    if func(-2, -4, -6) != -4:
        return False
    if func(20000000000, 3000000000000000000, 100000000) != 20000000000:
        return False
    if func(-20000000000, -3000000000000000000, -10000000) != -20000000000:
        return False
    else:
        return True
