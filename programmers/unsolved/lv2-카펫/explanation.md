# 카펫

## 문제 설명
중앙에는 노란색 격자가 있고, 테두리 1줄은 갈색 격자로 둘러싸인 카펫이 있습니다.
갈색 격자 수 `brown`, 노란색 격자 수 `yellow`가 주어질 때 카펫의 전체 가로, 세로 크기를 구하세요.
(단, 가로 $\ge$ 세로)

### 핵심 개념
1.  **완전 탐색 (Exhaustive Search)**: 노란색 격자의 가로(`yh`), 세로(`yv`) 길이를 바꾸어가며 조건을 만족하는지 확인합니다.
2.  **약수 (Divisors)**: 노란색 격자는 직사각형 모양이므로 `yellow = yh * yv` 입니다. 즉 `yv`는 `yellow`의 약수입니다.
3.  **검증 공식**: 테두리 갈색 격자의 개수는 `(yh + 2) * (yv + 2) - yellow` 또는 `(yh + yv) * 2 + 4` 입니다.

## Python 풀이

```python
def solution(brown, yellow):
    # 전체 면적 = brown + yellow = W * H
    total = brown + yellow
    
    # H 길이를 3부터 증가시키며 탐색 (최소 높이는 3이어야 yellow가 들어감)
    # 카펫의 세로 길이 H를 기준으로 봅니다.
    for h in range(3, int(total**0.5) + 1):
        if total % h == 0:
            w = total // h
            
            # 카펫의 가로 w, 세로 h 일 때,
            # 내부 yellow의 개수가 (w-2)*(h-2)와 일치하는지 확인
            if (w - 2) * (h - 2) == yellow:
                return [w, h]
                
    # 문제 조건상 반드시 답이 존재함
    return []
```

### 코드 설명
- `total`(전체 격자 수)의 약수 쌍 `(w, h)`를 찾습니다. (`w >= h`)
- 약수 쌍에 대해, 테두리(두께 1)를 제외한 내부 면적이 `yellow`와 같은지 검사합니다.
- `(w-2) * (h-2) == yellow`
