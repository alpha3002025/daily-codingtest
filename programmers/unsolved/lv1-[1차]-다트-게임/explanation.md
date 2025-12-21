# [1차] 다트 게임

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/17682)

다트 게임의 점수 계산 로직을 구현하세요.
- 포맷: `점수|보너스|[옵션]` (예: `1S`, `1D*`, `10T#`)
- 점수: 0~10
- 보너스: S(1제곱), D(2제곱), T(3제곱)
- 옵션:
    - `*` (스타상): 해당 점수와 **바로 전에 얻은 점수**를 각각 2배로 만듦.
    - `#` (아차상): 해당 점수를 마이너스함.
    - 옵션은 없을 수도 있음.

## 해결 전략
문자열 파싱과 스택 개념이 혼합된 문제입니다.
1. 문자열을 순회하며 점수, 보너스, 옵션을 분리합니다.
2. 점수를 계산하여 **리스트(스택)**에 넣습니다.
3. 옵션이 나오면 스택의 마지막 값(현재 점수)과 그 앞의 값(이전 점수)을 수정합니다.

### 알고리즘 순서
1. `scores` = []
2. 문자열 `dartResult`를 순회 (또는 정규식 분리):
    - **숫자**: `10`인지 `1`~`9`인지 구분하여 파싱 -> 스택에 변환해서 넣기 전 임시 저장.
    - **보너스(SDT)**: 임시 저장된 숫자를 제곱하여 스택에 push.
        - S: 1제곱, D: 2제곱, T: 3제곱.
    - **옵션(*#)**:
        - `*`: `scores[-1] *= 2`, `if len(scores) > 1: scores[-2] *= 2`
        - `#`: `scores[-1] *= -1`
3. `sum(scores)` 반환.

## Python 코드

```python
import re

def solution(dartResult):
    # 정규식으로 토큰 분리 (점수, 보너스, 옵션)
    # (\d+) : 숫자
    # ([SDT]) : 보너스
    # ([*#]?) : 옵션 (있거나 없거나)
    tokens = re.findall(r'(\d+)([SDT])([*#]?)', dartResult)
    
    scores = []
    
    for score_str, bonus, option in tokens:
        score = int(score_str)
        
        # 보너스 처리
        if bonus == 'D':
            score = score ** 2
        elif bonus == 'T':
            score = score ** 3
            
        scores.append(score)
        
        # 옵션 처리
        if option == '*':
            # 현재 점수 2배
            scores[-1] *= 2
            # 이전 점수도 2배 (존재한다면)
            if len(scores) > 1:
                scores[-2] *= 2
        elif option == '#':
            scores[-1] *= -1
            
    return sum(scores)
```

## 배운 점 / 팁
- **정규식 파싱**: `re.findall`을 사용하여 `(그룹1)(그룹2)(그룹3)` 형태로 패턴을 잡으면 리스트 형태의 튜플 `[('1', 'S', ''), ('2', 'D', '*'), ...]`로 아주 깔끔하게 파싱됩니다. 복잡한 문자열 처리에 강력합니다.
- **Index 관리**: "직전 점수"를 참조해야 하므로 리스트(스택)를 쓰는 것이 배열 인덱스 관리보다 편합니다.
