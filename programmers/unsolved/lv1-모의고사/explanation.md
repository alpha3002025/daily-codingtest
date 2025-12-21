# 모의고사

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/42840)

수포자 3명이 문제를 찍습니다.
1. `1, 2, 3, 4, 5` 반복
2. `2, 1, 2, 3, 2, 4, 2, 5` 반복
3. `3, 3, 1, 1, 2, 2, 4, 4, 5, 5` 반복
정답(`answers`)이 주어질 때 가장 많이 맞힌 사람(들)을 오름차순으로 반환하세요.

## 해결 전략
단순 구현(Simulation) 문제입니다.
각 수포자의 패턴을 리스트로 정의하고, 정답 배열을 순회하며 비교합니다.
패턴 길이가 다르므로 모듈러 연산(`%`)으로 인덱스를 순환시킵니다.

### 알고리즘 순서
1. `pat1` = `[1,2,3,4,5]`, `pat2` = `[2,1,2,3,2,4,2,5]`, `pat3` = `[3,3,1,1,2,2,4,4,5,5]`
2. `score` = `[0, 0, 0]`
3. `answers` 순회 (`i`, `ans`):
    - `if ans == pat1[i % len(pat1)]`: `score[0] += 1`
    - `if ans == pat2[i % len(pat2)]`: `score[1] += 1`
    - `if ans == pat3[i % len(pat3)]`: `score[2] += 1`
4. `max_score` = `max(score)`
5. `result` = `[idx+1 for idx, s in enumerate(score) if s == max_score]`
6. 반환.

## Python 코드

```python
def solution(answers):
    # 수포자들의 찍기 패턴
    pat1 = [1, 2, 3, 4, 5]
    pat2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pat3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    scores = [0, 0, 0]
    
    for i, ans in enumerate(answers):
        # 패턴의 길이로 나눈 나머지 인덱스와 비교
        if ans == pat1[i % 5]:
            scores[0] += 1
        if ans == pat2[i % 8]:
            scores[1] += 1
        if ans == pat3[i % 10]:
            scores[2] += 1
            
    max_score = max(scores)
    
    result = []
    for i, score in enumerate(scores):
        if score == max_score:
            result.append(i + 1)
            
    return result
```

## 배운 점 / 팁
- **모듈러 연산**: 반복되는 패턴(Cycle)을 처리할 때 인덱스 접근용으로 필수적인 테크닉입니다.
- **Enumerate**: 인덱스와 값을 동시에 필요로 할 때 유용합니다.
