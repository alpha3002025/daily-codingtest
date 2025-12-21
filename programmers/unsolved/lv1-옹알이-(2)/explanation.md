# 옹알이 (2)

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/133499)

아기가 발음할 수 있는 단어는 "aya", "ye", "woo", "ma" 4가지입니다.
이들을 조합해서 만들 수 있는 발음만 할 수 있습니다. 단, **같은 발음을 연속해서 할 수는 없습니다** (예: "yeye" 불가).
주어진 문자열 리스트 `babbling` 중 발음 가능한 단어의 개수를 구하세요.

## 해결 전략
문자열 치환(Replace)을 이용하되, 연속 발음 제약 조건을 체크해야 합니다.
1. 연속된 발음("ayaaya", "yeye" 등)이 포함되어 있다면 즉시 불가능으로 판단.
2. 연속 발음이 없다면, 가능한 4가지 발음을 공백이나 특수문자로 치환하여 지워나갑니다.
3. 최종적으로 문자열이 비어있으면(또는 공백만 남으면) 발음 가능한 것입니다.
    - 주의: 단순히 `""`로 replace하면 "yayae"에서 "aya"를 뺀 뒤 "ye"가 붙어서 발음 가능한 것처럼 오판할 수 있습니다. 따라서 **공백으로 치환(`" "`)** 한 뒤 마지막에 공백을 제거하고 확인해야 합니다.

### 알고리즘 순서
1. `answer` = 0
2. `babbling` 순회 (`word`):
    - "ayaaya", "yeye", "woowoo", "mama" 중 하나라도 있으면 패스.
    - "aya", "ye", "woo", "ma"를 각각 " "(공백)으로 치환. (`replace`)
    - 치환된 결과에서 공백(`" "`)을 모두 제거(`strip` X, `replace(" ", "")` O).
    - 길이가 0이면 `answer += 1`.
3. 반환.

## Python 코드

```python
def solution(babbling):
    answer = 0
    can_speak = ["aya", "ye", "woo", "ma"]
    
    for word in babbling:
        # 1. 연속 발음 체크
        is_consecutive = False
        for sound in can_speak:
            if sound * 2 in word:
                is_consecutive = True
                break
        
        if is_consecutive:
            continue
            
        # 2. 발음 가능한 단어 소거
        for sound in can_speak:
            word = word.replace(sound, " ")
            
        # 3. 남은 문자 확인 (공백 제외하고 아무것도 없어야 함)
        if word.replace(" ", "") == "":
            answer += 1
            
    return answer
```

## 배운 점 / 팁
- **Replace 함정**: 제거 목적으로 `replace`를 쓸 때, 앞뒤 글자가 붙어서 새로운 패턴을 만드는 부작용(Side Effect)을 막기 위해 **임시 문자(공백 등)**로 바꾸는 테크닉이 중요합니다.
- **예외 조건 선처리**: "연속 발음 불가" 같은 조건을 먼저 필터링하면 로직이 단순해집니다.
