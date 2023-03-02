# David Ovits
# exercise 5.1 That's the way

import os

NAME = "DEEP"
PATH = "images"


def find_file(path):
    """
    Gets a folder path and returns the files that start with "deep"
    :param path: folder path
    :return: list of name files
    """
    list_name_files = []
    try:
        name_files = os.listdir(path)
        for file in name_files:
            if file[0:4].lower() == NAME.lower():
                list_name_files.append(file)

    except FileNotFoundError:
        list_name_files.append('No path exists')

    return list_name_files


assert find_file(PATH) == ['deeper.svg', 'deeper2.svg'], 'Not the expected result'
assert find_file('c') == ['No path exists'], 'Not the expected result'
