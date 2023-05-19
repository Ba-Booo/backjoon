i = 1

while i != 0:       #반복문
    
    number = input().split(' ')     #입력

    if int( number[0] ) == 0 and int( number[1] ) == 0:     #입력이 0,0일때 탈출

        break

    elif int( number[1] ) % int( number[0] ) == 0:      #약수일때

        print("factor")

    elif int( number[0] ) % int( number[1] ) == 0:      #배수일때

        print("multiple")

    else:       #아무것도 아닐때

        print("neither")
