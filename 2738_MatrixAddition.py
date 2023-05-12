number = input().split(' ')

list_one = []
list_two = []

for i in range( int( number[1] ) ):                 #list_one 입력

    list_one.append( input().split(' ') )

for i in range( int( number[1] ) ):                 #list_twe 입력

    list_two.append( input().split(' ') )

for y in range( int( number[1] ) ):                 #계산 및 출력

    for x in range( int( number[0] ) ):

        print( int( list_one[y][x] ) + int( list_two[y][x] ), "",end="")

    print()
