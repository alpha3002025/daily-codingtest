# 865. Smallest Subtree with all the Deepest Nodes

## 문제 설명
이진 트리(Binary Tree)가 주어졌을 때, **가장 깊은 노드들(Deepest Nodes)을 모두 포함하는 가장 작은 서브트리(Smallest Subtree)**의 루트를 찾는 문제입니다.

다르게 말하면, 트리의 최대 깊이에 위치한 모든 노드들의 **최소 공통 조상(LCA, Lowest Common Ancestor)**을 찾는 것과 같습니다.

## 접근 방법 (DFS & Recursion)

이 문제는 트리 순회(Traversal)를 통해 해결할 수 있습니다. 각 노드에서 두 가지 정보를 부모에게 반환하는 **Bottom-up DFS** 방식을 사용하면 효율적입니다.

### 핵심 아이디어
각 노드를 방문할 때마다 다음 정보를 반환합니다:
1.  **해당 서브트리의 높이(깊이)**
2.  **해당 서브트리에서 가장 깊은 노드들의 공통 조상(LCA)**

### 로직
현재 노드(`node`)에서 왼쪽 자식과 오른쪽 자식에 대해 재귀적으로 함수를 호출하여 `(높이, LCA)`를 얻습니다.

1.  `left_depth`와 `left_lca` (왼쪽 서브트리 결과)
2.  `right_depth`와 `right_lca` (오른쪽 서브트리 결과)

이제 두 자식의 깊이를 비교하여 현재 노드가 반환할 값을 결정합니다.

*   **Case 1: `left_depth > right_depth`**
    *   왼쪽 서브트리가 더 깊습니다. 즉, 전체 트리에서 가장 깊은 노드들은 왼쪽에만 존재합니다.
    *   따라서 답은 왼쪽에서 찾은 `left_lca`가 되며, 현재 높이는 `left_depth + 1`입니다.
*   **Case 2: `right_depth > left_depth`**
    *   오른쪽 서브트리가 더 깊습니다.
    *   답은 오른쪽에서 찾은 `right_lca`가 되며, 현재 높이는 `right_depth + 1`입니다.
*   **Case 3: `left_depth == right_depth`**
    *   왼쪽과 오른쪽의 깊이가 같습니다. 즉, 가장 깊은 노드들이 양쪽에 흩어져 있다는 뜻입니다.
    *   따라서, **현재 노드(`node`)**가 이 노드들을 아우르는 가장 작은(가장 낮은) 공통 조상이 됩니다.
    *   반환값은 `(node, left_depth + 1)` 입니다.

## Python 풀이

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        # 반환값: (서브트리의 높이, 그 서브트리의 가장 깊은 노드들의 LCA)
        def dfs(node):
            if not node:
                # Base Case: 노드가 존재하지 않음 (None)
                # 0: 비어있는 트리의 높이(깊이)는 0
                # None: 비어있는 트리이므로 LCA 노드도 없음
                return 0, None
            
            left_depth, left_lca = dfs(node.left)
            right_depth, right_lca = dfs(node.right)
            
            # Case 1: 왼쪽이 더 깊은 경우 -> 답은 왼쪽에 있음
            if left_depth > right_depth:
                # 자식 노드로부터 받은 깊이(left_depth)에 현재 노드의 높이 1칸을 더해서 부모에게 보고합니다.
                # LCA는 이미 왼쪽 자식 쪽에서 결정된 값(left_lca)을 그대로 올립니다.
                return left_depth + 1, left_lca
            
            # Case 2: 오른쪽이 더 깊은 경우 -> 답은 오른쪽에 있음
            elif right_depth > left_depth:
                # 자식 노드로부터 받은 깊이(right_depth)에 현재 노드의 높이 1칸을 더해서 부모에게 보고합니다.
                # LCA는 이미 오른쪽 자식 쪽에서 결정된 값(right_lca)을 그대로 올립니다.
                return right_depth + 1, right_lca
            
            # Case 3: 깊이가 같은 경우 -> 현재 노드가 LCA
            else:
                # 여기서 left_depth == right_depth 이므로, 둘 중 아무거나 사용해도 같은 값입니다.
                return left_depth + 1, node
        
        # 깊이는 필요 없고 LCA 노드만 반환
        return dfs(root)[1]
```

## 복잡도 분석
- **시간 복잡도**: `O(N)`. 모든 노드를 한 번씩 방문하므로 트리의 노드 수 N에 비례합니다.
- **공간 복잡도**: `O(H)`. 재귀 호출 스택의 깊이는 트리의 높이 H에 비례합니다. (Worst case: 편향 트리일 때 O(N))

## 참고 사항
이 문제는 LeetCode 1123번 "Lowest Common Ancestor of Deepest Leaves"와 완전히 동일한 문제입니다.
