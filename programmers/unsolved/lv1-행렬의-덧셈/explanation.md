# 행렬의 덧셈

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12950)

행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과를 구하세요.

## 해결 전략
이중 반복문이나 `zip`을 활용하여 같은 위치의 요소끼리 더합니다.
리스트 컴프리헨션을 중첩하여 한 줄로 작성할 수도 있습니다.

### 알고리즘 순서
1. `answer` = `[[c1 + c2 for c1, c2 in zip(r1, r2)] for r1, r2 in zip(arr1, arr2)]`
2. 반환.

## Python 코드

```python
def solution(arr1, arr2):
    # 중첩 리스트 컴프리헨션 + zip
    # 바깥 zip: 각 행(row)끼리 묶음
    # 안쪽 zip: 각 행의 원소(col)끼리 묶음
    answer = [[c + d for c, d in zip(row1, row2)] for row1, row2 in zip(arr1, arr2)]
    return answer
```

## 배운 점 / 팁
- **Numpy**: 실제로는 `numpy`를 쓰면 `arr1 + arr2`로 끝이지만, 코딩테스트에서는 라이브러리 제한이 있을 수 있으므로 리스트 연산을 익혀야 합니다.
