ls = []


for y in range(9):      #y좌표

    ls.append( input().split(" ") ) #입력

    for x in range(8):      #x좌표

        if x == 0 and y == 0:   #변수선언용

            output = [ls[y][x], y, x]      

        elif int(output[0]) < int(ls[y][x + 1]):        #뒤가 더 클때

            output = [ls[y][x + 1], y, x + 1]
                        


print( output[0])                       #출력
print(output[1] + 1, output[2] + 1 )
