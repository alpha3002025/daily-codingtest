# 주식가격

## 문제 설명
초 단위로 기록된 주식 가격이 담긴 배열 `prices`가 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지 구하는 문제입니다.

### 핵심 개념
1.  **스택 (Stack)**: $O(N)$으로 효율적으로 해결하기 위해 스택을 사용합니다.
    - 스택에는 **아직 가격이 떨어지지 않은 시점의 인덱스**를 저장합니다.
    - 현재 가격(`prices[i]`)이 스택의 top에 있는 시점(`prices[stack[-1]]`)보다 낮다면, 가격이 떨어진 것입니다. 이때 스택에서 pop하여 "떨어질 때까지 걸린 시간"을 계산합니다.
2.  **완전 탐색 (Double Loop)**: $N$이 최대 100,000이므로 $O(N^2)$은 시간 초과(효율성 테스트) 가능성이 있지만, 주식 가격 문제에서는 단순 이중 루프로도 통과가 되는 경우가 많습니다. 하지만 정석은 스택입니다.

## Python 풀이 (Stack - O(N))

```python
def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = [] # 인덱스를 저장
    
    for i, price in enumerate(prices):
        # 스택이 비어있지 않고, 현재 가격이 스택의 top 가격보다 떨어졌다면
        while stack and prices[stack[-1]] > price:
            top_idx = stack.pop()
            # 떨어진 시점(i) - 저장된 시점(top_idx) = 버틴 시간
            answer[top_idx] = i - top_idx
            
        stack.append(i)
        
    # 끝까지 가격이 떨어지지 않은 인덱스들 처리
    # (전체 길이 - 1) - 시작 인덱스
    while stack:
        idx = stack.pop()
        answer[idx] = (n - 1) - idx
        
    return answer
```

### 코드 설명
- `stack`에는 "가격이 떨어지지 않은 상태인 인덱스들"이 오름차순(시간순)으로 쌓여 있습니다.
- 새로운 가격이 들어올 때마다, 스택의 끝(가장 최근) 가격과 비교합니다.
- 가격이 떨어졌으면(`current < stack_top`), 그 시점(`stack_top`)의 *가격 방어*는 끝난 것이므로 pop하고 시간을 계산합니다.
- 루프가 끝난 후에도 스택에 남아있는 값들은 끝까지 가격이 떨어지지 않은 경우입니다. 전체 시간(n-1)에서 해당 시점을 빼서 기간을 구합니다.

## Python 풀이 (Brute Force - O(N^2))
직관적이지만 데이터가 많으면 느립니다.

```python
def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            answer[i] += 1
            if prices[i] > prices[j]:  # 가격이 떨어지면 중단
                break
    return answer
```
