# David Ovits
# exercise 5.2 cup of join


def join(*lists, sep=None):
    """
    The function receives lists and returns a single list separated by sea or "-" by default
    :param lists: lists
    :param sep: Separation between the lists
    :return: A single list
    """
    if lists != ():
        flat_list = lists[0]
        for i in range(1, len(lists)):
            if sep is not None:
                flat_list.append(sep)
            else:
                flat_list.append("-")
            item_list = lists[i]
            for j in item_list:
                flat_list.append(j)

        return flat_list
    else:
        return "ERROR"


assert join([1, 2], [8], [9, 5, 6], sep='@') == [1, 2, '@', 8, '@', 9, 5, 6], 'Not the expected result'
assert(join([1, 2], [8], [9, 5, 6])) == [1, 2, '-', 8, '-', 9, 5, 6], 'Not the expected result'
assert(join([1])) == [1], 'Not the expected result'
assert join() == "ERROR", 'Not the expected result'


