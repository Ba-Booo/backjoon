ls = []     #변수선언  
x = 0

for i in range(5):      #입력
    ls.append( input().split(" ") )


while x != -1:       #출력

    end = 0

    for y in range(5):

        if len(ls[y]) > x:

            print( ls[y][x], end="" )
            
        else:
            end = end + 1


    if end == 5:        #탈출
        break

    x = x + 1