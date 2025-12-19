# 시소 짝꿍
{100, 100} 은 서로 같은 거리에 마주보고 앉으면 균형을 이룹니다.
- e.g. 좌: 2m, 우: 2m (100x2 = 100x2)

{180, 360} 은 각각 4(m), 2(m) 거리에 마주보고 앉으면 균형을 이룹니다.
- e.g. 좌: 4m, 우: 2m (180x4 = 360x2)

{180, 270} 은 각각 3(m), 2(m) 거리에 마주보고 앉으면 균형을 이룹니다.
- e.g. 좌: 3m, 우: 2m (180x3 = 270x2)

{270, 360} 은 각각 4(m), 3(m) 거리에 마주보고 앉으면 균형을 이룹니다.
- e.g. 좌: 4m, 우: 3m (270x4 = 360x3)

<br/>
<br/>

## 문제 설명
시소는 중심으로부터 2m, 3m, 4m 거리에 좌석이 있습니다.
두 사람이 시소에 앉아 평형을 이루면 "시소 짝꿍"이라고 합니다.
즉, `몸무게 A * 거리 A = 몸무게 B * 거리 B`가 성립해야 합니다.
사람들의 몸무게 목록 `weights`가 주어질 때 시소 짝꿍이 몇 쌍인지 구하는 문제입니다.

<br/>
<br/>


## 풀이 개념
**카운터(Dictionary)**를 활용한 수학 문제입니다.
가능한 거리 비율은 (2, 2), (2, 3), (2, 4), (3, 2), (3, 4), (4, 2), (4, 3) 입니다.
이를 몸무게 비율로 정리하면 1:1, 2:3, 1:2(2:4), 3:4 총 4가지 케이스만 고려하면 됩니다. (반대 비율은 중복이므로 한쪽만 계산하거나 정렬 후 계산)

1. 몸무게 별 인원수를 `Counter`로 셉니다.
2. `weights`의 중복을 제거한 유니크한 몸무게 `w`를 순회합니다.
3. 해당 몸무게 `w`를 가진 사람끼리의 짝꿍 수 계산: `n * (n-1) / 2`.
4. 다른 몸무게와의 짝꿍 여부 확인:
   - `w`가 더 작은 쪽이라고 가정하고, `w`보다 큰 짝꿍 몸무게 `target`을 찾습니다.
   - 비율: `w * 2 = target * 1` (불가능, w < target 이므로),
   - `w * 3 = target * 2` -> `target = w * 3 / 2`
   - `w * 4 = target * 2` -> `target = w * 2`
   - `w * 4 = target * 3` -> `target = w * 4 / 3`
5. 계산된 `target`이 정수이고 `Counter`에 존재하면, `count(w) * count(target)` 만큼 쌍을 추가합니다.

## 코드 (Python)

```python
from collections import Counter

def solution(weights):
    counter = Counter(weights)
    answer = 0
    
    # 1. 같은 몸무게끼리 (1:1 비율)
    for k, v in counter.items():
        if v > 1:
            answer += v * (v - 1) // 2
            
    # 2. 다른 몸무게끼리 (2:3, 2:4, 3:4 비율)
    # 중복 계산 방지를 위해 keys를 정렬하거나 set을 사용
    # 여기서는 dict를 순회하며 계산 가능한 비율만 확인
    
    for w in counter:
        # 비율 2:3 (w가 2/3 지점에, 상대가 1 지점에? 아님. w*3 = target*2)
        # target = w * 3 / 2
        if w % 2 == 0 and (w * 3 // 2) in counter:
            answer += counter[w] * counter[w * 3 // 2]
            
        # 비율 2:4 (= 1:2)
        # w * 2 = target * 1 -> target = w * 2
        if (w * 2) in counter:
            answer += counter[w] * counter[w * 2]
            
        # 비율 3:4
        # w * 4 = target * 3 -> target = w * 4 / 3
        if w % 3 == 0 and (w * 4 // 3) in counter:
            answer += counter[w] * counter[w * 4 // 3]
            
    return answer
```

### 코드 설명: `v * (v - 1) // 2`
- **조합(Combination) 공식**: $_nC_2 = \frac{n(n-1)}{2}$
- 같은 몸무게를 가진 사람이 `v`명 있을 때, 이 중 2명을 뽑아 짝을 짓는 경우의 수입니다.
- 예: 100kg인 사람이 `A`, `B`, `C` 3명(`v=3`) 있다면?
  - (A, B), (A, C), (B, C) -> 총 3쌍.
  - 계산: $3 \times (3-1) / 2 = 3$.

### 코드 설명: 다른 몸무게 비율 계산
서로 다른 몸무게 `w`와 `target`(`target > w` 가정)이 균형을 이루는 경우는 다음 3가지 비율입니다. 중복을 피하기 위해 `w`가 더 작은 값일 때, 더 큰 값(`target`)이 존재하는지만 확인하면 됩니다.

1.  **2:3 비율 (w : target)**
    - 위치: `w`는 3m, `target`은 2m 지점. -> $w \times 3 = target \times 2$.
    - `target = w * 3 / 2`.
    - `w`가 2의 배수여야 `target`이 정수가 됩니다. (`if w % 2 == 0`)

2.  **1:2 비율 (w : target)**
    - 위치: `w`는 4m, `target`은 2m 지점. -> $w \times 4 = target \times 2$ -> $w \times 2 = target$.
    - `target = w * 2`.
    - 항상 정수이므로 별도 조건 불필요.

3.  **3:4 비율 (w : target)**
    - 위치: `w`는 4m, `target`은 3m 지점. -> $w \times 4 = target \times 3$.
    - `target = w * 4 / 3`.
    - `w`가 3의 배수여야 합니다. (`if w % 3 == 0`)

**`answer += counter[w] * counter[target]`**:
- 몸무게가 `w`인 사람이 A명, `target`인 사람이 B명 있다면, 이 둘 사이의 짝꿍 조합 수는 $A \times B$입니다. (곱의 법칙)


