# 성격 유형 검사하기

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/118666)

MBTI처럼 4가지 지표(`RT`, `CF`, `JM`, `AN`)로 성격을 분류합니다.
`survey` 질문(예: "TR")과 사용자의 선택(`choices`, 1~7)에 따라 점수를 매기고, 최종 성격 유형 문자열을 반환합니다.
- 점수가 같으면 사전 순으로 빠른 유형을 선택합니다.
- 1(매우 비동의) ~ 7(매우 동의)
- "TR", 1점 -> T형 3점 획득.

## 해결 전략
각 유형별(R, T, C, F, J, M, A, N) 점수를 저장할 딕셔너리를 만듭니다.
`survey`와 `choices`를 순회하며 점수를 누적합니다.
- 선택지 4(모르겠음) 기준:
    - 1~3: 앞 글자 유형 점수 획득 (3, 2, 1점)
    - 5~7: 뒷 글자 유형 점수 획득 (1, 2, 3점)
    - 4: 점수 없음

최종적으로 4개 지표를 순서대로 비교하여 결과 문자열을 조합합니다.

### 알고리즘 순서
1. `scores` = `{"R":0, "T":0, ...}` 초기화.
2. `zip(survey, choices)` 순회:
    - `type1, type2 = surv[0], surv[1]`
    - `score = choice - 4`
    - `score < 0`: `scores[type1] += abs(score)`
    - `score > 0`: `scores[type2] += score`
3. 지표별 비교:
    - 1: `R` vs `T` (점수 같거나 R이 크면 R, 아니면 T)
    - 2: `C` vs `F`
    - ...
4. 반환.

## Python 코드

```python
def solution(survey, choices):
    # 성격 유형 점수 테이블
    scores = {c: 0 for c in "RTCFJMAN"}
    
    # 지표 정의
    indicators = [("R", "T"), ("C", "F"), ("J", "M"), ("A", "N")]
    
    for s, choice in zip(survey, choices):
        # 1~3: 비동의(앞글자), 5~7: 동의(뒷글자)
        # 4를 빼면: -3, -2, -1, 0, 1, 2, 3
        
        val = choice - 4
        
        if val < 0:
            # 음수면 앞 글자가 점수 획득 (절댓값)
            scores[s[0]] += abs(val)
        elif val > 0:
            # 양수면 뒷 글자가 점수 획득
            scores[s[1]] += val
            
    result = ""
    for t1, t2 in indicators:
        # 점수가 같거나 t1이 더 크면 t1 (사전순 빠른게 t1이므로)
        if scores[t1] >= scores[t2]:
            result += t1
        else:
            result += t2
            
    return result
```

## 배운 점 / 팁
- **점수 매핑**: `choice - 4` 연산을 통해 1~7 범위를 -3~3으로 변환하면, 부호에 따라 앞/뒤 유형을 바로 결정할 수 있어 직관적입니다.
- **사전 순 조건**: 문제의 "점수가 같으면 사전 순으로 빠른 것" 조건은 지표 정의(`RT` 등)에서 이미 알파벳 순으로 배치(`R` < `T`)해두었으므로 `>=` 조건만으로 처리 가능합니다.
