# 풍선 터트리기

## 문제 설명
풍선들이 일렬로 있고, 다음 규칙으로 터트려 최후의 1개가 남을 때까지 반복합니다.
1. 인접한 두 풍선 중 하나를 터트립니다.
2. 기본적으로는 **더 큰 풍선**만 터트릴 수 있습니다.
3. 단, **번호가 더 작은 풍선**을 터트리는 행위는 **최대 1번**만 가능합니다.

최후까지 남을 수 있는 풍선의 개수를 구하세요.

## 문제 해결 전략

어떤 풍선 `X`가 살아남으려면?
- `X`를 기준으로 왼쪽 그룹과 오른쪽 그룹이 있습니다.
- "큰 것만 터트리기"는 무제한이므로, 왼쪽 그룹에서 제일 작은 놈(`min_left`) 하나만 남길 수 있습니다. (큰 애들은 다 터트려서 제거 가능)
- 마찬가지로 오른쪽 그룹에서도 제일 작은 놈(`min_right`) 하나만 남길 수 있습니다.
- 이제 `min_left`, `X`, `min_right` 세 개가 남았다고 칩시다. (실제 인접하진 않지만 논리적으로)
- `X`가 살아남으려면:
  - `min_left`나 `min_right` 중 적어도 하나보다는 `X`가 작아야 합니다. (또는 둘 다 없거나)
  - 만약 `min_left < X` 이고 `min_right < X` 라면, `X`는 양쪽보다 큽니다.
    - 왼쪽과 붙을 때 `X`를 살리려면 "작은 거 터트리기(기회 소진)"로 `min_left`를 죽여야 합니다.
    - 그 후 오른쪽 `min_right`와 붙을 때 또 `min_right`가 작으므로 `X`가 죽어야 합니다 (기회 이미 씀).
    - 즉, 양쪽 최솟값이 모두 나보다 작으면 나는 살 수 없습니다.
  - 반대로, 한쪽이라도 나보다 큰 값이 있다면(예: `min_left > X`), "큰 거 터트리기"로 `min_left`를 죽이고, 남은 기회(있다면)로 `min_right`를 처리하거나 살아남을 수 있습니다.

결론: `a[i]`가 살아남으려면 `left_min[i] > a[i]` 또는 `right_min[i] > a[i]` 여야 합니다. (적어도 한 쪽의 최솟값보다는 내가 작아야 함)

## Python 코드

```python
def solution(a):
    if len(a) <= 2:
        return len(a)
    
    n = len(a)
    left_min = [float('inf')] * n
    right_min = [float('inf')] * n
    
    # 왼쪽 최솟값 미리 계산
    m = float('inf')
    for i in range(n):
        if a[i] < m: m = a[i]
        left_min[i] = m
        
    # 오른쪽 최솟값 미리 계산
    m = float('inf')
    for i in range(n - 1, -1, -1):
        if a[i] < m: m = a[i]
        right_min[i] = m
        
    answer = 0
    for i in range(n):
        # 내 왼쪽 전체의 최소, 내 오른쪽 전체의 최소
        # 주의: left_min[i]는 0~i까지의 최소이므로 a[i] 포함함.
        # 문제 조건: "인접한 두 풍선". 내 왼쪽 어딘가에 있는 애들이 다 터지고 최후에 남은 1개.
        # 즉 i-1까지의 최소가 필요함.
        
        l_min = left_min[i-1] if i > 0 else float('inf')
        r_min = right_min[i+1] if i < n - 1 else float('inf')
        
        # 조건: 둘 다 나보다 작으면(나는 둘 다보다 크면) 죽음.
        if a[i] > l_min and a[i] > r_min:
            continue
        else:
            answer += 1
            
    return answer
```
