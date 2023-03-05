# David Ovits
# exercise 5.4 connected_vessels


def interleave(*argu):
    """
    get one or more iterable parameters, and returns a list of interlaced members
    :param argu: One or more iterable parameters
    :return: All the members in one list are intertwined
    """
    flat_list = []
    for i in range(len(argu)):
        for item in argu:
            flat_list.append(item[i])
    return flat_list


def generator_interleave(*argu):
    """
    get one or more iterable parameters, and returns a list of interlaced members
     (one more at a time)
    :param argu: One or more iterable parameters
    :return: All the members in one list are intertwined in the generator version (one more member each time)
    """
    flat_list = []
    for i in range(len(argu)):
        for item in argu:
            flat_list.append(item[i])
            yield flat_list


print(interleave('abc', [1, 2, 3], ('!', '@', '#')))

print("\n##### generator_interleave ####\n")

our_generator = generator_interleave('abc', [1, 2, 3], ('!', '@', '#'))
for item in our_generator:
    print(item)
