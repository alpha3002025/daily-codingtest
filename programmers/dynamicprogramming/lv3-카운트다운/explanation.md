# 카운트 다운 (Level 3)

## 문제 설명
프로그래머스 "카운트 다운" 문제는 다트 게임을 소재로 한 동적계획법(Dynamic Programming) 문제입니다.
목표 점수 `target`을 0으로 만드는 데 필요한 최소한의 다트 던지기 횟수와, 그 상황에서 "싱글(Single)" 또는 "불(Bull)"을 최대한 많이 맞힌 횟수를 구해야 합니다.

### 점수 체계
- **싱글 (Single)**: 1 ~ 20점 (보너스 카운트 +1)
- **더블 (Double)**: 2 * (1 ~ 20)점 (보너스 카운트 0)
- **트리플 (Triple)**: 3 * (1 ~ 20)점 (보너스 카운트 0)
- **불 (Bull)**: 50점 (보너스 카운트 +1)

### 우선순위
1. **던진 다트 수 최소화**
2. **("싱글" + "불") 횟수 최대화**

## 해결 방법: 동적계획법 (DP)

목표 점수 `target`이 최대 100,000이므로, O(target)의 시간 복잡도를 가진 DP로 해결할 수 있습니다.

### 점화식 정의
`dp[i]`를 점수 `i`를 만드는 최적의 해 `[던진 횟수, 싱글/불 횟수]`라고 정의합니다.
- 초기 상태: `dp[0] = [0, 0]`
- 목표: `dp[target]` 구하기

점수 `i`에 도달하기 위해, 마지막에 던진 점수를 `p`라고 하면:
`dp[i] = min_condition(dp[i - p] + cost(p))`
여기서 `cost(p)`는 `[1, 1]` (싱글/불인 경우) 또는 `[1, 0]` (그 외)입니다.

단, 비교 연산은 다음과 같이 정의됩니다:
- 던진 횟수가 더 작은 것이 우선.
- 던진 횟수가 같다면, 싱글/불 횟수가 더 큰 것이 우선.

### 구현 상세
한 번에 얻을 수 있는 점수들을 미리 정의해두고, `target`까지 바텀업(Bottom-Up) 방식으로 테이블을 채웁니다.
유효한 점수는 1~20(싱글), 2~40(더블), 3~60(트리플), 50(불) 입니다.
동일한 점수라도 '싱글/불'로 얻을 수 있다면 가산점을 얻으므로, 각 점수별로 얻을 수 있는 최대 보너스를 미리 전처리(Pre-calculation)하여 사용합니다.

## Python 풀이

```python
def solution(target):
    # 각 점수를 얻을 때의 최대 보너스 (싱글/불: 1, 그외: 0) 저장
    # best_moves[score] = bonus
    best_moves = {}
    
    # 1. 더블, 트리플 (보너스 0)
    for i in range(1, 21):
        for mult in [2, 3]:
            score = i * mult
            if score not in best_moves:
                best_moves[score] = 0
                
    # 2. 싱글 (보너스 1) - 덮어쓰기 (우선순위 높음)
    for i in range(1, 21):
        best_moves[i] = 1
        
    # 3. 불 (보너스 1)
    best_moves[50] = 1
    
    # DP 테이블 초기화
    # dp[i] = [던진 횟수, 싱글/불 횟수]
    # 초기값: 던진 횟수 무한대
    dp = [[float('inf'), 0] for _ in range(target + 1)]
    dp[0] = [0, 0]
    
    # DP 수행
    # 1부터 target까지 순회
    for i in range(1, target + 1):
        # 가능한 모든 던지기 점수에 대해
        for score, bonus in best_moves.items():
            if i >= score:
                prev_darts, prev_bonus = dp[i - score]
                
                # 라운드 갱신
                new_darts = prev_darts + 1
                new_bonus = prev_bonus + bonus
                
                # 최적해 갱신 조건
                # 1. 횟수가 더 적으면 갱신
                # 2. 횟수가 같으면 보너스가 더 많으면 갱신
                if new_darts < dp[i][0] or (new_darts == dp[i][0] and new_bonus > dp[i][1]):
                    dp[i] = [new_darts, new_bonus]
                    
    return dp[target]
```

## 복잡도 분석
- **시간 복잡도**: O(Target * K). `target`은 최대 100,000이고, `K`는 한 번에 낼 수 있는 점수의 종류(유니크한 점수 약 40~50개)입니다.
- **공반 복잡도**: O(Target). `dp` 배열의 크기입니다.
