# 가장 가까운 같은 글자

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/142086)

문자열 `s`가 주어졌을 때, 각 위치의 문자에 대해 **자신보다 앞에 나왔으면서, 자신과 가장 가까운 곳에 있는 같은 글자**가 어디 있는지 찾습니다.
- 있다면: 현재 위치 - 그 위치 (거리)
- 없다면: -1
결과를 배열에 담아 반환하세요.

## 해결 전략
문자열을 앞에서부터 순회하며 "각 문자가 마지막으로 등장한 인덱스"를 기억해두면 됩니다.
**딕셔너리(`last_idx_map`)**를 사용하여 `{문자: 마지막인덱스}`를 계속 갱신합니다.

### 알고리즘 순서
1. `last_idx` = {} (비어 있는 딕셔너리)
2. `result` = []
3. `s`를 순회하며 (`i`, `char`):
    - 만약 `char`가 `last_idx`에 있다면:
        - `dist` = `i` - `last_idx[char]`
        - `result.append(dist)`
    - 없다면:
        - `result.append(-1)`
    - `last_idx[char] = i` (현재 위치로 갱신)
4. `result` 반환.

## Python 코드

```python
def solution(s):
    last_idx = {}
    answer = []
    
    for i, char in enumerate(s):
        if char in last_idx:
            # 거리 계산: 현재 위치 - 마지막 위치
            answer.append(i - last_idx[char])
        else:
            answer.append(-1)
            
        # 마지막 등장 위치 갱신
        last_idx[char] = i
        
    return answer
```

## 배운 점 / 팁
- **Hash Map 활용**: "마지막으로 본 위치" 같은 상태를 저장하고 조회하는 데 O(1) 성능을 내는 딕셔너리가 제격입니다.
- **실시간 갱신**: 데이터를 한 번 다 훑고 나서 처리하는 게 아니라, 순회하면서 조회와 동시에 갱신(Update)하는 패턴입니다.
