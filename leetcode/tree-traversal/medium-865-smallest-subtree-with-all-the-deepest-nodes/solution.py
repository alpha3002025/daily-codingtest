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
                return left_depth + 1, left_lca
            
            # Case 2: 오른쪽이 더 깊은 경우 -> 답은 오른쪽에 있음
            elif right_depth > left_depth:
                return right_depth + 1, right_lca
            
            # Case 3: 깊이가 같은 경우 -> 현재 노드가 LCA
            else:
                # 여기서 left_depth == right_depth 이므로, 둘 중 아무거나 사용해도 같은 값입니다.
                return left_depth + 1, node
        
        # 깊이는 필요 없고 LCA 노드만 반환
        return dfs(root)[1]