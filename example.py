x = [] 

for i in range(5):
    x.append(int(input()))

x.sort() #x정렬

print(int(sum(x)/5)) #평균
print(x[2]) #중앙값