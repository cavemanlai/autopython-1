try:
    char = input('input a char: ')
    int(char)
    print('it is int')
except ValueError:
    print('it is not int,input a int')