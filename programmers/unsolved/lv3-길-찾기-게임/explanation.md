# 길 찾기 게임

## 문제 설명
`nodeinfo`에 각 노드의 `(x, y)` 좌표가 주어집니다.
이진 트리를 구성해야 합니다.
- y값이 클수록 레벨이 높습니다 (루트가 가장 위).
- 같은 레벨(y)이면 x값으로 왼쪽/오른쪽 구분하지 않습니다 (부모의 x보다 작으면 왼쪽 서브트리, 크면 오른쪽 서브트리).
전위 순회(Preorder)와 후위 순회(Postorder) 결과를 반환하세요.

## 문제 해결 전략

1. **정렬**: 레벨(y) 내림차순, x 오름차순으로 노드를 정렬합니다.
   - 첫 번째 노드가 루트입니다.
2. **트리 구성**:
   - 루트부터 시작해서 다음 노드들을 하나씩 삽입합니다.
   - 삽입하려는 노드의 x가 현재 노드의 x보다 작으면 왼쪽, 크면 오른쪽으로 보냅니다.
   - 빈 자리가 나오면 거기에 노드를 붙입니다.
   - 재귀적으로 구현합니다.
3. **순회**:
   - 구성된 트리로 preorder, postorder 수행.
   - 재귀 제한 해제 필요 (`sys.setrecursionlimit`).

## Python 코드

```python
import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.left = None
        self.right = None
        
def insert_node(parent, child):
    if child.x < parent.x:
        if parent.left is None:
            parent.left = child
        else:
            insert_node(parent.left, child)
    else:
        if parent.right is None:
            parent.right = child
        else:
            insert_node(parent.right, child)

def preorder(node, result):
    if node is None: return
    result.append(node.id)
    preorder(node.left, result)
    preorder(node.right, result)
    
def postorder(node, result):
    if node is None: return
    postorder(node.left, result)
    postorder(node.right, result)
    result.append(node.id)

def solution(nodeinfo):
    nodes = []
    for i, (x, y) in enumerate(nodeinfo):
        nodes.append(Node(i + 1, x, y))
        
    # y 내림차순, x 오름차순
    nodes.sort(key=lambda n: (-n.y, n.x))
    
    root = nodes[0]
    for i in range(1, len(nodes)):
        insert_node(root, nodes[i])
        
    pre = []
    post = []
    
    preorder(root, pre)
    postorder(root, post)
    
    return [pre, post]
```
