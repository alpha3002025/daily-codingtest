# 봉인된 주문

## 문제 설명
영일이는 마법의 주문을 외우려고 합니다. 주문서는 규칙에 따라 생성된 문자열들의 리스트입니다.
1. 길이가 짧은 문자열이 먼저 나옵니다.
2. 길이가 같다면 사전 순으로 정렬됩니다.
(`a`, `b`, ..., `z`, `aa`, `ab`, ...)

이 중 일부 주문은 `bans` 리스트에 포함되어 봉인되었습니다. 봉인된 주문을 제외하고 `n`번째 주문을 찾아야 합니다.

## 문제 해결 전략

이 문제는 **수학적 카운팅**과 **이분 탐색**을 결합하여 해결할 수 있습니다. `n`이 최대 $10^{15}$로 매우 크기 때문에, 단순히 문자열을 나열하는 것은 불가능합니다.

### 1. 자릿수(길이) 확정하기
먼저 `n`번째 주문이 몇 글자인지 알아내야 합니다.
- 길이가 $L$인 문자열의 전체 개수는 $26^L$개입니다.
- `bans`에 포함된 문자열 중 길이가 $L$인 것의 개수를 뺍니다.
- `n`에서 해당 길이의 유효한 문자열 개수를 빼가며, `n`이 0 이하가 되는 시점의 길이를 찾습니다.

### 2. 해당 길이 내에서의 순서 찾기
길이가 $L$로 정해졌다면, 해당 길이의 전체 문자열 공간에서 `bans`를 고려했을 때 `n`번째인 문자열을 찾아야 합니다.
이 과정은 **이분 탐색**으로 최적화할 수 있습니다.
- 탐색 범위: $0$ ~ $26^L - 1$ (각 숫자는 길이 $L$의 문자열에 1:1 매핑됨)
- `mid` 값을 문자열로 변환했을 때, 이보다 작거나 같은(사전 순) 봉인된 주문의 개수를 `cnt`라고 하면,
- `mid`의 실제 순위(봉인 제외) = `mid - cnt + 1` (1-based index)
- 이 순위가 목표 `n`과 같은지 확인하며 범위를 좁힙니다.

### 3. 진법 변환
숫자를 길이 $L$의 26진수 문자열로, 또는 그 반대로 변환하는 함수가 필요합니다. a=0, b=1, ... , z=25로 매핑하여 처리합니다.

## Python 코드

```python
def solution(n, bans):
    # 1. 밴 리스트 정리: 길이별로 분류
    bans_by_len = {}
    for b in bans:
        l = len(b)
        if l not in bans_by_len:
            bans_by_len[l] = []
        bans_by_len[l].append(b)
    
    # bans 내에서 탐색을 위해 정렬해둠 (이분 탐색용)
    for l in bans_by_len:
        bans_by_len[l].sort()

    # 숫자 -> 문자열 변환 함수 (0 -> 'a' ... 25 -> 'z')
    def num_to_str(val, length):
        res = []
        for _ in range(length):
            res.append(chr(ord('a') + val % 26))
            val //= 26
        return "".join(res[::-1])

    # 문자열 -> 숫자 변환 함수
    def str_to_num(s):
        val = 0
        for char in s:
            val = val * 26 + (ord(char) - ord('a'))
        return val

    # 2. 목표 문자열의 길이(length) 찾기
    length = 0
    for l in range(1, 12): # 문제 조건 상 11글자 이하
        total_count = 26**l
        banned_count = len(bans_by_len.get(l, []))
        valid_count = total_count - banned_count
        
        if n <= valid_count:
            length = l
            break
        n -= valid_count
    
    # 3. 이분 탐색으로 해당 길이 내에서 n번째 문자열 찾기
    # 범위: 0 ~ 26^length - 1
    left, right = 0, 26**length - 1
    answer_val = 0
    
    current_bans = bans_by_len.get(length, [])
    # bans를 숫자로 변환해둠
    current_bans_nums = [str_to_num(b) for b in current_bans]

    while left <= right:
        mid = (left + right) // 2
        
        # mid값 이하인 ban된 숫자의 개수 찾기 (bisect_right)
        from bisect import bisect_right
        banned_cnt = bisect_right(current_bans_nums, mid)
        
        # 실제 순위 (1-based)
        real_rank = mid - banned_cnt + 1
        
        if real_rank >= n:
            answer_val = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return num_to_str(answer_val, length)
```
