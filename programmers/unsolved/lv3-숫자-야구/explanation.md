# 프로그래머스 Lv3 숫자 야구 - Python 풀이

## 문제 설명
숫자 야구 게임은 1부터 9까지의 서로 다른 숫자 4개로 이루어진 비밀번호를 맞추는 게임입니다.
정해진 횟수(`n`) 내에 질문(`submit`)을 던져서 반환되는 볼(B), 스트라이크(S) 판정 결과를 통해 후보군을 좁혀나가 비밀번호를 찾아야 합니다.

- **비밀번호(Secret)**: 1~9 사이의 서로 다른 숫자 4개 (예: 1357)
- **제출(Submit)**: 1000~9999 사이의 정수 제출
- **결과(Result)**: "xS yB" 형태의 문자열 (예: "1S 2B")

## 풀이 전략: 완전 탐색 및 가지치기 (Pruning)

가능한 비밀번호의 전체 경우의 수는 1부터 9까지의 숫자 중 4개를 순서를 고려하여 뽑는 순열(Permutation)과 같습니다.

- 전체 후보군 크기: $P(9, 4) = 9 \times 8 \times 7 \times 6 = 3,024$개

3,024개는 컴퓨터가 처리하기에 매우 작은 수이므로, 가능한 모든 후보를 생성해두고 매 질문마다 불가능한 후보를 제거(Filtering)하는 방식으로 해결할 수 있습니다.

### 알고리즘 순서
1. **후보군 초기화**: 1~9의 숫자로 만들 수 있는 4자리 순열 3,024개를 모두 생성하여 `candidates` 리스트에 저장합니다.
2. **반복 (While Loop)**:
    - 후보군 중 하나를 선택하여 질문(`submit`)을 던집니다. (가장 첫 번째 후보를 선택해도 무방합니다)
    - 결과(`strike`, `ball`)를 받습니다.
    - 만약 `4S 0B`라면 정답이므로 해당 숫자를 반환하고 종료합니다.
    - 현재 후보군에 남아있는 모든 숫자들에 대해, **"만약 이 숫자가 정답이라면, 방금 던진 질문에 대해 같은 결과(S, B)가 나오는가?"**를 검사합니다.
    - 조건을 만족하지 않는(결과가 모순되는) 후보들을 모두 제거합니다.
3. 정답을 찾을 때까지 반복합니다.

이 방식은 평균적으로 5~6회 내외의 시도로 정답을 찾아낼 수 있어, 문제의 제한 횟수(`n` >= 10)를 충분히 만족합니다.

## Python 코드

```python
from itertools import permutations

def solution(n, submit):
    # 1. 1~9까지의 숫자로 구성된 모든 4자리 순열 생성 (총 3024개)
    nums = [str(i) for i in range(1, 10)]
    candidates = list(permutations(nums, 4))
    
    # 점수 계산 헬퍼 함수
    # secret: 정답이라고 가정한 후보 (tuple)
    # guess: 실제 던진 질문 (tuple)
    def calculate_score(secret, guess):
        strikes = 0
        balls = 0
        for i in range(4):
            if secret[i] == guess[i]:
                strikes += 1
            elif guess[i] in secret:
                balls += 1
        return strikes, balls

    while candidates:
        # 후보군 중 하나를 선택 (첫 번째 후보 사용)
        guess_tuple = candidates[0]
        guess_val = int("".join(guess_tuple))
        
        # 질문 던지기 (submit 함수 호출)
        result_str = submit(guess_val)
        
        # 결과 파싱 "xS yB" -> x, y 정수 변환
        # 예: "1S 2B" -> s=1, b=2
        s_part, b_part = result_str.split()
        real_s = int(s_part.replace('S', ''))
        real_b = int(b_part.replace('B', ''))
        
        # 정답인 경우 반환
        if real_s == 4:
            return guess_val
        
        # 가지치기 (Pruning)
        # 현재 질문(guess_tuple)에 대해, 실제 결과(real_s, real_b)와 
        # 동일한 결과를 내는 후보만 남깁니다.
        next_candidates = []
        for cand in candidates:
            # 자기 자신은 제외 (이미 오답임이 판명됨)
            if cand == guess_tuple:
                continue
                
            # cand가 정답이라면 guess_tuple을 질문했을 때 어떤 결과가 나올까?
            temp_s, temp_b = calculate_score(cand, guess_tuple)
            
            # 실제 결과와 일치하는 후보만 유지
            if temp_s == real_s and temp_b == real_b:
                next_candidates.append(cand)
        
        candidates = next_candidates
        
    return 0 # 도달하지 않음
```

## 코드 설명
1.  `itertools.permutations`를 사용하여 `('1', '2', '3', '4')` 형태의 튜플 리스트를 생성합니다.
2.  `candidates[0]`을 선택하여 `int`로 변환 후 `submit` 합니다.
3.  반환된 문자열을 파싱하여 스트라이크와 볼 개수를 얻습니다.
4.  유효성 검사를 위해 이중 for문 대신, 모든 후보에 대해 `calculate_score`를 수행하고 결과가 일치하지 않는 후보를 `next_candidates`에서 제외합니다.
5.  이 과정을 정답(`4S 0B`)이 나올 때까지 반복합니다.
