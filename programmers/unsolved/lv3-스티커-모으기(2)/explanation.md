# 스티커 모으기(2)

## 문제 설명
원형으로 연결된 스티커 뜯기 문제입니다.
스티커를 뜯으면 양옆의 스티커는 찢어져서 못 씁니다.
숫자의 합이 최대가 되도록 스티커를 뜯으세요.

## 문제 해결 전략

**다이나믹 프로그래밍 (DP)**.
원형이므로 두 가지 경우로 나누어 선형 DP를 풉니다.
1. **첫 번째 스티커를 뜯는 경우**: 마지막 스티커는 못 뜯음 (범위: 0 ~ N-2). `dp[0] = sticker[0]`, `dp[1] = sticker[0]`.
2. **첫 번째 스티커를 안 뜯는 경우**: 마지막 스티커 뜯을 수 있음 (범위: 1 ~ N-1). `dp[0] = 0`, `dp[1] = sticker[1]`. (인덱스는 편의상 맞춤)

점화식: `dp[i] = max(dp[i-1], dp[i-2] + sticker[i])` (안 뜯고 이전값 유지 vs 전전꺼 뜯고 이번꺼 뜯기)

## Python 코드

```python
def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]
        
    # Case 1: 첫 번째 뜯음 (마지막 못 씀 -> index 0 ~ len-2)
    dp1 = [0] * len(sticker)
    dp1[0] = sticker[0]
    dp1[1] = sticker[0] # 1번은 못 뜯으므로 0번 값 유지
    
    for i in range(2, len(sticker) - 1): # 마지막 제외
        dp1[i] = max(dp1[i-1], dp1[i-2] + sticker[i])
        
    # Case 2: 첫 번째 안 뜯음 (마지막 쓸 수 있음 -> index 1 ~ len-1)
    dp2 = [0] * len(sticker)
    dp2[0] = 0
    dp2[1] = sticker[1]
    
    for i in range(2, len(sticker)):
        dp2[i] = max(dp2[i-1], dp2[i-2] + sticker[i])
        
    return max(max(dp1), max(dp2))
```
