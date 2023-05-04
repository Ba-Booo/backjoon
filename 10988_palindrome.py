palindrome = input()                                                        #입력

if len(palindrome) % 2 == 1:                                                #홀수일때
    left = palindrome[ : int(len(palindrome)/2)]
    right = palindrome[ len(palindrome) : int(len(palindrome)/2) : -1 ]     
else:                                                                       #짝수일때
    left = palindrome[ : int(len(palindrome)/2)]
    right = palindrome[ len(palindrome) : int(len(palindrome)/2)-1 : -1 ]

if left == right:                                                           #결과확인
    print(1)
else:
    print(0)