size = int(input('Enter the size of the pattern: '))

loops = 0

while loops < size:
    for i in range(1, size + 1):
        print('*', end='')
    print('\n')
    loops += 1
