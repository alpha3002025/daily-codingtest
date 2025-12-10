# LeetCode: Trapping Rain Water (Two Pointer Approach)

## 코드

```python
class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        ans = 0
        left_max, right_max = 0, 0
        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                ans += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                ans += right_max - height[right]
                right -= 1
        return ans
```

## 풀이 설명

이 코드는 **투 포인터(Two Pointers)** 알고리즘을 사용하여 빗물(Trapping Rain Water) 문제를 O(N) 시간 복잡도와 O(1) 공간 복잡도로 해결합니다.

### 핵심 로직

빗물이 고이는 양은 특정 위치를 기준으로 **왼쪽에서 가장 높은 벽(`left_max`)**과 **오른쪽에서 가장 높은 벽(`right_max`)** 중 **더 낮은 쪽**에 의해 결정됩니다.

1.  **초기화**:
    *   `left`, `right` 포인터를 양쪽 끝에 배치합니다.
    *   `left_max`, `right_max`를 0으로 초기화합니다.

2.  **이동 규칙 (`while left < right`)**:
    *   두 포인터가 가리키는 높이를 비교하여 **더 낮은 쪽을 이동**시킵니다.
    *   이유: 낮은 쪽의 벽은 높은 쪽의 벽보다 낮으므로, 물의 높이는 반드시 현재 `left_max`와 `right_max` 중 낮은 쪽에 의해 제한되기 때문입니다.

3.  **상세 동작**:
    *   **`height[left] < height[right]`인 경우**:
        *   오른쪽 어딘가에 현재 왼쪽 벽보다 더 높은 벽이 존재함이 보장됩니다. 따라서 현재 `left` 위치에 고일 수 있는 물은 오직 `left_max`에 의해서만 결정됩니다.
        *   `left_max`를 갱신합니다 (`max(left_max, height[left])`).
        *   현재 위치(`left`)에 고이는 물(`left_max - height[left]`)을 `ans`에 더합니다.
        *   `left`를 오른쪽으로 한 칸 이동합니다.
    *   **그렇지 않은 경우 (`height[left] >= height[right]`)**:
        *   왼쪽 어딘가에 현재 오른쪽 벽보다 더 높거나 같은 벽이 존재함이 보장됩니다. 따라서 `right` 위치의 물은 `right_max`에 의해 결정됩니다.
        *   `right_max`를 갱신합니다.
        *   현재 위치(`right`)에 고이는 물(`right_max - height[right]`)을 `ans`에 더합니다.
        *   `right`를 왼쪽으로 한 칸 이동합니다.

### 복잡도

*   **시간 복잡도**: O(N) - `left`와 `right`가 만나면서 리스트를 한 번만 순회합니다.
*   **공간 복잡도**: O(1) - 별도의 배열(스택이나 메모이제이션 테이블) 없이 변수 몇 개만 사용합니다.
