def interleave(*argu):
    flat_list = []
    for i in range(len(argu)):
        for item in argu:
            flat_list.append(item[i])
    return flat_list


def generator_interleave(*argu):
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