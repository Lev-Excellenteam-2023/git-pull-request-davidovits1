# David Ovits
# exercise 5.3 parseltongue

FILE_NAME = 'resources/logo.jpg'


def parseltongue(file_name):
    """
    Gets the name of a file and returns words found there if there is a sequence
     of 5 or more lowercase letters and an exclamation mark at the end
    :param file_name: name of file
    :return: Secret messages from the file name
    """
    count = 0
    data = open(file_name, 'rb')
    word = ''
    while True:
        chr_byte = data.read(1)
        if not chr_byte:
            break
        if chr_byte.isalpha():
            word += chr_byte.decode()
            count += 1
        elif chr_byte == b'!'and count >= 5:
            yield word
            word = ''
            count = 0
        else:
            word = ''
            count = 0


our_generator = parseltongue(FILE_NAME)
for item in our_generator:
    print(item)
