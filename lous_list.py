from urllib.request import urlopen


def instructors(department):
    url = 'http://cs1110.cs.virginia.edu/files/louslist/' + department
    classes = urlopen(url)
    names = []
    for line in classes:
        line = line.decode('utf-8')
        line = str(line.strip())
        line = line.split('|')
        name = line[4]
        if name[-2] == '+':
            name = name[:-2]
        names.append(name)
    names = list(set(names))
    names.sort()
    return names


def class_search(dept_name, has_seats_available=True, level=None, not_before=None, not_after=None):
    url = 'http://cs1110.cs.virginia.edu/files/louslist/' + dept_name
    classes = urlopen(url)
    has_seats = []
    right_level = []
    late_enough = []
    early_enough = []
    final_search = []
    for line in classes:
        line = line.decode('utf-8')
        line = str(line.strip())
        line = line.split('|')
        course_number = line[1]
        course_number = int(course_number[0])
        start_time = int(line[12])
        seats_taken = int(line[15])
        seats = int(line[16])
        if type(level) == int:
            level = str(level)
            level = int(level[0])
        if has_seats_available is True:
            if seats > seats_taken:
                has_seats.append(line)
        if has_seats_available is False:
            has_seats.append(line)
        if type(level) == int:
            if level == course_number:
                right_level.append(line)
        else:
            right_level.append(line)
        if type(not_before) == int:
            if start_time >= not_before:
                late_enough.append(line)
        else:
            late_enough.append(line)
        if type(not_after) == int:
            if start_time <= not_after:
                early_enough.append(line)
        else:
            early_enough.append(line)
        if line in has_seats and line in right_level and line in late_enough and line in early_enough:
            final_search.append(line)
    return final_search
