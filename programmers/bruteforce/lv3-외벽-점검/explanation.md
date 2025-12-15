# 외벽 점검 (Wall Inspection)

## 1. 문제 설명
- **문제 링크**: [https://school.programmers.co.kr/learn/courses/30/lessons/60062](https://school.programmers.co.kr/learn/courses/30/lessons/60062)
- **정보**:
  - 카카오 블라인드 채용 문제.
  - 외벽의 총 둘레 $n$, 취약 지점의 위치 배열 `weak`, 친구들이 이동할 수 있는 거리 배열 `dist`가 주어집니다.
  - 취약 지점을 모두 점검하기 위해 투입해야 하는 친구 수의 최솟값을 반환해야 합니다.
  - 불가능할 경우 -1을 반환합니다.
- **제한사항**:
  - `weak`의 길이(취약 지점 수): 1 이상 15 이하.
  - `dist`의 길이(친구 수): 1 이상 8 이하.

---

## 2. 접근법 및 핵심 개념 (Brute Force + Permutation)

### 개념 1: 원형을 선형으로 변환
원형 문제는 시작과 끝이 연결되어 있어 처리가 까다롭습니다. 이를 해결하는 가장 일반적인 테크닉은 **배열을 2배로 늘려 선형(직선)으로 만드는 것**입니다.
- 예: `n=12`, `weak=[1, 5, 10]`
- 변환: `weak_linear = [1, 5, 10, 13, 17, 22]` (각 원소에 $n$을 더한 값을 뒤에 붙임)
- 이렇게 하면 `10`번 지점에서 출발해 `1`번 지점(`13`으로 표현됨)을 커버하는 경우를 연속된 인덱스로 처리할 수 있습니다.

### 개념 2: 완전 탐색 (순열)
`weak`의 길이가 최대 15, `dist`의 길이가 최대 8로 매우 작습니다. 이는 **완전 탐색**이 가능하다는 신호입니다.
우리는 다음 두 가지를 고려해야 합니다.
1. **어디서 시작할 것인가?**: `weak`의 모든 지점을 시작점으로 고려해봐야 합니다.
2. **누구를 먼저 보낼 것인가?**: 이동 거리가 긴 친구를 먼저 보낼지, 짧은 친구를 먼저 보낼지에 따라 결과가 달라집니다. 따라서 친구들의 투입 순서(순열)를 모두 확인해야 합니다.

### 알고리즘 로직
1. `weak` 배열을 2배로 확장하여 `weak_linear`를 만듭니다.
2. `dist` 배열(친구들)의 모든 **순열(Permutations)**을 구합니다.
3. `weak`의 각 지점을 시작점(`start`)으로 설정하고 반복합니다:
   - 각 순열마다 친구들을 차례대로 투입합니다.
   - 첫 번째 친구가 `start` 지점부터 어디까지 커버하는지 계산합니다.
   - 커버하지 못한 지점이 나오면 다음 친구를 투입합니다.
   - 모든 취약 지점을 커버하면 투입된 친구 수를 기록하고 최솟값을 갱신합니다.

---

## 3. Python 풀이

```python
from itertools import permutations

def solution(n, weak, dist):
    # 취약점 개수
    length = len(weak)
    # 원형을 선형으로 변환 (길이 2배)
    # [1, 5, 10] -> [1, 5, 10, 13, 17, 22] (n=12일 때)
    weak_linear = weak + [w + n for w in weak]
    
    # 최솟값을 구하기 위해 초기값을 친구 수 + 1로 설정
    answer = len(dist) + 1
    
    # 1. 시작점을 weak의 모든 지점으로 설정하며 탐색
    for start in range(length):
        # 2. 친구를 투입하는 순서의 모든 경우 (순열)
        for friends in permutations(dist, len(dist)):
            count = 1 # 투입된 친구 수
            # 현재 친구가 커버할 수 있는 마지막 위치
            # 시작점(weak_linear[start])에서 친구의 이동 거리만큼 더함
            position = weak_linear[start] + friends[count-1]
            
            # 시작점부터 포인터 이동하며 확인
            # start부터 start + length까지가 우리가 확인해야 할 전체 취약점 구간
            for index in range(start, start + length):
                # 현재 커버 가능한 위치(position)보다 취약점 위치가 멀다면
                if position < weak_linear[index]:
                    count += 1 # 친구 추가 투입
                    if count > len(dist): # 친구를 다 썼는데도 부족하면 중단
                        break
                    
                    # 새로운 친구 투입: 현재 커버 못한 지점(weak_linear[index])부터 시작
                    position = weak_linear[index] + friends[count-1]
            
            # 끝까지 도달해서 모든 취약점을 커버한 경우
            else: # (for-else 문법: break 없이 루프가 끝나면 실행)
                answer = min(answer, count)
    
    if answer > len(dist):
        return -1
    
    return answer
```

### 코드 분석
- **`permutations(dist, len(dist))`**: 친구들의 순서를 섞는 모든 경우의 수입니다. 최대 $8! = 40,320$가지입니다.
- **`for start in range(length)`**: 시작점을 바꾸는 루프입니다. 최대 15번 반복합니다.
- 내부 로직은 선형 탐색이므로 `weak` 길이만큼 수행됩니다.
- 전체 연산량은 대략 $15 \times 40,320 \times 15 \approx 9,000,000$ 정도로, Python 기준 1초 내에 충분히 수행 가능합니다.

---

## 4. 복잡도 분석
- **시간 복잡도**: $O(W^2 \cdot P)$
  - $W$: 취약 지점의 개수 (최대 15)
  - $P$: 친구의 수에 대한 팩토리얼 ($D!$, 최대 $8!$)
  - $15 \times 15 \times 40,320 \approx 9 \times 10^6$.
- **공간 복잡도**: $O(W \times D!)$ 또는 $O(W)$ (구현에 따라 다름)
  - 단순히 순열을 하나씩 생성해 처리하면 메모리는 크게 필요하지 않습니다. 리스트 확장에 $O(W)$ 정도 사용됩니다.
