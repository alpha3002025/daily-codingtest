# 유사 칸토어 비트열

## 문제 설명
0번째 유사 칸토어 비트열은 "1"입니다.
n번째 비트열은 n-1번째 비트열에서 1을 "11011"로, 0을 "00000"으로 치환하여 만듭니다.
`n`과 구간 `[l, r]`이 주어졌을 때, 해당 구간 내에 존재하는 1의 개수를 구하는 문제입니다.

## 풀이 개념
**분할 정복 (Divide and Conquer)** 또는 **재귀**를 사용합니다.
비트열을 다 생성하면 길이가 `5^n`으로 매우 커지므로(최대 5^20), 직접 생성할 수 없습니다.
특정 위치의 비트가 1인지 0인지를 재귀적으로 판별하거나, 누적 1의 개수를 계산하는 함수를 만듭니다.

`count_ones(n, limit)`: n번째 비트열의 앞에서부터 `limit`개까지의 1의 개수를 반환하는 함수.
답은 `count_ones(n, r) - count_ones(n, l - 1)`로 구할 수 있습니다.

**로직**:
- 길이 `len = 5^n`. 이를 5등분하면 각 섹션의 길이는 `part = 5^(n-1)`.
- `limit`이 몇 번째 섹션(`idx = limit // part`)에 속하는지 확인합니다.
- 앞쪽의 완전한 섹션들에 대해:
  - 0, 1번 섹션(11...): 각각 `4^(n-1)`개의 1이 있음.
  - 2번 섹션(00...): 1이 없음 (0개).
  - 3, 4번 섹션(11...): 각 `4^(n-1)`개의 1이 있음.
- `limit`이 속한 마지막 불완전한 섹션에 대해 재귀 호출:
  - 만약 그 섹션이 2번(가운데 0)이라면 더 이상 셀 필요 없음 (0이므로).
  - 아니라면 `count_ones(n-1, limit % part)`를 더해줌.

## 코드 (Python)

```python
def solution(n, l, r):
    # n번째 비트열에서 k번째 인덱스(1-based)까지의 1의 개수 반환
    def count(n, k):
        if n == 0:
            return 1 if k > 0 else 0
        if k == 0:
            return 0
            
        part_len = 5 ** (n - 1) # 한 섹션의 길이
        section = k // part_len # 0 ~ 4 섹션 중 어디인지 (완전히 포함된 개수)
        remainder = k % part_len
        
        # 이전 단계의 전체 1 개수
        prev_ones = 4 ** (n - 1)
        
        result = 0
        
        # 1. 완전히 포함된 앞 섹션들 계산
        if section < 2:
            result = section * prev_ones
        elif section == 2: # 0, 1 섹션만 더함 (2는 00000)
            result = 2 * prev_ones
        else: # section > 2 (3, 4)
            result = (section - 1) * prev_ones
            
        # 2. 현재 작업 중인 섹션(section) 내부의 나머지 계산
        # 만약 현재 섹션이 2(가운데 0구간)라면 나머지도 전부 0이므로 더하지 않음.
        if section != 2:
            result += count(n - 1, remainder)
            
        return result

    return count(n, r) - count(n, l - 1)
```
