def st_jeor(mass, height, age, sex):
    if sex == 'male':
        return 10.0 * mass + 6.25 * height - 5.0 * age + 5
    if sex == 'female':
        return 10.0 * mass + 6.25 * height - 5.0 * age - 161