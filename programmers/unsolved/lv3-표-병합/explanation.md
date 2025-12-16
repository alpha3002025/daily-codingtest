# 표 병합

## 문제 설명
50x50 크기의 엑셀 시트 같은 표에서 `UPDATE`, `MERGE`, `UNMERGE`, `PRINT` 명령어를 처리합니다.
- `UPDATE`: 특정 셀 값 변경, 또는 특정 값을 가진 모든 셀 값 변경.
- `MERGE`: 두 셀 병합. 두 셀은 같은 그룹이 되며 값을 공유합니다.
- `UNMERGE`: 셀의 병합 해제. 선택된 셀만 값을 갖고 나머지는 비워집니다.
- `PRINT`: 셀 값 출력.

## 문제 해결 전략

**Union-Find (Disjoint Set)** 알고리즘이 핵심입니다.
각 좌표 $(r, c)$를 $0$부터 $2499$까지의 정수로 매핑하고, `parent` 배열로 병합 관계를 관리합니다.

1. **자료구조**:
   - `parent`: 각 셀의 부모(대표) 셀 인덱스.
   - `cells`: 각 셀의 값 (문자열). 실제 값은 **대표(root) 셀**에만 저장합니다.

2. **명령어 처리**:
   - `UPDATE r c value`:
     - $(r, c)$의 루트 $root$를 찾고, `cells[root] = value`.
   - `UPDATE value1 value2`:
     - 모든 셀(또는 모든 루트)을 순회하며 값이 `value1`이면 `value2`로 변경.
   - `MERGE r1 c1 r2 c2`:
     - 두 좌표의 루트 $root1, root2$를 찾습니다.
     - 같다면 무시.
     - 다르다면 하나로 합칩니다(Union).
     - **값 병합 규칙**: 한쪽만 값이 있으면 그 값을 가짐. 둘 다 있으면 $(r1, c1)$ 값(즉 $root1$의 값)을 가짐.
     - 병합 후 자식 쪽 값은 비워도 됨(루트만 참조하므로).
   - `UNMERGE r c`:
     - $(r, c)$의 루트 $root$를 찾습니다.
     - $root$가 가지고 있던 값($val$)을 저장해둡니다.
     - **전체 순회**하며 $root$와 같은 그룹(find 결과가 $root$)인 모든 셀들의 병합을 풉니다.
       - `parent[i] = i`, `cells[i] = "EMPTY"`
     - 원래 지정된 $(r, c)$ 셀에 값을 복구: `cells[converted_rc] = val`.
     - 주의: Union-Find에서 특정 그룹만 해제하는 표준 연산은 없습니다. $N=50$으로 작으므로, 모든 셀(2500개)에 대해 `find`를 수행하여 그룹을 찾아도 충분합니다.

   - `PRINT r c`:
     - $(r, c)$의 루트를 찾아 그 `cells` 값을 출력.

## Python 코드

```python
def solution(commands):
    # 50x50 = 2500
    parent = list(range(2501))
    cells = ["EMPTY"] * 2501
    
    def find(x):
        if parent[x] == x:
            return x
        parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            parent[rootY] = rootX
            
    def convert(r, c):
        return (int(r) - 1) * 50 + int(c)

    answer = []
    
    for cmd in commands:
        parts = cmd.split()
        op = parts[0]
        
        if op == "UPDATE":
            if len(parts) == 4: # UPDATE r c value
                r, c, value = parts[1], parts[2], parts[3]
                idx = convert(r, c)
                root = find(idx)
                cells[root] = value
            else: # UPDATE val1 val2
                val1, val2 = parts[1], parts[2]
                for i in range(1, 2501):
                    # 모든 '루트'에 대해 값을 바꿀 수도 있고
                    # 그냥 cells 전체 순회해도 되지만, 
                    # 정확히는 '값'은 루트에만 의미가 있음.
                    # 하지만 편의상 cells 배열을 다 쓴다면 
                    # find(i)==i (루트)인 경우만 바꿔야 논리적 오류 없음.
                    # 혹은 모든 셀이 루트를 바라보므로, 루트값만 바꿔도 됨.
                    if find(i) == i and cells[i] == val1:
                        cells[i] = val2
                        
        elif op == "MERGE":
            r1, c1, r2, c2 = parts[1], parts[2], parts[3], parts[4]
            idx1 = convert(r1, c1)
            idx2 = convert(r2, c2)
            
            root1 = find(idx1)
            root2 = find(idx2)
            
            if root1 != root2:
                # 값 결정
                new_val = "EMPTY"
                if cells[root1] != "EMPTY":
                    new_val = cells[root1]
                elif cells[root2] != "EMPTY":
                    new_val = cells[root2]
                
                # 병합 (root2를 root1 밑으로)
                union(root1, root2)
                cells[root1] = new_val # 대표 노드 값 갱신
                # cells[root2]는 이제 쓰이지 않음
                
        elif op == "UNMERGE":
            r, c = parts[1], parts[2]
            idx = convert(r, c)
            root = find(idx)
            val = cells[root]
            
            # 모든 셀 검사하여 root가 같은 애들 분리
            # 주의: loop 돌면서 parent를 리셋하므로, 
            # find 결과가 달라질 수 있음. 
            # 따라서 '타겟들'을 먼저 찾고나서 리셋해야 함.
            targets = []
            for i in range(1, 2501):
                if find(i) == root:
                    targets.append(i)
                    
            for i in targets:
                parent[i] = i
                cells[i] = "EMPTY"
                
            # 지정된 셀(r, c)에 값 복구
            cells[idx] = val
            
        elif op == "PRINT":
            r, c = parts[1], parts[2]
            idx = convert(r, c)
            root = find(idx)
            answer.append(cells[root])
            
    return answer
```
