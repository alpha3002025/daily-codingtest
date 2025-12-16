# N개의 최소공배수

## 문제 설명
$N$개의 숫자가 담긴 배열 `arr`이 주어질 때, 이 수들의 최소공배수(LCM)를 구하는 문제입니다.

### 핵심 개념
1.  **최대공약수(GCD)와 최소공배수(LCM)**:
    - 두 수 $A, B$의 $LCM(A, B) = \frac{A \times B}{GCD(A, B)}$
2.  **누적 연산**:
    - N개의 수에 대한 LCM은 앞에서부터 두 개씩 순차적으로 구하면 됩니다.
    - $LCM(A, B, C) = LCM(LCM(A, B), C)$

## Python 풀이

```python
import math

def solution(arr):
    # 첫 번째 수로 초기화
    answer = arr[0]
    
    # 두 번째 수부터 순차적으로 LCM 갱신
    for num in arr[1:]:
        # answer와 num의 최소공배수 구하기
        # LCM = (A * B) // GCD(A, B)
        answer = (answer * num) // math.gcd(answer, num)
        
    return answer
```

### 코드 설명
- `math.gcd` 함수를 이용해 효율적으로 최대공약수를 구합니다.
- 배열의 크기가 작으므로(15개 이하) 순차적으로 계산해도 충분합니다.
