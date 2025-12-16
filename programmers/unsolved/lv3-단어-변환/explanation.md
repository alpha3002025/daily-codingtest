# 단어 변환

## 문제 설명
두 단어 `begin`, `target`과 단어의 집합 `words`가 있습니다.
`begin`에서 `target`으로 변환하는 가장 짧은 과정을 찾으세요.
규칙:
1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
2. `words`에 있는 단어로만 변환할 수 있습니다.

## 문제 해결 전략

**BFS (너비 우선 탐색)**를 사용하여 최단 거리를 찾습니다.
- 상태: `(current_word, step_count)`
- 다음 상태: `words` 중 현재 단어와 **알파벳이 딱 1개만 다른 단어**.
- `visited` 체크 필수.

## Python 코드

```python
from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
        
    q = deque([(begin, 0)])
    visited = [False] * len(words)
    
    while q:
        curr, step = q.popleft()
        
        if curr == target:
            return step
        
        for i in range(len(words)):
            if visited[i]:
                continue
            
            # 한 글자 차이 확인
            diff = 0
            for a, b in zip(curr, words[i]):
                if a != b:
                    diff += 1
            
            if diff == 1:
                visited[i] = True
                q.append((words[i], step + 1))
                
    return 0
```
