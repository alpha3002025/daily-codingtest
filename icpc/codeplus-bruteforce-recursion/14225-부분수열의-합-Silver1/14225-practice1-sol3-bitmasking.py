n = int(input())
s = list(map(int, input().split()))

# 모든 부분수열의 합을 저장할 집합
sums = set()

# 2^n개의 모든 부분집합 탐색
for i in range(1, 1 << n):  # 1부터 2^n-1까지 (공집합 제외)
    total = 0
    for j in range(n):
        if i & (1 << j):  # j번째 비트가 1이면
            total += s[j]
    sums.add(total)

# 만들 수 없는 가장 작은 자연수 찾기
answer = 1
while True:
    if answer not in sums:
        print(answer)
        break
    answer+=1

# answer = 1
# while answer in sums:
#     answer += 1

# print(answer)