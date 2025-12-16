# 홀짝트리

## 문제 설명
주어진 트리 형태의 데이터에서, 각 노드를 루트로 설정했을 때 해당 트리가 "홀짝 트리" 또는 "역홀짝 트리"의 성질을 만족하는지 판단하고, 만족하는 루트 노드의 개수를 구하는 문제입니다.

**조건 (가정 및 일반적 해석):**
- **홀짝 노드(Odd-Even Node)**: 노드의 값이 홀수이고, 자식 노드의 개수(차수)가 짝수인 경우 (문제의 정확한 정의 확인 필요, 여기서는 일반적인 트리 성질 문제의 패턴을 따름)
- **역홀짝 노드(Reverse Odd-Even Node)**: 노드의 성질이 반대인 경우.

문제의 핵심은 **루트 노드의 상태가 결정되면, 트리의 레벨(깊이)에 따라 자식 노드들이 가져야 할 상태가 교차로 결정된다**는 점입니다. 즉, 루트가 Pattern A라면 자식은 Pattern B, 그 자식은 Pattern A여야 합니다.

## 문제 해결 전략

각 노드가 "자신이 루트라면(혹은 부모와 다른 상태라면) 가질 수 있는 상태"와 "부모와 같은 상태라면 가질 수 있는 상태"를 가지고 있는지 미리 판별해야 합니다.

모든 노드를 루트로 시뮬레이션하면 $O(N^2)$이 되어 시간 초과가 발생할 수 있습니다. 따라서 **트리의 이분 그래프(Bipartite) 성질**과 **Re-rooting 아이디어**를 활용해야 합니다.

### 알고리즘
1. **각 노드의 가능한 상태 판별**:
   각 노드 $u$에 대해, "홀짝 노드" 조건($S_1$)과 "역홀짝 노드" 조건($S_2$)을 만족하는지 확인합니다.
   
2. **트리 2-Coloring (Parity)**:
   트리는 이분 그래프입니다. 임의의 노드(예: 1번)를 루트로 잡고 BFS/DFS를 수행하여 각 노드의 `color` (깊이의 홀짝 여부, 0 또는 1)를 매깁니다.
   - `dist(root, u) % 2 == color(root) ^ color(u)` 관계가 성립합니다.

3. **조건 통합**:
   어떤 노드 $r$이 루트가 되기 위해서는, 모든 노드 $u$에 대해 다음이 성립해야 합니다.
   - $r$이 상태 $S$ (0 또는 1)일 때, $u$는 상태 $S \oplus \text{dist}(r, u) \pmod 2$ 를 만족해야 합니다.
   - 즉, $u$ 입장에서 만족해야 하는 상태 $S_u = S \oplus \text{color}(r) \oplus \text{color}(u)$ 가 $u$의 가능한 상태 집합에 포함되어야 합니다.
   - 이를 정리하면, $S \oplus \text{color}(r) = S_u \oplus \text{color}(u)$ 입니다.
   - 모든 $u$에 대해 $RequiredState(u) = \{ S' \oplus \text{color}(u) \mid S' \in \text{PossibleStates}(u) \}$ 집합을 구합니다.
   - 모든 $u$의 교집합 $ValidCommonStates = \bigcap_u RequiredState(u)$을 구합니다.
   - 만약 $ValidCommonStates$가 비어있다면, 어떤 루트도 불가능합니다.
   - 비어있지 않다면, 각 후보 루트 $r$에 대해 $S \oplus \text{color}(r) \in ValidCommonStates$를 만족하는 $S$가 존재하는지 확인합니다.

### 핵심 아이디어 요약
"모든 노드가 동시에 만족해야 하는 불변량"을 찾아내는 것입니다. 각 노드는 자신의 `color`(깊이)와 자신의 값에 따라, "루트의 상태가 무엇일 때 내가 행복한가"를 말할 수 있습니다. 모두가 행복해지는 루트 상태 $X$가 존재한다면, 그 $X$를 제공해줄 수 있는 루트들을 세는 것입니다.

## Python 코드

```python
import sys
sys.setrecursionlimit(10**6)

def solution(nodes, edges):
    # nodes: [번호, 값] 리스트라고 가정 (문제 형식에 따라 파싱 필요)
    # edges: [u, v] 간선 리스트
    
    # 1. 인접 리스트 생성
    # nodes의 형태가 [num1, val1, num2, val2, ...] 인지 리스트의 리스트인지 확인 필요.
    # 여기서는 nodes가 [val1, val2, ...] 순서대로 1번부터 N번까지라고 가정하거나
    # 문제의 입력 형식에 맞게 조정 필요. 통상 1~N번 노드.
    
    # 문제 입력이 (nodes, edges)라면 nodes에 각 노드의 정보가 있을 것임.
    # nodes[i]가 i+1번 노드의 정보라고 가정.
    
    # 트리 구성 (숲일 수도 있음)
    # 문제에서 "하나의 트리"라고 했으면 OK. 숲이면 컴포넌트별로 계산 후 곱함.
    # 일단 하나의 트리로 가정 및 숲 처리 추가.
    
    n = len(nodes)
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
        
    # 각 노드의 "가능한 상태" 확인
    # 상태 0: 홀짝 노드 (가정: val 홀수, degree 짝수)
    # 상태 1: 역홀짝 노드 (가정: val 짝수, degree 홀수)
    # *정확한 정의는 문제 지문 필독*
    
    # 편의상, node_possible[u] = {0, 1} 중 가능한 것 집합
    node_possible = [set() for _ in range(n + 1)]
    
    for i in range(n):
        u = i + 1
        val = nodes[i]
        deg = len(adj[u])
        
        # 예시 로직 (문제 조건에 맞춰 수정 필수)
        is_odd_even = (val % 2 == 1) and (deg % 2 == 0)
        is_rev_odd_even = (val % 2 == 0) and (deg % 2 == 1)
        
        if is_odd_even: node_possible[u].add(0)
        if is_rev_odd_even: node_possible[u].add(1)
            
    visited = [False] * (n + 1)
    colors = [-1] * (n + 1)
    
    answer_roots = 0
    
    # 컴포넌트 별로 처리
    # 전체 정답은 (컴포넌트1의 가능한 루트 수) * (컴포넌트2...) 가 아니라,
    # "전체 노드 중 루트가 될 수 있는 것의 개수"를 묻는다면, 
    # 사실 숲인 경우, 하나의 루트를 정한다는 개념이 모호함.
    # 문제에서 "트리"라고 명시했으면 컴포넌트 1개.
    
    # 컴포넌트 1개라고 가정하고 BFS
    components = []
    
    for i in range(1, n + 1):
        if not visited[i]:
            # 새 컴포넌트 발견
            comp_nodes = []
            q = [i]
            visited[i] = True
            colors[i] = 0
            comp_nodes.append(i)
            
            valid_common = {0, 1} # 교집합 초기값
            
            idx = 0
            while idx < len(q):
                u = q[idx]; idx += 1
                
                # u의 제약조건을 common에 반영
                # u가 만족하려면, (RootColor ^ color[u]) 가 node_possible[u] 에 있어야 함.
                # 즉 RootColor 가 (state ^ color[u]) for state in node_possible[u] 이어야 함.
                required_root_states = {s ^ colors[u] for s in node_possible[u]}
                valid_common &= required_root_states
                
                if not valid_common:
                    break # 더 이상 불가능
                
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        colors[v] = 1 - colors[u]
                        q.append(v)
                        comp_nodes.append(v)
            
            # 이 컴포넌트 내의 노드가 루트가 되려면?
            # 만약 u가 루트라면, u 자신은 반드시 node_possible[u] 중 하나를 만족해야 함 (당연).
            # 그리고 RootColor는 node_possible[root_val] 중 하나.
            # 위에서 구한 valid_common은 "가상의 RootColor(0번노드 기준 위상)"에 대한 제약.
            # Root가 u일 때의 "실제 위상"은 color[u]와 관련됨.
            # 정확히: 우리가 구한 valid_common은 "Global Reference(예: color[start_node]=0)" 기준
            # 필요한 "Global Phase Shift" 값들의 집합.
            
            # 즉, 어떤 Global Phase P가 valid_common에 있다면,
            # color[start]가 0일 때, 전체 트리가 P 모드로 정렬됨을 의미.
            # 루트 r이 선택되었을 때, 이 트리의 위상은 color[r] ^ State(r) 에 의해 결정됨.
            # 즉, 우리는 (color[r] ^ State(r)) == P 인 r과 State(r)을 찾아야 함.
            
            if valid_common:
                # 컴포넌트 내의 각 노드를 루트로 시도
                # r이 루트가 되려면, r 스스로 가능한 상태 s \in node_possible[r] 가 존재해서
                # (s ^ colors[r]) \in valid_common 이어야 함.
                count = 0
                for u in comp_nodes:
                    can_be_root = False
                    for s in node_possible[u]:
                        if (s ^ colors[u]) in valid_common:
                            can_be_root = True
                            break
                    if can_be_root:
                        count += 1
                components.append(count)
            else:
                components.append(0)

    # 숲인 경우 처리 (문제에 따라 다름)
    # 만약 "숲"에서 노드 하나를 루트로 잡는다는 건, 그 노드가 포함된 트리만 루트 성질 갖는 것?
    # 문제 의도가 "주어진 그래프가 트리 하나"라면 components는 1개.
    if not components: return 0
    return components[0] 
```
