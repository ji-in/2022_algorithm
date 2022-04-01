import math

def k_digit(n, k):
    res = ''
    while n != 0:
        res += str(n % k)
        n //= k
    return res[::-1]

def check_prime(n):
    if n == 1: 
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    res = k_digit(n, k)
    num_list = res.split('0')

    for num in num_list:
        if num != '' and check_prime(int(num)):
            answer += 1            

    return answer
    