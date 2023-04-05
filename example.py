A, B = map(int, input().split())

m = int(input())

num = list(map(int, input().split()))

result = []

n = 0

for i in range(len(num)):
    n = n + (num.pop() * (A**i))
    
while n:
    result.append(n%B)
    n //= B
    
while result:
    print(result.pop(), end=' ')