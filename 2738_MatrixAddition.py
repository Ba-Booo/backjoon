number = input().split(' ')

list_one = []
list_two = []

for i in range( int( number[1] ) ):                 #list_one 입력

    fake_list = []
    fake_list.append( input().split(' ') )
    list_one = list_one + fake_list

for i in range( int( number[1] ) ):                 #list_twe 입력

    fake_list = []
    fake_list.append( input().split(' ') )
    list_two = list_two + fake_list


for y in range( int( number[1] ) ):                 #계산 및 출력

    for x in range( int( number[0] ) ):

        print( int( list_one[x][y] ) + int( list_two[x][y] ), "",end="")

    print()
