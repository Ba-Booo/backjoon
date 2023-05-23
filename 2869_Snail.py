day = 0 #버그시발

snail = input().split(' ')

while int( snail[2] ) > 1:

    snail[2] = int( snail[2] ) - int( snail[0] ) + int( snail[1] )
    
    day = day + 1

print(day)