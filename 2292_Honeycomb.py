distance = 0
number = 1

location = input()


while int(location) >= number:  

    distance = distance + 1
    number = number + distance * 6


print(distance + 1)