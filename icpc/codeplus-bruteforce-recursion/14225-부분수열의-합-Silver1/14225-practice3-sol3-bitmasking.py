N = int(input())
S = list(map(int, input().split()))

# 모든 부분수열의 합을 저장할 집합
sum_set = set()

for i in range(1, 1<<N): ## 1 ~ (2^N)-1 
                         ## 모든 자릿수의 표현
    acc = 0
    for j in range(N): ## 1 ~ N (자리수의 개수)
        if i & (1<<j): ## 각 자리수에 대해 더하느냐 마느냐를 1로 표시한 것을 현재 경우의 수인 i 의 값과 대조해
                       ## 현재 턴에서 해당 자리수를 더할지를 체크
            acc += S[j]
    
    sum_set.add(acc)

answer = 1
while True:
    if answer not in sum_set:
        print(answer)
        break
    answer += 1