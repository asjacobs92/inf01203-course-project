# -*- coding: utf-8 -*-

from collections import Counter, OrderedDict
from sets import *

from config import *
from unidecode import *


def list_searches_by_city(searches, input, size):
    city = input[0]
    city_searches = [search for search in searches if search['city'] == city]

    list_searches(city_searches, input[1:], size)


def list_searches(searches, input, size):
    num_searches = int(input[0])
    all_searches = [tuple(sorted(search['terms'])) for search in searches]

    counter = Counter(all_searches)
    with open("res/{}/output.txt".format(size), "a") as file:
        search_list = counter.most_common() if num_searches == 0 else counter.most_common(num_searches)
        for key, count in sorted(search_list, key=lambda item: (-item[1], item[0])):
            key_string = ';'.join(list(key))
            file.write('{} {}\n'.format(count, key_string))


def list_terms_by_city(searches, input, size):
    city = input[0]
    city_search_terms = [search for search in searches if search['city'] == city]

    list_terms(city_search_terms, input[1:], size)


def list_terms(searches, input, size):
    num_terms = int(input[0])

    all_terms = [term for sublist in [search['terms'] for search in searches] for term in sublist]

    counter = Counter(all_terms)
    with open("res/{}/output.txt".format(size), "a") as file:
        list = counter.most_common() if num_terms == 0 else counter.most_common(num_terms)
        for key, count in sorted(list, key=lambda item: (-item[1], item[0])):
            file.write('{} {}\n'.format(count, key))


def mean_length_by_city(searches, input, size):
    city = input[0]
    city_searches = [search for search in searches if search['city'] == city]

    mean_length(city_searches, input[1:], size)


def mean_length(searches, input, size):
    lengths = [len(search['terms']) for search in searches]

    with open("res/{}/output.txt".format(size), "a") as file:
        mean = 0 if len(lengths) == 0 else float(sum(lengths)) / len(lengths)
        file.write('Media de termos {}\n'.format(int(mean)))


operation_callbacks = {
    'a': list_searches_by_city,
    'b': list_searches,
    'c': list_terms_by_city,
    'd': list_terms,
    'e': mean_length_by_city,
    'f': mean_length
}


def read_operations(size):
    operations = []
    with open('res/{}/operations.txt'.format(size), 'r') as file:
        lines = file.readlines()
        for line in lines:
            line_terms = line.split(";")
            operation = {}
            operation['code'] = unidecode(line_terms[0].strip().lower().decode('utf-8'))
            operation['input'] = [unidecode(term.strip().lower().decode('utf-8')) for term in line_terms[1:]]
            operations.append(operation)
    return operations


def read_searches(size):
    searches = []
    with open('res/{}/input.txt'.format(size), 'r') as file:
        lines = file.readlines()
        for line in lines:
            line_terms = line.split(";")
            search = {}
            search['city'] = unidecode(line_terms[0].strip().lower().decode('utf-8'))
            search['terms'] = [unidecode(term.strip().lower().decode('utf-8')) for term in line_terms[1:]]
            searches.append(search)
    return searches


def solve_small():
    searches = read_searches('small')
    operations = read_operations('small')

    for op in operations:
        operation_callbacks[op['code']](searches, op['input'], 'small')


def solve_large():
    searches = read_searches('large')
    operations = read_operations('large')

    for op in operations:
        operation_callbacks[op['code']](searches, op['input'], 'large')


def cleanup():
    open('res/small/output.txt', 'w').close()
    open('res/large/output.txt', 'w').close()
    open('res/evaluation/output.txt', 'w').close()


if __name__ == "__main__":
    cleanup()

    solve_small()
    solve_large()
