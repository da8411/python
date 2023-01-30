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

#baekjoon_1181

n = int(input())
lst = []

for i in range(n):
    lst.append(input())

set_lst = set(lst)	# set으로 변환해서 중복값을 제거
lst = list(set_lst)	# 다시 list로 변환

lst.sort()
lst.sort(key = len)

for i in lst:
    print(i)