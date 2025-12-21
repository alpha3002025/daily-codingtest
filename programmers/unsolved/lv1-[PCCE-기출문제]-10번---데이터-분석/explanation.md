# [PCCE 기출문제] 10번 / 데이터 분석

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/250121)

데이터 목록 `data`가 주어집니다. 각 데이터는 `[code, date, maximum, remain]` 형태입니다.
주어진 조건(`ext`, `val_ext`)에 맞는 데이터를 필터링한 후, 정렬 기준(`sort_by`)에 따라 오름차순 정렬하여 반환하세요.

- `ext`: 필터링 기준 컬럼 이름 ("code", "date", "maximum", "remain")
- `val_ext`: 필터링 기준 값 (이 값보다 **작은** 데이터만 선택)
- `sort_by`: 정렬 기준 컬럼 이름

## 해결 전략
문자열로 주어지는 컬럼 이름(`"code"`, `"date"` 등)을 실제 데이터의 인덱스(`0`, `1`...)로 매핑하여 처리하는 것이 핵심입니다.

1. **컬럼 매핑**: 각 문자열이 몇 번째 인덱스인지를 저장하는 딕셔너리를 만듭니다.
    - `col_map = {"code": 0, "date": 1, "maximum": 2, "remain": 3}`
2. **필터링**: 리스트 컴프리헨션(List Comprehension)을 사용하여 `data`에서 `ext` 컬럼 값이 `val_ext`보다 작은 항목만 추출합니다.
3. **정렬**: 추출된 리스트를 `sort_by` 컬럼 값을 기준으로 오름차순 정렬합니다. 파이썬의 `sort(key=...)` 또는 `sorted()`를 활용합니다.

### 알고리즘 순서
1. 컬럼명 -> 인덱스 맵 생성.
2. `ext_idx`, `sort_idx` 찾기.
3. `filtered_data` 생성: `[row for row in data if row[ext_idx] < val_ext]`
4. `filtered_data` 정렬: `sort(key=lambda x: x[sort_idx])`
5. 반환.

## Python 코드

```python
def solution(data, ext, val_ext, sort_by):
    # 컬럼 이름과 인덱스 매핑
    col_idx = {
        "code": 0,
        "date": 1,
        "maximum": 2,
        "remain": 3
    }
    
    criterion_idx = col_idx[ext]
    sort_criterion_idx = col_idx[sort_by]
    
    # 1. 조건에 맞는 데이터 필터링 (val_ext보다 작은 값)
    filtered_data = [item for item in data if item[criterion_idx] < val_ext]
    
    # 2. 정렬 기준에 따라 오름차순 정렬
    filtered_data.sort(key=lambda x: x[sort_criterion_idx])
    
    return filtered_data
```

## 배운 점 / 팁
- **Dictionary Look-up**: 문자열 형태의 키를 코드상의 로직에 필요한 값(인덱스)으로 변환할 때 딕셔너리가 가장 깔끔한 방법입니다.
- **lambda 함수와 정렬**: `sort` 함수의 `key` 인자에 `lambda`를 사용하여 특정 인덱스를 기준으로 정렬하는 방법은 매우 자주 사용되므로 숙달해야 합니다.
