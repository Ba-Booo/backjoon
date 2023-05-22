number = 0

nk = input().split()    #입력

if int( nk[0] ) % int( nk[1] ) == 0:    #k가 n의 약수일때

    for i in range(1, int( nk[0] ) + 1 ):   #n만큼 반복

        if int( nk[0] ) % i == 0:   #i가 약수일때

            number = number + 1
    

        if number == int( nk[1] ):  #number이 k와 같을때

            measure = i
            break


if int( nk[1] ) == number:  #k가 n의 약수 개수보다 작을때

    print(measure)

else:

    print(0)
