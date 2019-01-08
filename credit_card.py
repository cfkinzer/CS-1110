def check(n):
    x = str(n)  # changes the integer input to a string
    x = list(x[::-2])  # changes the string to a list of every other character, including rightmost
    x = list(map(int, x))  # changes the list of strings into a list of integers
    x = sum(x)  # adds together all of the integers in the list
    y = str(n)  # changes the integer input to a string
    y = list(y[-2::-2])  # changes the string into a list of every other character, including second to rightmost
    y = list(map(int, y))  # changes the list of strings into a list of integers
    y = [i * 2 for i in y]  # multiplies all of the integers in the list by two
    y = list(map(str, y))  # changes the integers in the list back into strings
    for i in y:  # for each number in the list,
        if len(i) == 2:  # if the number has two digits
            first_digit = i[0]  # take the first digit
            second_digit = i[1]  # take the second digit
            y.remove(i)  # remove the two digit number from the list
            y.append(first_digit)  # adds the first digit back into the list
            y.append(second_digit)  # adds the second digit back into the list
    y = list(map(int, y))  # changes the list of strings into a list of integers
    y = sum(y)  # adds all the integers in the list together
    sum_xy = x + y  # adds both lists together
    if sum_xy % 10 == 0:  # if the remainder of the sum of both lists divided by 10 = 0,
        return True  # then the input is a valid credit card number
    else:  # if not,
        return False  # the input is not a valid credit card number
