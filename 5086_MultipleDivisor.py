i = 1

while i != 0:
    
    number = input().split(' ')

    if int( number[0] ) == 0 and int( number[1] ) == 0:

        break

    elif int( number[1] ) % int( number[0] ) == 0:

        print("factor")

    elif int( number[0] ) % int( number[1] ) == 0:

        print("multiple")

    else:

        print("neither")