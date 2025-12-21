# 카드 뭉치

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/159994)

두 개의 카드 뭉치 `cards1`, `cards2`가 순서대로 정렬되어 있습니다.
원하는 문장 `goal`을 만들기 위해, **순서를 바꾸지 않고** 각 뭉치의 **가장 앞에 있는 카드**만 사용하여 문장을 완성할 수 있는지 ("Yes" / "No") 확인하세요.
- 한 번 사용한 카드는 버려집니다(재사용 불가).
- 뭉치의 순서를 건너뛸 수 없습니다.

## 해결 전략
두 카드 뭉치의 현재 위치를 가리키는 포인터(인덱스) 두 개를 사용합니다.
`goal`의 단어를 순서대로 확인하면서:
1. `cards1`의 현재 카드가 목표 단어와 같으면 `idx1` 증가.
2. `cards2`의 현재 카드가 목표 단어와 같으면 `idx2` 증가.
3. 둘 다 아니라면 만들 수 없으므로 "No".

### 알고리즘 순서
1. `idx1`, `idx2` = 0
2. `goal`의 각 단어 `word`에 대해:
    - 만약 `idx1 < len(cards1)` 이고 `cards1[idx1] == word`:
        - `idx1 += 1`
    - 만약 `idx2 < len(cards2)` 이고 `cards2[idx2] == word`:
        - `idx2 += 1`
    - 둘 다 아니면 return "No"
3. 모든 단어를 통과하면 "Yes" 반환.

## Python 코드

```python
def solution(cards1, cards2, goal):
    idx1 = 0
    idx2 = 0
    
    for word in goal:
        # 카드 뭉치 1 확인 (인덱스 범위 체크 필수)
        if idx1 < len(cards1) and cards1[idx1] == word:
            idx1 += 1
        # 카드 뭉치 2 확인
        elif idx2 < len(cards2) and cards2[idx2] == word:
            idx2 += 1
        # 둘 다 없으면 실패
        else:
            return "No"
            
    return "Yes"
```

## 배운 점 / 팁
- **투 포인터 (Two Pointers)**: 두 배열을 동시에 순회하며 비교할 때 유용한 기본 테크닉입니다.
- **인덱스 범위 체크**: 배열 접근 전 `idx < len()` 검사는 필수입니다. 그렇지 않으면 `IndexError`가 발생합니다.
- `pop(0)`을 사용하는 방법도 있지만, 리스트의 앞 요소를 제거하는 것은 `O(N)` 비용이 들기에 인덱스를 사용하는 것이 더 효율적입니다. (물론 `cards` 길이가 최대 10이라 `pop`도 상관없음)
