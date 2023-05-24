distance = 0    #거리
number = 1  #방번호

location = input()  #입력


while int(location) >= number:      #(위치) >= (방번호)

    distance = distance + 1
    number = number + distance * 6


print(distance + 1) #출력
