import random
import copy

def generate_list(length, least=0, most=100):
    array = []
    for each in range(length):
        array.append(random.randint(least,most))
    return array
