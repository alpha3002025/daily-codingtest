# 나누어 떨어지는 숫자 배열

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12910)

`arr`의 요소 중 `divisor`로 나누어 떨어지는 값을 오름차순으로 반환하세요. 없으면 `[-1]`을 반환하세요.

## 해결 전략
필터링 후 정렬.

### 알고리즘 순서
1. `res` = `[x for x in arr if x % divisor == 0]`
2. `res.sort()`
3. return `res` if `res` else `[-1]`

## Python 코드

```python
def solution(arr, divisor):
    result = [x for x in arr if x % divisor == 0]
    
    if not result:
        return [-1]
        
    return sorted(result)
```

## 배운 점 / 팁
- **필터링**: 리스트 컴프리헨션이 가장 깔끔합니다.
