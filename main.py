import os
from pprint import pprint

BASE_PATH = os.getcwd()
files = os.listdir(BASE_PATH)
txt = list(filter(lambda x: x.endswith('txt'), files))

list_ = []
sum = 0
text = ''


def custom_sort(element):
    return element[1]





for file in txt:
    with open(file, 'r', encoding='utf-8') as file_handler:
        sum = 0
        for line in file_handler:
           sum += 1
           text += line.strip()
        dict_ = [file, sum, text]
        list_.append(dict_)
list_.sort(key = custom_sort)

pprint(list_)



