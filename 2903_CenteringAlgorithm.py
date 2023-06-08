n = input()

dot = 2 #기본 점 개수

for i in range( int( n ) ):

    dot = dot * 2 - 1   #점들 사이에 추가한 점을 더한 개수

print( dot ** 2 )