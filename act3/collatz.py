def collatz(number):
    if number % 2 == 0:
        return number//2
    elif number % 2 == 1:
        return 3*number+1

Num = int(input('Input a number:'))
while Num != 1:
    NewNum = int(collatz(Num))
    print(NewNum)
    Num = NewNum


