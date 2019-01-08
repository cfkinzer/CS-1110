"""Christian Kinzer (cfk5ax)
lab done by myself, did not come to class, chose to watch the Hoos instead"""


import random

restaurants = ['Newcomb', 'Qdoba', 'Chick-fil-A', 'The Virginian', 'Citizen Burger', 'The Alley Light']
styles = ['Dining hall', 'Mexican', 'Fast Food', 'American', 'Hamburger', 'French']
costs = ['$', '$', '$', '$$', '$$', '$$$']


def get_random_restaurant():
    x = random.randint(0, 5)
    print("We're going to ", restaurants[x], " today! (Style: ", styles[x], ' / Cost: ', costs[x], ')')


def get_restaurant_style(chosen_style):
    x = styles.index(chosen_style)
    print("We're going to ", restaurants[x], "today! (Style: ", styles[x], ' / Cost: ', costs[x], ')')


def get_restaurant_cost(chosen_cost):
    x = costs.index(chosen_cost)
    print("We're going to ", restaurants[x], "today! (Style: ", styles[x], ' / Cost: ', costs[x], ')')

print("Welcome to WahooSpoon!")
print("  1. Get a random restaurant")
print("  2. Get a random restaurant based on style")
print("  3. Get a random restaurant based on cost")
choice = int(input('Choice? '))
if choice == 1:
    get_random_restaurant()
elif choice == 2:
    print(set(styles))
    style = input("What style would you like?: ")
    get_restaurant_style(style)
else:
    print(set(costs))
    cost = input("What cost would you like?: ")
    get_restaurant_cost(cost)
