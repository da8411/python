#baekjoon_2587
x = [] 

for i in range(5):
    x.append(int(input()))

x.sort() #x정렬

print(int(sum(x)/5)) #평균
print(x[2]) #중앙값

#baekjoon_25305

n,k = map(int,input().split())
scores = list(map(int,input().split()))
scores.sort(reverse=True) #내림차순 정렬
print(scores[k-1])