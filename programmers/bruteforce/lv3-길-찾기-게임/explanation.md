# 길 찾기 게임 (Finding the Path Game)

## 1. 문제 설명
- **문제 링크**: [https://school.programmers.co.kr/learn/courses/30/lessons/42892](https://school.programmers.co.kr/learn/courses/30/lessons/42892)
- **정보**:
  - 카카오 블라인드 채용 문제.
  - 노드의 $(x, y)$ 좌표가 주어집니다.
  - $y$값이 높을수록 상위 레벨(부모 쪽)에 위치합니다.
  - 같은 레벨($y$)인 경우 $x$가 작으면 왼쪽 자식, 크면 오른쪽 자식 방향입니다.
  - 이 규칙에 따라 구성된 **이진 트리(Binary Tree)**에서 **전위 순회(Preorder)**와 **후위 순회(Postorder)** 결과를 반환해야 합니다.
  - 노드의 개수는 최대 10,000개입니다.

---

## 2. 접근법 및 핵심 개념 (BST Construction)

### 개념: 이진 탐색 트리와 레벨
이 문제는 **이진 탐색 트리(BST)**의 성질을 가지고 있습니다. $x$좌표가 트리의 정렬 기준(Key) 역할을 하고, $y$좌표는 트리의 깊이(Level) 또는 우선순위를 결정합니다.

트리를 구성하는 가장 직관적인 방법은 다음과 같습니다:
1. **정렬**: $y$좌표가 높은 순서대로 노드를 정렬합니다. (루트 노드가 가장 위에 있어야 하므로)
2. **순차 삽입**: 정렬된 순서대로 BST에 노드를 하나씩 삽입합니다.
   - 먼저 들어간 노드는 나중에 들어오는 노드보다 항상 $y$가 크거나 같습니다(부모 후보).
   - 나중에 들어오는 노드는 먼저 자리 잡은 노드들과 $x$좌표를 비교하며 자신의 자리를 찾아갑니다.

### 알고리즘 단계
1. 노드 정보에 **원래 번호(Index)**를 추가하여 객체나 튜플로 관리합니다.
2. 리스트를 **$y$ 내림차순**(같으면 $x$ 오름차순)으로 정렬합니다.
3. 첫 번째 노드를 루트로 설정하고, 나머지 노드들을 순서대로 트리에 삽입합니다.
   - 삽입 시 현재 노드보다 $x$가 작으면 왼쪽, 크면 오른쪽으로 이동합니다.
   - 비어있는 자리에 도달하면 그곳에 연결합니다.
4. 완성된 트리로 전위 순회와 후위 순회를 수행하여 답을 구합니다.

---

## 3. Python 풀이

```python
import sys
sys.setrecursionlimit(10**6) # 재귀 깊이 제한 해제 (필수)

class Node:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.left = None
        self.right = None

def add_node(parent, child):
    # BST 삽입 로직: x좌표 비교하여 위치 선정
    if child.x < parent.x:
        if parent.left is None:
            parent.left = child
        else:
            add_node(parent.left, child)
    else: # child.x > parent.x
        if parent.right is None:
            parent.right = child
        else:
            add_node(parent.right, child)

def preorder(node, result):
    if node is None:
        return
    result.append(node.id)      # Root
    preorder(node.left, result) # Left
    preorder(node.right, result)# Right

def postorder(node, result):
    if node is None:
        return
    postorder(node.left, result)# Left
    postorder(node.right, result)# Right
    result.append(node.id)      # Root

def solution(nodeinfo):
    # 노드 객체 생성 (id는 1부터 시작)
    nodes = []
    for i, (x, y) in enumerate(nodeinfo):
        nodes.append(Node(i + 1, x, y))
    
    # 1. 정렬: y축 내림차순 (먼저 트리에 들어가야 부모가 됨)
    nodes.sort(key=lambda n: (-n.y, n.x))
    
    # 2. 트리 구성
    root = nodes[0]
    # 루트 이후의 노드들을 순서대로 삽입
    for i in range(1, len(nodes)):
        add_node(root, nodes[i])
        
    # 3. 순회 결과 기록
    pre_result = []
    post_result = []
    
    preorder(root, pre_result)
    postorder(root, post_result)
    
    return [pre_result, post_result]
```

---

## 4. 복잡도 분석
- **시간 복잡도**: 
  - 정렬: $O(N \log N)$
  - 트리 구성:
    - 평균적인 경우(균형 잡힌 트리): $O(N \log N)$
    - 최악의 경우(한쪽으로 치우친 편향 트리): $O(N^2)$
    - $N=10,000$일 때 최악의 경우 $10^8$ 연산이지만, 단순 비교 연산이므로 Python으로 통과 가능합니다.
  - 순회: $O(N)$
- **공간 복잡도**: $O(N)$
  - 모든 노드 객체 저장 및 재귀 호출 스택($N$ 깊이).
  - 따라서 `sys.setrecursionlimit` 설정이 반드시 필요합니다.

## 5. 최적화 팁 (참고)
$O(N^2)$ 최악의 경우를 피하고 싶다면, 트리를 삽입 방식이 아니라 **분할 정복**으로 구성할 수도 있습니다.
1. 현재 범위의 노드 중 $y$가 가장 큰 노드를 찾습니다(Root).
2. 그 노드의 $x$를 기준으로 왼쪽 그룹, 오른쪽 그룹으로 리스트를 나눕니다.
3. 각 그룹에 대해 재귀적으로 수행합니다.
이 경우에도 매번 최대값을 찾으면 $O(N^2)$이 되지만, $y$값에 대해 미리 정렬된 정보를 활용하거나 쿼리 구조를 쓰면 최적화할 수 있습니다. 하지만 이 문제에서는 위 삽입 방식이 구현이 더 간단하고 효율성 테스트를 통과합니다.
