N = int(input())

# 이전 자리의 값만 저장
prev_0, prev_1 = 0, 1

for i in range(2, N + 1):
    curr_0 = prev_0 + prev_1  # 현재 0으로 끝나는 경우
    curr_1 = prev_0            # 현재 1로 끝나는 경우
    prev_0, prev_1 = curr_0, curr_1

print(prev_0 + prev_1)