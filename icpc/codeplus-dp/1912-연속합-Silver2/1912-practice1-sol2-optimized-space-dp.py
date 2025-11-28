n = int(input())
arr = list(map(int, input().split()))

current_sum = arr[0]  # 현재 위치를 포함하는 최대 연속합
max_sum = arr[0]      # 전체 최댓값

for i in range(1, n):
    # 이전 합에 추가 vs 새로 시작
    current_sum = max(arr[i], current_sum + arr[i])
    # 최댓값 갱신
    max_sum = max(max_sum, current_sum)

print(max_sum)