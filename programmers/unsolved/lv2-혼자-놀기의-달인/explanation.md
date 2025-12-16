# 혼자 놀기의 달인

## 문제 설명
1번부터 n번까지의 카드가 무작위로 상자에 들어있습니다.
1. 임의의 상자를 열어 숫자를 확인하고, 그 숫자에 해당하는 상자를 찾아가서 엽니다. 이를 이미 열려있는 상자를 만날 때까지 반복합니다. 이것이 1번 그룹입니다.
2. 남은 상자가 있다면 다시 임의의 상자를 골라 같은 방식으로 반복해 2번 그룹을 만듭니다.
3. 1번 그룹의 상자 수와 2번 그룹의 상자 수를 곱해 점수를 얻습니다. 남은 상자가 없으면 점수는 0입니다. 최대로 얻을 수 있는 점수를 구합니다.

## 풀이 개념
**그래프 탐색 (DFS/Cycle Detection)** 문제입니다.
각 카드는 단 하나의 '다음 상자'를 가리키므로, 여러 개의 독립적인 **사이클(Cycle)**들로 구성된 형태입니다.

1. 방문 여부(`visited`) 배열을 만듭니다.
2. 모든 상자에 대해 방문하지 않았다면 DFS/반복문을 통해 사이클을 탐색하고, 사이클의 크기(그룹의 크기)를 구합니다.
3. 모든 그룹의 크기를 리스트에 모읍니다.
4. 그룹 개수를 내림차순 정렬합니다.
5. 만약 그룹이 1개 이하라면 점수는 0입니다.
6. 그룹이 2개 이상이라면 가장 큰 두 그룹의 크기를 곱합니다.

## 코드 (Python)

```python
def solution(cards):
    n = len(cards)
    visited = [False] * n
    groups = []
    
    for i in range(n):
        if not visited[i]:
            count = 0
            current = i
            while not visited[current]:
                visited[current] = True
                current = cards[current] - 1 # 1-based index to 0-based
                count += 1
            groups.append(count)
            
    if len(groups) < 2:
        return 0
    
    groups.sort(reverse=True)
    return groups[0] * groups[1]
```
