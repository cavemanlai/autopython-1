#! python3

def boxPrint(symbol, width, hight):
    if len(symbol) != 1:
        raise Exception('symbol must be a single character string')
    if width <= 2:
        raise Exception('width must be greater than 2')
    if hight <= 2:
        raise Exception('hight must be greater than 2')
    print(symbol * width)
    for i in range(hight - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

for sym, w, h in (('*', 4, 4), ('0', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        boxPrint(sym, w, h)
    except Exception as err:
        print('an exception happened:' + str(err))