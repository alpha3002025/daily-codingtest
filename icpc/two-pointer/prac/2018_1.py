import sys

N: int = int(sys.stdin.readline().strip())

left: int = 0
right: int = 0
total = 0
cnt = 0

while right <= N:
    if total == N:
        cnt+=1
        right+=1
        total+=right
    elif total > N:
        left+=1
        total -= left
    elif total < N:
        right+=1
        total += right

print(f"{cnt}")