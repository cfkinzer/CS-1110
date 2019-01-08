num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
           (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]  # establishes a list of integers and corresponding numerals

roman = ''  # establishes the string that will be printed as the roman numeral of the input
num = int(input('Enter an integer: '))  # takes input
n = num  # moves input to another variable so we can change it while keeping the original value
if 1 > n or n > 3999:
    print('Input must be between 1 and 3999.')  # rejects inputs outside of the range (1, 3999)
else:
    while n > 0:
        for i, r in num_map:
            while n >= i:
                roman += r
                n -= i  # adds correct strings and subtracts the integer values from n until n == 0
    print('In roman numerals, ', num, ' is ', roman,)  # prints the conversion
