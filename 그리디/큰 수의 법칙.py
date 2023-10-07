import sys

input = sys.stdin.readline

# n,m, k 입력받기
n, m, k = map(int, input().split())
# n 개의 수 입력 받기
n_list = list(map(int, input().split()))

n_list.sort()

first_big_n = n_list[-1]
second_big_n = n_list[-2]
answer = 0
"""
# 이 방식은 m 이 커질 수록 시간이 오래 걸린다.
# 하나씩 더해서 해결하는 방식이기 때문에
while True:
    for i in range(k):
        if m == 0:
            break
        answer += first_big_n
        m -= 1
    if m == 0:
        break
    answer += second_big_n
    m -= 1
    
print(answer)
"""

# 최댓값을 (6+6+6+5) + (6+6+6+5) 라고 생각해보자
# 반복되는 수열에 대해서 파악이 중요

# 가장 큰 수 묶음이 더해지는 경우를 계산
cnt = int(m / (k + 1)) * k
cnt += m % (k + 1)

answer = 0
answer += cnt * first_big_n
answer += (m - cnt) * second_big_n
print(answer)
