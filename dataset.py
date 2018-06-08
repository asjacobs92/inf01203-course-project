# -*- coding: utf-8 -*-

from random import *

from config import *


def generate_small():
    input_search = []
    for i in range(50):
        search = []
        search.append(sample(RS_CITIES, 1)[0])
        search.extend(sample(SEARCH_TERMS, randint(1, 3)))
        input_search.append(search)

    with open('res/small/input.txt', 'w') as file:
        for search in input_search:
            file.write(';'.join(search) + '\n')


def generate_large():
    input_search = []
    for i in range(1000):
        search = []
        search.append(sample(BRAZIL_CAPITALS, 1)[0])
        search.extend(sample(SEARCH_TERMS, randint(1, 20)))
        input_search.append(search)

    with open('res/large/input.txt', 'w') as file:
        for search in input_search:
            file.write(';'.join(search) + '\n')

    input_operations = []
    for i in range(50):
        operation = []
        op = sample(OPERATIONS, 1)[0]
        operation.append(op)
        if op is 'a'or op is 'c' or op is 'e':
            operation.append(sample(BRAZIL_CAPITALS, 1)[0])
        if op is not 'f':
            operation.append(str(randrange(0, 100, 10)))

        input_operations.append(operation)

    with open('res/large/operations.txt', 'w') as file:
        for op in input_operations:
            file.write(';'.join(op) + '\n')


def generate_evaluation():
    input_search = []
    for i in range(5000):
        search = []
        search.append(sample(BRAZIL_CAPITALS, 1)[0])
        search.extend(sample(SEARCH_TERMS, randint(1, 20)))
        input_search.append(search)

    with open('res/evaluation/input.txt', 'w') as file:
        for search in input_search:
            file.write(';'.join(search) + '\n')

    input_operations = []
    for i in range(100):
        operation = []
        op = sample(OPERATIONS, 1)[0]
        operation.append(op)
        if op is 'a'or op is 'c' or op is 'e':
            operation.append(sample(BRAZIL_CAPITALS, 1)[0])
        if op is not 'f':
            operation.append(str(randrange(0, 100, 10)))

        input_operations.append(operation)

    with open('res/evaluation/operations.txt', 'w') as file:
        for op in input_operations:
            file.write(';'.join(op) + '\n')


if __name__ == "__main__":
    generate_small()
    generate_large()
    generate_evaluation()
