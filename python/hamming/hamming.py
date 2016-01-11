def distance(str_1, str_2):
    distance = 0
    for index, char in enumerate(str_1):
        if char != str_2[index]:
            distance += 1
    return distance
