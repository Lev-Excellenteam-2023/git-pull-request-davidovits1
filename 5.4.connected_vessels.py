def interleave(*argu):
    flat_list = []
    for i in range(len(argu)):
        for item in argu:
            flat_list.append(item[i])

    yield flat_list


our_generator = interleave('abc', [1, 2, 3], ('!', '@', '#'))
for item in our_generator:
    print(item)