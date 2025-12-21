# K번째수

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/42748)

배열 `array`의 `i`번째 숫자부터 `j`번째 숫자까지 자르고 정렬했을 때, `k`번째에 있는 수를 구하세요.
`commands` 배열(`[i, j, k]`)이 여러 개 주어질 때 결과를 배열로 반환하세요.

## 해결 전략
파이썬의 리스트 슬라이싱과 정렬 기능을 그대로 사용하면 됩니다.
- 문제의 인덱스는 1-based이므로, 파이썬의 0-based 인덱스로 변환할 때 `-1`을 잘 적용해야 합니다.
- `i`번째 ~ `j`번째 -> `array[i-1 : j]`

### 알고리즘 순서
1. `answer` = []
2. `commands` 순회 (`i`, `j`, `k`):
    - `cut` = `array[i-1 : j]`
    - `cut.sort()`
    - `answer.append(cut[k-1])`
3. 반환.

## Python 코드

```python
def solution(array, commands):
    answer = []
    
    for i, j, k in commands:
        # i번째 ~ j번째 슬라이싱 (인덱스는 i-1 ~ j)
        cut_arr = array[i-1 : j]
        
        # 정렬
        cut_arr.sort()
        
        # k번째 숫자 선택 (인덱스는 k-1)
        answer.append(cut_arr[k-1])
        
    return answer
```

## 배운 점 / 팁
- **슬라이싱 범위**: `[start : end]`에서 `end`는 **포함되지 않음(exclusive)**을 유의해야 합니다. 문제의 "j번째까지"는 인덱스 `j` 앞까지가 아니라 `j`번 요소까지이므로, 슬라이싱 끝 인덱스를 `j`로 잡아야 `j-1`번 인덱스까지 포함됩니다.
