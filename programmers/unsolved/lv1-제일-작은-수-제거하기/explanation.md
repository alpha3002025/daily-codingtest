# 제일 작은 수 제거하기

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12935)

배열 `arr`에서 가장 작은 수를 제거한 배열을 반환하세요.
- 제거 후 빈 배열이 되면 `[-1]`을 반환합니다.
- `arr`은 길이 1 이상입니다.

## 해결 전략
1. `min(arr)`로 최솟값을 찾습니다.
2. `arr.remove(min_val)`로 제거합니다.
3. 빈 배열 체크.

### 알고리즘 순서
1. `if len(arr) <= 1`: return `[-1]`
2. `min_val` = `min(arr)`
3. `arr.remove(min_val)`
4. return `arr`

## Python 코드

```python
def solution(arr):
    if len(arr) <= 1:
        return [-1]
        
    # 최솟값을 찾아 제거 (값 기준 삭제)
    arr.remove(min(arr))
    return arr
```

## 배운 점 / 팁
- **Remove**: `list.remove(x)`는 리스트에서 첫 번째로 나오는 `x`를 삭제합니다. 인덱스를 몰라도 값으로 지울 때 유용합니다.
