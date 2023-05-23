day = 0 

snail = input().split(' ')  #입력

while int( snail[2] ) > 1:  

    snail[2] = int( snail[2] ) - int( snail[0] ) + int( snail[1] )  #(거리) - (올라감) + (내려감)
    
    day = day + 1   #날짜

print(day)  #출력
