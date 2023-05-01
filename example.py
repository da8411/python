import sys

input = sys.stdin.readline
n = int(input())
t = int(input())
c = [[] for i in range(n + 1)] # 각 컴퓨터마다 연결 된 컴퓨터 정보 저장
q = [] # 탐색할 컴퓨터 배열
visit = [0] * (n + 1) # 탐색한 컴퓨터 방문 확인용 배열

for i in range(t):
	c1, c2 = map(int, input().split())
	c[c1].append(c2) # c[1] = = [2, 5] c[2] = 3 ... 과 같이 저장
	c[c2].append(c1)

q.append(1) # 가장 먼저 탐색할 1번 컴퓨터 q에 삽입

while q: # 탐색할 컴퓨터가 있는 동안
    tmp = q.pop(0) # 팀색할 컴퓨터 pop
    visit[tmp] = 1 # 방문 처리
    for i in c[tmp]: # 해당 컴퓨터에 연결된 컴퓨터 모두 조사
        if visit[i] != 1: # 아직 방문하지 않은 컴퓨터라면
            visit[i] = 1 # 방문처리 후
            q.append(i) # q에 삽입

print(visit[2:].count(1)) # 1번 컴퓨터 제외 2번 컴퓨터부터 방문한 컴퓨터 개수 반환