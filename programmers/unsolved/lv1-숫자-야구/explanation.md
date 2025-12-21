# 숫자 야구

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/451808)

숫자 야구 게임은 1~9까지의 서로 다른 숫자 4개로 이루어진 비밀번호를 맞히는 게임입니다.
주어진 `n`회 이내에 `submit` 함수를 사용하여 올바른 비밀번호를 반환해야 합니다.

`submit` 함수는 4자리 정수를 인자로 받아 스트라이크(S)와 볼(B)의 개수를 "xS yB" 형태의 문자열로 반환합니다.

## 해결 전략
이 문제는 **제약 충족 문제(Constraint Satisfaction Problem)**로 볼 수 있습니다.
가능한 모든 비밀번호 후보(1~9의 서로 다른 숫자 4개, 총 3024개) 중에서, 지금까지 얻은 힌트(S, B 결과)와 모순되지 않는 후보들만 남겨가며 정답을 좁혀나가는 방식이 유효합니다.

특히 `n`이 6으로 매우 작은 경우도 있으므로, 단순히 남은 후보 중 아무거나 선택하기보다 **가장 정보를 많이 얻을 수 있는(남은 후보를 가장 많이 줄일 수 있는)** 수를 선택하는 전략(Minimax 등)이 필요할 수 있습니다. 하지만, 후보가 충분히 줄어든 상태에서는 단순히 남은 후보 중 첫 번째를 선택해도 대부분 5~6회 이내에 정답을 찾을 수 있습니다.

### 알고리즘 순서
1. **초기화**: 1~9로 만들 수 있는 모든 4자리 순열(3,024개)을 후보군(`pool`)으로 생성합니다.
2. **첫 추측**: 정보 획득 효율이 좋은 "1234"로 시작합니다.
3. **반복**:
    - 현재 `guess`를 `submit`합니다.
    - 결과가 "4S 0B"라면 정답이므로 반환합니다.
    - 결과(S, B)를 바탕으로, `pool`에 있는 후보들 중 **만약 그 후보가 정답이었다면 같은 결과(S, B)를 냈을 후보**만 남기고 나머지는 제거합니다.
    - `pool`이 줄어들면, 다음 `guess`를 선택합니다.
        - `pool`의 크기가 작을 때(예: 500개 미만)는 최적의 수를 계산할 수도 있지만, 시간 복잡도를 고려하여 단순히 첫 번째 후보를 선택해도 통과 가능한 경우가 많습니다. (여기서는 간단히 첫 번째 후보를 선택하는 방식을 사용하거나, 필요시 엔트로피/Minimax 전략을 추가할 수 있습니다.)

## Python 코드

```python
from itertools import permutations

def get_score(secret, guess):
    """
    secret과 guess(문자열)를 비교하여 (strike, ball)을 반환
    """
    s = 0
    b = 0
    for i in range(4):
        if guess[i] == secret[i]:
            s += 1
        elif guess[i] in secret:
            b += 1
    return s, b

def solution(n, submit):
    # 1. 모든 가능한 후보 생성 (1~9, 서로 다른 4자리)
    digits = '123456789'
    pool = [''.join(p) for p in permutations(digits, 4)]
    
    # 첫 추측은 일반적으로 1234가 무난함
    guess = "1234"
    
    while True:
        # 2. 제출 및 결과 확인
        res_str = submit(int(guess))
        
        # 정답인 경우
        if res_str == "4S 0B":
            return int(guess)
        
        # 결과 파싱 "xS yB"
        s_part, b_part = res_str.split()
        s = int(s_part[:-1])
        b = int(b_part[:-1])
        
        # 3. 후보 필터링
        new_pool = []
        for candidate in pool:
            # candidate가 정답이라고 가정했을 때, 
            # 우리가 낸 guess와의 점수가 실제 얻은 점수(s, b)와 같아야 함
            if get_score(candidate, guess) == (s, b):
                new_pool.append(candidate)
        
        pool = new_pool
        
        if not pool:
            break
            
        # 4. 다음 추측 선택
        # 남은 후보 중 첫 번째를 선택 (Consistent Guess)
        # 만약 n이 매우 작아 최적화가 필요하다면 Minimax 전략을 사용할 수 있으나,
        # 대부분의 경우 남은 후보 중 하나를 선택하면 수렴함.
        guess = pool[0]
        
        # (심화) Minimax 전략 예시:
        # if len(pool) <= 1:
        #     guess = pool[0]
        # else:
        #     # 다음 guess로 pool을 가장 잘게 쪼개는(최악의 경우 남은 pool이 최소가 되는) 후보 선정
        #     pass 
            
    return int(guess)
```

## 배운 점 / 팁
- **완전 탐색(Brute Force)**과 **가지치기(Pruning)**: 초기 탐색 공간은 크지 않으므로($9P4 = 3024$), 매 단계마다 불가능한 후보를 제거(Pruning)해나가는 방식으로 효율적인 해결이 가능합니다.
- **문자열 처리**: 숫자 야구에서 자릿수별 비교를 위해 숫자를 문자열로 다루는 것이 편리합니다.
- `itertools.permutations`: 순열을 생성할 때 매우 유용한 표준 라이브러리입니다.
