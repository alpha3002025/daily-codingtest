# 1458. Max Dot Product of Two Subsequences

## 문제 설명
두 배열 `nums1`과 `nums2`가 주어졌을 때, 각각의 비어있지 않은 부분 수열(subsequence)을 선택하여 얻을 수 있는 최대 내적(Dot Product)을 구하는 문제입니다.
부분 수열은 원래 배열에서 0개 이상의 원소를 삭제하고 남은 원소들의 순서를 유지하여 만든 배열을 의미합니다.

## 접근 방법 (Dynamic Programming)

이 문제는 두 배열의 부분 수열 간의 매칭을 고려해야 하므로 **LCS (Longest Common Subsequence)** 문제와 유사한 2차원 DP 접근 방식을 사용할 수 있습니다.

### DP 상태 정의
`dp[i][j]`를 `nums1[0...i]`와 `nums2[0...j]`까지 고려했을 때, 각각의 비어있지 않은 부분 수열로 만들 수 있는 **최대 내적**이라고 정의합니다.

### 점화식 (Transition)
`i`번째 원소(`nums1[i]`)와 `j`번째 원소(`nums2[j]`)를 고려할 때, 다음과 같은 선택지들이 있습니다.

1.  **현재 두 원소를 매칭하는 경우**:
    *   두 원소만으로 내적을 구성: `nums1[i] * nums2[j]`
    *   이전까지의 최대 내적에 현재 곱을 추가: `dp[i-1][j-1] + (nums1[i] * nums2[j])`
2.  **현재 원소를 매칭하지 않는 경우**:
    *   `nums1[i]`를 제외하고 이전 상태를 가져옴: `dp[i-1][j]` (코드의 `# 3. nums1[i-1] 스킵`에 해당)
    *   `nums2[j]`를 제외하고 이전 상태를 가져옴: `dp[i][j-1]` (코드의 `# 4. nums2[j-1] 스킵`에 해당)

따라서 점화식은 다음과 같습니다.
`product = nums1[i] * nums2[j]`
`dp[i][j] = max(product, product + dp[i-1][j-1], dp[i-1][j], dp[i][j-1])`

### 초기화 및 주의사항
*   **음수 처리**: 모든 결과가 음수일 수 있습니다. 따라서 DP 테이블을 0으로 초기화하면 안 되고, 매우 작은 값(`-infinity`)으로 초기화해야 합니다.
*   문제 조건에서 "비어있지 않은(non-empty)" 부분 수열을 요구하므로, 최소 하나의 쌍은 선택되어야 합니다. 위 점화식에서 `product` 단독 항이 이를 보장해 줍니다 (이전 값이 음수여서 더하지 않는 것이 이득일 때 새로운 시작점이 됨).

## Python 풀이

```python
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        # DP 테이블을 매우 작은 값으로 초기화
        dp = [[float('-inf')] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                curr_product = nums1[i-1] * nums2[j-1]
                
                dp[i][j] = max(
                    curr_product,                    # 1. 현재 두 수만 선택 (새로운 시작)
                    dp[i-1][j-1] + curr_product,     # 2. 이전 수열에 현재 두 수 추가
                    dp[i-1][j],                      # 3. nums1[i]를 제외(코드의 nums1[i-1])하고 이전 상태를 가져옴
                    dp[i][j-1]                       # 4. nums2[j]를 제외(코드의 nums2[j-1])하고 이전 상태를 가져옴
                )
        
        return dp[n][m]
```
<br/>

### `curr_product`, `dp[i-1][j-1] + curr_product` 모두 max에 포함되는 이유

핵심 이유는 **이전까지의 누적 결과가 음수일 경우, 그것을 버리고 새로 시작하는 것이 더 유리하기 때문**입니다.

`dp[i][j]`를 계산할 때 고려해야 하는 두 가지 중요한 상황이 있습니다.

1.  **`dp[i-1][j-1] + curr_product` (연장하기)**:
    *   이전(`i-1`, `j-1`)까지 만들어놓은 최적의 내적 값에 현재 값(`curr_product`)을 더해서 **수열을 이어가는 경우**입니다.
    *   이전 값이 양수라면 더해서 값을 키우는 것이 유리하므로 이 값을 선택하게 됩니다.

2.  **`curr_product` (새로 시작하기)**:
    *   이전(`i-1`, `j-1`)까지의 최적 결과(`dp[i-1][j-1]`)가 **매우 작은 음수**인 경우입니다.
    *   예를 들어, 이전까지의 결과가 `-100`이고 현재 곱이 `10`이라면:
        *   이어 붙인 값: `-100 + 10 = -90`
        *   새로 시작한 값: `10`
    *   이 경우, 굳이 손해인 과거를 안고 갈 필요 없이 **현재 두 수의 곱부터 새로운 부분 수열을 시작**하는 것이 훨씬 이득입니다.

즉, `max()` 함수 안에 이 두 가지를 모두 포함시킴으로써, **"과거의 값을 이어받는 것이 이득인지"** 아니면 **"과거를 버리고 현재부터 새로 시작하는 것이 이득인지"**를 비교하여 항상 최선의 선택을 하도록 만드는 것입니다.
<br/>
<br/>



## 공간 복잡도 최적화 (선택 사항)
현재 상태 `dp[i][j]`를 구하기 위해 `dp[i-1]`(이전 행)만 필요하므로, 2차원 배열 대신 1차원 배열 두 개(혹은 하나)를 사용하여 공간 복잡도를 `O(N*M)`에서 `O(min(N, M))`으로 줄일 수 있습니다.

```python
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        prev = [float('-inf')] * (m + 1)
        
        for i in range(1, n + 1):
            curr = [float('-inf')] * (m + 1)
            for j in range(1, m + 1):
                product = nums1[i-1] * nums2[j-1]
                curr[j] = max(
                    product,
                    prev[j-1] + product,
                    prev[j],
                    curr[j-1]
                )
            prev = curr
            
        return prev[m]
```

## 복잡도 분석
- **시간 복잡도**: `O(N * M)`. 이중 반복문을 통해 테이블을 채웁니다.
- **공간 복잡도**: `O(N * M)` (2차원 배열 사용 시) 또는 `O(M)` (공간 최적화 시).
