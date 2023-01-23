# 1부터 10,000까지 숫자 중 생성자가 있는 숫자를 제외한 셀프 넘버를 출력하는 문제
# 생성자가 있는 숫자의 리스트(또는 집합)를 먼저 생성
# 1부터 10,000까지의 숫자 범위에서 생성자가 있는 숫자를 제거

numbers = list(range(1, 10_001))
remove_list = []  # 이후에 삭제할 숫자 list
for num in numbers :
    for n in str(num):
        num += int(n)  # 생성자가 있는 숫자
    if num <= 10_000:  # 10,000보다 작거나 같을 때만,
        remove_list.append(num)  # append: 리스트에 요소를 추가할 때

for remove_num in set(remove_list) :  # set 으로 중복값 제거
    numbers.remove(remove_num)
for self_num in numbers :  # 생성자가 있는 숫자를 삭제한 리스트
    print(self_num)