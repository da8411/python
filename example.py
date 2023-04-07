import sys

iter_num = int(sys.stdin.readline())
budget = []

for i in range(iter_num):
    x = int(sys.stdin.readline())
    if x == 0:
        budget.pop()
    else:
        budget.append(x)

print(sum(budget))