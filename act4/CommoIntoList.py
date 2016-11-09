def CommoIntoList(list):
    headvalue = []
    commovalue = []
    for i in range(0,len(list)-1):
        headvalue.append(str(list[i]) + ', ')
    for I in range(0,len(headvalue)):
        commovalue.append(str(headvalue[I]))
        print(commovalue[I], end='')
    print('and ' + str(list[-1]))

L = ['a','c','james',1,[2,3,4,5]]
CommoIntoList(L)