import os
import re
import time

def print_docs(directory):
    for root, directories, files in os.walk(directory):
        for file in files:
            print(os.path.join(root, file))


def first():
    print_docs("/users/artem/Downloads/mobla")


def second():
    with open('./test.txt', 'r') as f:
        all_words = re.split('\s|\n', f.read())
        max_len = 0
        current_max_words = []

        for i in all_words:
            if max_len < len(i):
                current_max_words = [i]
                max_len = len(i)
            elif max_len == len(i):
                current_max_words.append(i)
        print(current_max_words)


def third():
    with open('rows_300.csv', 'w', newline='') as file:

        file.write('№;Секунда;Микросекунда\n')

        for i in range(1, 301):
            sec = time.time() // 1
            microsec = time.time() * 1000 % 1000 // 1

            file.write(str(i) + ";" + str(sec) + ";" + str(microsec) + "\n")

            time.sleep(0.01)

