import sys

input = sys.stdin.readline

# 행의 갯수 n 열의 갯수 m 공백
n, m = map(int, input().split())
# 각 카드에 적힌 숫자 

answer = 0
'''
# for문으로 한줄씩 받아서 바로 바로 비교하기
for i in range(n):
    n_list = list(map(int, input().split()))
    min_n = min(n_list)
    answer = max(answer,min_n)

print(answer)
'''
# 2중 반복문 구조사용

for i in range(n):
    n_list = list(map(int, input().split()))
    min_n = 10001
    for n in n_list:
        min_n = min(min_n, n)
    answer = max(answer, min_n)
print(answer)