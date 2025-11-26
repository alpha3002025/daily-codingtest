n = int(input())
s = list(map(int, input().split()))
sums = set()

def backtrack(idx, total):
    if idx == n:
        if total > 0:
            sums.add(total)
        return
    
    # 현재 원소 포함
    backtrack(idx + 1, total + s[idx])
    # 현재 원소 미포함
    backtrack(idx + 1, total)

backtrack(0, 0)

answer = 1
while answer in sums:
    answer += 1

print(answer)