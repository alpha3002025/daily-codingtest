# 추억 점수

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/176963)

사진 속에 등장하는 인물들의 그리움 점수를 합산하여 사진의 추억 점수를 구합니다.
- `name`: 그리워하는 사람의 이름 목록
- `yearning`: 각 사람의 그리움 점수 (name과 순서 일치)
- `photo`: 각 사진에 찍힌 인물들의 이름 리스트 (2차원 배열)

그리움 점수 목록에 없는 사람은 0점으로 처리합니다.

## 해결 전략
아주 간단한 매핑 및 합산 문제입니다.
`name`과 `yearning`이 별도의 리스트로 주어지므로, 이를 **딕셔너리(`name` -> `score`)** 형태로 묶어두면 조회가 매우 간편해집니다.

1. **매핑**: `zip`을 사용하여 `{이름: 점수}` 딕셔너리를 만듭니다.
2. **합산**: 각 사진(`photo[i]`)에 대해 등장하는 인물들의 점수를 더합니다. 딕셔너리에 없는 이름은 `get(name, 0)`으로 처리하여 0을 더합니다.

### 알고리즘 순서
1. `score_map` = `{n: y for n, y in zip(name, yearning)}`
2. `result` 리스트 생성.
3. `photo`의 각 리스트 `p`에 대해:
    - `current_score` = `sum(score_map.get(person, 0) for person in p)`
    - `result.append(current_score)`
4. `result` 반환.

## Python 코드

```python
def solution(name, yearning, photo):
    # 이름과 점수를 매핑하여 딕셔너리 생성
    score_map = dict(zip(name, yearning))
    
    answer = []
    
    for p in photo:
        total = 0
        for person in p:
            # 딕셔너리에 있으면 점수 더하고, 없으면 0 더함
            total += score_map.get(person, 0)
        answer.append(total)
        
    return answer
```

## 배운 점 / 팁
- **`zip` 함수**: 두 개의 리스트를 묶어서 처리할 때 매우 유용합니다.
- **딕셔너리 `.get()`**: 키가 존재하지 않을 때 기본값(default value)을 반환하게 하여 `if-else` 없이 깔끔한 코드를 작성할 수 있습니다.
