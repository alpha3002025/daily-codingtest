from bisect import bisect_left
import sys

input = sys.stdin.readline

# 11055번: 가장 큰 증가하는 부분 수열 (Largest Increasing Subsequence)
# https://www.acmicpc.net/problem/11055

# bisect_left를 활용한 풀이
# 일반적인 LIS(길이) 구하는 O(N log N) 알고리즘과 달리, 
# '합'을 최대화해야 하므로 단순한 tails 배열로는 불가능합니다.
# 대신 (마지막 값, 누적 합) 쌍을 관리하며, "마지막 값이 커질수록 합도 커져야 한다"는 
# 최적의 상태들(Pareto frontier)만 유지하는 방식으로 bisect를 활용할 수 있습니다.
# 이 방식은 리스트 삽입/삭제가 있어 최악의 경우 O(N^2)이지만, bisect를 사용하여 탐색을 최적화합니다.

N = int(input())
if N == 0:
    print(0)
    sys.exit()

A = list(map(int, input().split()))

# tails: 증가하는 부분 수열의 마지막 값들을 저장 (오름차순 정렬 유지)
# max_sums: 해당 tails[i]로 끝나는 부분 수열의 최대 합 (오름차순 정렬 유지되도록 관리)
# tails[i]가 증가하면 max_sums[i]도 반드시 증가해야 함 (그렇지 않은 원소는 제거)
tails = [0]
max_sums = [0]

for x in A:
    # 1. x보다 작은 값들 중에서 가장 큰 값의 위치를 찾음
    # tails[i-1] < x <= tails[i] 가 되는 idx를 찾음
    idx = bisect_left(tails, x)
    
    # x를 마지막으로 하는 새로운 부분 수열의 합 계산
    # idx-1 위치의 값은 x보다 작은 값 중 가장 큰 값 (및 그에 대응하는 최대 합)
    current_sum = max_sums[idx-1] + x
    
    # 2. x를 tails에 삽입하거나 업데이트
    # 만약 tails[idx]가 이미 x라면 (같은 값이 있는 경우), 더 큰 합으로만 업데이트
    if idx < len(tails) and tails[idx] == x:
        if current_sum > max_sums[idx]:
            max_sums[idx] = current_sum
            # 업데이트 후 뒤쪽 원소들이 '지배(dominated)'되는지 확인 필요하므로 아래쪽 prune 로직으로 이어짐
        else:
            # 기존 합이 더 크거나 같으면 이 x는 쓸모 없음
            continue
    else:
        # x가 tails에 없다면 삽입
        tails.insert(idx, x)
        max_sums.insert(idx, current_sum)
    
    # 3. 불필요한 원소 제거 (Pruning)
    # tails는 오름차순으로 유지됨.
    # 만약 tails[j] > x 인데 max_sums[j] <= current_sum 이라면,
    # (tails[j], max_sums[j])는 (x, current_sum)보다 비효율적임 (더 큰 값으로 끝리는데 합은 작거나 같으므로)
    # 따라서 이런 원소들을 제거하여 'tails 증가 -> max_sums 증가' 성질 유지
    
    # idx 위치에 x가 들어갔으므로, idx+1 부터 확인
    while idx + 1 < len(tails) and max_sums[idx+1] <= current_sum:
        tails.pop(idx+1)
        max_sums.pop(idx+1)

print(max_sums[-1])