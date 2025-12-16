# 타겟 넘버

## 문제 설명
$n$개의 음이 아닌 정수들이 주어질 때, 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 방법의 수를 구하세요.

### 핵심 개념
1.  **DFS/BFS (탐색)**: 각 숫자마다 `+` 또는 `-` 두 가지 선택지가 있습니다.
    - 트리의 깊이는 $n$, 리프 노드의 개수는 $2^n$개입니다.
    - $n$이 최대 20이므로 $2^{20} \approx 1,000,000$ 으로 충분히 완전 탐색이 가능합니다.
2.  **재귀 (Recursion)**: DFS 구현에 적합합니다.

## Python 풀이 (DFS)

```python
def solution(numbers, target):
    n = len(numbers)
    answer = 0
    
    def dfs(index, current_sum):
        nonlocal answer
        # Base Case: 마지막 숫자까지 다 썼을 때
        if index == n:
            if current_sum == target:
                answer += 1
            return
        
        # Recursive Step: 더하거나 빼거나
        dfs(index + 1, current_sum + numbers[index])
        dfs(index + 1, current_sum - numbers[index])
        
    dfs(0, 0)
    return answer
```

## Python 풀이 (BFS - Pythonic)
리스트의 각 단계마다 모든 가능한 합을 저장해 나가는 방식입니다.

```python
def solution(numbers, target):
    # 초기 상태: 합계 0 하나
    leaves = [0]
    
    for num in numbers:
        temp = []
        for leaf in leaves:
            # 기존 합들에 현재 숫자를 더하고 뺀 결과를 모두 저장
            temp.append(leaf + num)
            temp.append(leaf - num)
        leaves = temp
        
    # 최종 결과 중 target과 같은 것 개수 세기
    return leaves.count(target)
```

### 코드 설명
- BFS 방식(`leaves` 리스트 활용)은 직관적이고 코드가 짧지만, 계산된 리스트의 크기가 지수적으로 커지므로 메모리를 좀 더 사용합니다.
- DFS 방식은 스택 프레임만 사용하므로 메모리 효율이 좋습니다. 문제 제약조건($N=20$)에서는 둘 다 무난합니다.
