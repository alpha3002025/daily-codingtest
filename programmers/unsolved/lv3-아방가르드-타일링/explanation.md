# 아방가르드 타일링

## 문제 설명
세로 길이가 3, 가로 길이가 `n`인 직사각형 격자를 타일로 채우는 방법을 구합니다.
주어진 타일 종류는:
- 1x2, 2x1 직사각형
- 'L'자 형태 등 다양한 타일이 아니라, 문제 예시를 보면 "정사각형 3개를 붙인 ㄱ자 모양 타일 2종류"가 추가로 주어질 수 있습니다. (정확히 확인 필요, 일반적인 3xn 타일링 문제는 2x1, 1x2만 사용하거나 혹은 추가 타일이 있습니다. 이 문제는 1x2, 2x1과 **세 변의 길이가 1인 ㄴ자 모양 타일**, **세 변의 길이가 1인 ㄱ자 모양 타일**을 사용합니다.) -> 사실 문제는 1x2, 2x1, 1x1 정사각형 3개로 이루어진 트로미노입니다.
- 즉, 2칸 혹은 3칸을 차지하는 타일들을 이용해 3xn을 채웁니다.

## 문제 해결 전략

$N$이 최대 10만입니다. DP $O(N)$으로 해결해야 합니다.
규칙성을 찾아 점화식을 세웁니다.
- 마지막 열을 어떻게 채우느냐에 따라 경우의 수가 나뉩니다.
- $N=3$ 타일링은 복잡한 패턴(특이한 모양)이 주기적으로 등장합니다.
- 점화식: `dp[n] = dp[n-1] * A + dp[n-2] * B + ...` 형태.
  - 길이 1만큼 연장: 직사각형 세우기(1가지) -> `dp[n-1] * 1`
  - 길이 2만큼 연장: 가로 2개 눕히기 등 (총 2가지) -> `dp[n-2] * 2`
  - 길이 3만큼 연장: 특수 모양 (총 5가지) -> `dp[n-3] * 5`
  - 길이 4 이상: 특수 모양들이 추가됨 (2가지, 2가지, 4가지 반복 ... 규칙 확인 필요)

정확한 점화식은 문제 분석을 통해 얻어야 합니다.
알려진 점화식:
$DP[i] = DP[i-1] \times 1 + DP[i-2] \times 2 + DP[i-3] \times 5 + \sum (DP[i-k] \times \text{Unique}_k)$
여기서 Unique 패턴 수는:
$k$가 3의 배수가 아닌 경우(4, 5, 7, 8...): 2가지
$k$가 3의 배수인 경우(6, 9...): 4가지
(단, 4이상에서)

즉:
$DP[i] = DP[i-1] + 2DP[i-2] + 5DP[i-3] + 2DP[i-4] + 2DP[i-5] + 4DP[i-6] + 2DP[i-7] + 2DP[i-8] + 4DP[i-9] \dots$

이 합을 $O(1)$에 구하기 위해 누적 합 배열을 3개 관리합니다.
- `S456[r]`: 나머지가 `r`인 인덱스들의 DP 합. (근데 계수가 2, 2, 4로 반복이므로 별도 처리가 나음)
- 계수가 `2, 2, 4` 반복 패턴이므로, 이를 `2*sum(dp[i-4], dp[i-5], dp[i-7]...) + 2*sum(...)` 처럼 묶습니다.

## Python 코드

```python
def solution(n):
    MOD = 1000000007
    
    dp = [0] * (n + 1)
    
    # Base cases
    dp[0] = 1 
    if n >= 1: dp[1] = 1
    if n >= 2: dp[2] = 3
    if n >= 3: dp[3] = 10
    
    # 누적합 변수들
    # sum_unique[0]: i-4, i-7, i-10 ... (나머지가 i와 다름에 주의)
    # 그냥 인덱스 관점이 아니라, 
    # dp[i] = dp[i-1] + 2*dp[i-2] + 5*dp[i-3] 
    #         + 2*(dp[i-4] + dp[i-5]) + 4*dp[i-6] 
    #         + 2*(dp[i-7] + dp[i-8]) + 4*dp[i-9] ...
    
    # 반복 패턴: (2, 2, 4) 가 i-4부터 시작.
    # 즉 k=4,5,6 -> 2,2,4 / k=7,8,9 -> 2,2,4...
    
    # dp[i] 계산을 위해 필요한 누적합:
    # S[val] : 계수 val을 곱해야 하는 dp값들의 합.
    
    # 하지만 계수가 2, 2, 4 로 바뀜.
    # (dp[i-4] + dp[i-7] + ...) * 2
    # (dp[i-5] + dp[i-8] + ...) * 2
    # (dp[i-6] + dp[i-9] + ...) * 4
    
    # 이렇게 3개 그룹으로 관리하면 됨!
    # group1: i-4, i-7...
    # group2: i-5, i-8...
    # group3: i-6, i-9...
    
    prefix_sum = [0, 0, 0] # 각각 나머지가 0, 1, 2인 인덱스에 대한 합 아님. 현재 i기준 오프셋 합?
    # 아니, 고정 인덱스(Modular 3)별 합을 관리하는게 편함.
    # i % 3 == 0 일 때, 
    #   i-4 (mod 2), i-5 (mod 1), i-6 (mod 0)
    #   i-7 (mod 2), i-8 (mod 1), i-9 (mod 0)
    # 즉, mod 1인 애들은 계수 2, mod 2인 애들은 계수 2, mod 0인 애들은 계수 4.
    
    # 일반화:
    # sum_dp[r] = sum(dp[k]) for k % 3 == r.
    
    sum_dp = [0, 0, 0]
    # 초기값 설정 (i=4부터 루프 돌 때 필요한 값 미리 넣기)
    # i=4일 때, i-4=0 (mod 0) -> 계수 2
    # i-5=-1 (X), i-6=-2 (X) ...
    
    # 루프 안에서 dp[i-4]를 sum_dp[(i-4)%3]에 추가하고 계산하면 됨.
    
    for i in range(4, n + 1):
        # Update prefix sum with dp[i-4] for next terms (2, 2, 4 pattern start from i-4)
        # Actually pattern starts from dist 4.
        
        # Add dp[i-4] to the corresponding accumulator
        # But wait, coefficients depend on distance, not absolute index modulo.
        # terms: 2*dp[i-4] + 2*dp[i-5] + 4*dp[i-6] + ...
        
        # Let's map distance to index:
        # dp[i-4] is used. index k = i-4.
        # if (i - k) % 3 == 1 (dist 4, 7...): coeff 2
        # if (i - k) % 3 == 2 (dist 5, 8...): coeff 2
        # if (i - k) % 3 == 0 (dist 6, 9...): coeff 4
        
        # So we maintain sum_dp[r] = sum of dp[k] where k % 3 == r.
        
        # When calculating dp[i]:
        # We need sum(dp[k] * coeff) for k <= i-4.
        # Coeff depends on (i - k) % 3.
        # If i%3 == 0:
        #   k%3 == 0 => i-k % 3 == 0 => coeff 4
        #   k%3 == 1 => i-k % 3 == 2 => coeff 2
        #   k%3 == 2 => i-k % 3 == 1 => coeff 2
        
        # If i%3 == 1:
        #   k%3 == 0 => i-k % 3 == 1 => coeff 2
        #   k%3 == 1 => i-k % 3 == 0 => coeff 4
        #   k%3 == 2 => i-k % 3 == 2 => coeff 2
        
        # If i%3 == 2:
        #   k%3 == 0 => i-k % 3 == 2 => coeff 2
        #   k%3 == 1 => i-k % 3 == 1 => coeff 2
        #   k%3 == 2 => i-k % 3 == 0 => coeff 4
        
        # Add dp[i-4] to sum_dp
        # 루프 시작 전에 dp[i-4]를 누적합에 반영
        r = (i - 4) % 3
        sum_dp[r] = (sum_dp[r] + dp[i-4]) % MOD
        
        val = dp[i-1] + 2*dp[i-2] + 5*dp[i-3]
        
        if i % 3 == 0:
            val += 4*sum_dp[0] + 2*sum_dp[1] + 2*sum_dp[2]
        elif i % 3 == 1:
            val += 2*sum_dp[0] + 4*sum_dp[1] + 2*sum_dp[2]
        else: # i % 3 == 2
            val += 2*sum_dp[0] + 2*sum_dp[1] + 4*sum_dp[2]
            
        dp[i] = val % MOD
        
    return dp[n]
```
