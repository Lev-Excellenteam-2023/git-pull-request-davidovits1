def parseltongue():
    count = 0
    word = ''
    data = open('resources/logo.jpg', 'rb')

    for i in data:
        for j in i:
            if 97 <= j <= 121 or j == 32:
                count += 1
                word += chr(j)
            else:
                count = 0
                word = ''
            if count >= 5 and chr(j) == '!':
                count = 0
                word += chr(j)
                yield word
                word = ''


our_generator = parseltongue()
for item in our_generator:
    print(item)
