n, m = map(int, input().split())

# 금지 조합 저장
forbidden = set()
for _ in range(m):
    a,b = map(int, input().split())
    forbidden.add((min(a,b), max(a,b)))

# 모든 3개 조합 확인
count = 0
## i=1...n -> j=2...n, -> k=3...n
for i in range(1, n+1):
    for j in range(i+1, n+1):
        for k in range(j+1, n+1):
            # 세 쌍 모두 금지되지 않았는지 확인
            if ((i,j) not in forbidden and 
                (i,k) not in forbidden and 
                (j,k) not in forbidden):
                count += 1

print(count)