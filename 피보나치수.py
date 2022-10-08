#피보나치 수
# F(2) = F(0) + F(1) = 0 + 1 = 1
# F(3) = F(1) + F(2) = 1 + 1 = 2
# F(4) = F(2) + F(3) = 1 + 2 = 3
# F(5) = F(3) + F(4) = 2 + 3 = 5


def solution(n:int) : 
    answer = 1
    first = 0
    second = 1
    for i in range(2, n+1):
        answer = first + second
        first = second
        second = answer
    return answer % 1234567

print(solution(3))
print(solution(5)) 