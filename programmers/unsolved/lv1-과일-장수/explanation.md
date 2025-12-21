# 과일 장수

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/135808)

사과 점수 `score`가 주어질 때, 한 상자에 `m`개씩 담아 포장합니다.
- 상자 가격 = (상자 내 최저 점수) x `m`
가능한 최대 이익을 구하세요. (남는 사과는 버림)

## 해결 전략
상자의 최저 점수가 높을수록 이득이므로, **점수가 높은 사과끼리 묶어야** 합니다.
1. `score`를 내림차순 정렬합니다. `[k, k, ..., 1]`
2. 앞에서부터 `m`개씩 자르면, 각 그룹의 '마지막' 원소가 그 상자의 최저 점수가 됩니다.
3. 이들을 모두 더해 계산합니다.

### 알고리즘 순서
1. `score` 정렬 (내림차순).
2. `answer` = 0.
3. `len(score) // m` 만큼 반복:
    - `group_idx = (i + 1) * m - 1` (각 상자의 마지막 사과 인덱스)
    - `min_score = score[group_idx]`
    - `answer += min_score * m`
4. 반환.
- 또는 슬라이싱으로 `score[m-1 :: m]` 요소들을 합산해도 됩니다.

## Python 코드

```python
def solution(k, m, score):
    # 내림차순 정렬
    score.sort(reverse=True)
    
    answer = 0
    # m개씩 묶었을 때 각 그룹의 최저 점수는 m-1, 2m-1, ... 인덱스에 위치함
    # 슬라이싱으로 최저 점수들만 추출하여 합산
    box_min_scores = score[m-1 : : m]
    
    answer = sum(box_min_scores) * m
            
    return answer
```

## 배운 점 / 팁
- **그리디 & 정렬**: 자원을 효율적으로 묶어야 할 때 정렬 후 순차 처리하는 전형적인 방법입니다.
- **슬라이싱 스텝**: `list[start::step]`을 활용하면 반복문 없이 특정 위치의 원소들을 쏙쏙 뽑아낼 수 있어 매우 파이썬스럽고 빠릅니다.
