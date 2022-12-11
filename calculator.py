def count_people(width, height, num_of_floors, disinfectants):
    total_area = width * height * num_of_floors
    people = round(total_area / 7.5)
    if disinfectants:
        people = round(people * 1.1)
    else:
        people = round(people * .5)
    return people
