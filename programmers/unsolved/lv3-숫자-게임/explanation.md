# 숫자 게임

## 문제 설명
A팀과 B팀이 숫자가 적힌 카드를 냅니다.
B팀은 A팀이 낼 카드의 순서를 알고 있습니다.
높은 숫자가 이깁니다.
B팀이 얻을 수 있는 최대 승점을 구하세요.

## 문제 해결 전략

**그리디 (Greedy)** 알고리즘.
- A와 B를 오름차순 정렬합니다.
- B의 가장 작은 카드가 A의 가장 작은 카드를 이길 수 있다면? -> 이기는 게 이득 (승점 1 획득).
- 이길 수 없다면? -> B의 가장 작은 카드는 A의 어떤 카드도 못 이기거나, 가장 강한 A에게 져주는 게 나음 (여기선 순서가 중요치 않으므로 그냥 버림).
- 즉, `B[j] > A[i]`를 만족하는 최소의 `B[j]`를 매칭합니다.

## Python 코드

```python
def solution(A, B):
    A.sort()
    B.sort()
    
    answer = 0
    idx_a = 0
    idx_b = 0
    n = len(A)
    
    while idx_a < n and idx_b < n:
        if B[idx_b] > A[idx_a]:
            # B가 이김 -> 승점 획득, 둘 다 다음 카드로
            answer += 1
            idx_a += 1
            idx_b += 1
        else:
            # B가 못 이김 -> B만 더 큰 카드로 넘어감 (현재 B는 버림)
            idx_b += 1
            
    return answer
```
