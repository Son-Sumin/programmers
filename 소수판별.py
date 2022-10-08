# 2~30 소수 리스트 뽑아내기
# 방법1
prime = []
for i in range(2,31):
    isPrimary = True
    for j in range(2, i) :
        if i % j == 0:
            isPrimary = False
            break
    if isPrimary :
        prime.append(i)
print(prime)

# 방법2
def isPrime(x) :
    if x == 1: return False
    for i in range(2,int(x**1.5)) :
        if x % i == 0 :
            return False
    return True

numlist = [1,2,3,4,5,6,7,8,9,10,11,12,13]
primelist = list(filter(isPrime,numlist))
print(primelist)