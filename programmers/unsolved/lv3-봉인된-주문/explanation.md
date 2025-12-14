# 봉인된 주문 (Sealed Spell)

## 문제 설명

주문서는 알파벳 소문자로 구성된 모든 문자열이 길이 순, 사전 순으로 정렬된 목록입니다.
일부 주문이 `bans` 목록에 의해 삭제되었습니다.
삭제된 주문을 제외하고 `n`번째에 위치하는 주문을 찾아야 합니다.

## 문제 분석

1.  **주문서의 규칙**:
    - 길이 1: "a" ~ "z" (26개)
    - 길이 2: "aa" ~ "zz" (26^2개)
    - ...
    - 전체적으로 길이 우선, 그 다음 사전 순 정렬입니다.
    - 이는 사실상 26진법 수 체계와 유사하지만, 자릿수가 늘어날 때마다 이전 길이의 모든 경우의 수를 더해주는 방식입니다.

2.  **삭제된 주문 처리**:
    - `bans`에 포함된 주문들을 건너뛰고 `n`번째를 세어야 합니다.
    - `n`이 최대 $10^{15}$로 매우 크기 때문에, 하나씩 세는 시뮬레이션은 불가능합니다.
    - `bans`의 길이는 최대 300,000입니다.
    - 따라서 수학적 접근이 필요합니다.

## 접근 방법

### 1. 문자열 $\leftrightarrow$ 정수 변환 (1-based Indexing)

모든 가능한 주문 문자열에 1부터 시작하는 고유 번호를 부여할 수 있습니다.
- "a" $\rightarrow$ 1
- "z" $\rightarrow$ 26
- "aa" $\rightarrow$ 27
- ...

변환 공식:
- **String to Int**:
  - 길이가 $L$인 문자열의 시작 번호는 $\sum_{i=1}^{L-1} 26^i + 1$ 입니다.
  - 여기에 해당 문자열이 길이 $L$인 문자열들 중에서 몇 번째인지(0-based rank)를 더합니다.
  - Rank는 26진법 변환과 동일하게 계산합니다. ($s[0] \times 26^{L-1} + s[1] \times 26^{L-2} + \dots$)

- **Int to String**:
  - 번호 $V$가 주어지면, 누적 합을 이용하여 길이를 먼저 찾습니다.
  - 해당 길이 내에서의 순서(offset)를 구한 뒤, 이를 26진법으로 변환하여 문자로 바꿉니다.

### 2. 타겟 번호 찾기

우리가 찾아야 할 주문의 "원래 번호(삭제되지 않았을 때의 번호)"를 $X$라고 합시다.
$X$번째 주문이 실제로는 삭제된 주문들을 제외하고 $n$번째여야 하므로, 다음 관계가 성립합니다.
$$ X - (\text{count of bans} \le X) = n $$
$$ X = n + (\text{count of bans} \le X) $$

이를 구하기 위해 다음과 같이 반복적으로 접근할 수 있습니다.
1. `curr = n`으로 시작합니다. (삭제된 주문이 없다면 $n$번째가 답이므로)
2. `bans` 리스트를 정수로 변환하여 오름차순 정렬해 둡니다.
3. 정렬된 `bans`를 순회하면서, 현재 `curr`보다 작거나 같은 삭제된 주문이 보일 때마다 `curr`를 1씩 증가시킵니다.
   - 원리: 내 앞에 삭제된 주문이 하나 있으면, 나는 한 칸 뒤로 밀려나야 하기 때문입니다.
   - `curr`가 증가하면, 이전에 `curr`보다 커서 카운트하지 않았던 삭제된 주문이 새로우 범위에 포함될 수 있습니다. 정렬된 리스트를 순차적으로 확인하면 이를 자연스럽게 처리할 수 있습니다.

### 알고리즘

1. `bans`의 모든 문자열을 정수로 변환하여 리스트 `B`를 만들고 정렬합니다.
2. `curr = n`
3. `B`의 각 원소 `b`에 대해:
   - if `b <= curr`: `curr += 1`
   - else: `break` (더 이상 `curr`에 영향을 주는 삭제된 주문은 없음)
4. 최종 `curr` 값을 문자열로 변환하여 반환합니다.

## Python 풀이

```python
def solution(n, bans):
    # 각 길이별로 가능한 문자열의 개수 누적합 미리 계산
    # cum_counts[k] = 길이가 k 이하인 모든 문자열의 개수
    cum_counts = [0] * 12
    current_sum = 0
    pow26 = [1] * 12
    for i in range(1, 12):
        pow26[i] = pow26[i-1] * 26
        current_sum += pow26[i]
        cum_counts[i] = current_sum

    # 문자열을 1-based 인덱스로 변환하는 함수
    def str_to_val(s):
        L = len(s)
        # 길이가 L보다 작은 모든 문자열의 개수를 더함
        val = cum_counts[L-1]
        
        # 길이가 L인 문자열 내에서의 순서(0-based) 계산
        rank = 0
        for i, char in enumerate(s):
            digit = ord(char) - ord('a')
            rank += digit * pow26[L - 1 - i]
        
        # 1-based 인덱스로 반환
        return val + rank + 1

    # 1-based 인덱스를 문자열로 변환하는 함수
    def val_to_str(v):
        # 해당 인덱스가 속하는 길이 L 찾기
        L = 1
        while L <= 11:
            if v <= cum_counts[L]:
                break
            L += 1
        
        # 길이가 L인 문자열 내에서의 순서(0-based)
        rank = v - cum_counts[L-1] - 1
        
        # 26진법 변환
        chars = []
        for i in range(L):
            power = pow26[L - 1 - i]
            digit = rank // power
            chars.append(chr(digit + ord('a')))
            rank %= power
        
        return "".join(chars)

    # bans 배열을 정수로 변환 후 정렬
    ban_vals = []
    for b in bans:
        ban_vals.append(str_to_val(b))
    
    ban_vals.sort()
    
    # n번째 유효한 주문 찾기
    curr = n
    for b in ban_vals:
        if b <= curr:
            curr += 1
        else:
            break
            
    return val_to_str(curr)
```

## 복잡도 분석

- **시간 복잡도**: $O(M \log M)$, 여기서 $M$은 `bans`의 길이입니다.
    - 문자열 변환: 상수 시간 (길이 최대 11).
    - 정렬: $O(M \log M)$.
    - 선형 탐색: $O(M)$.
- **공간 복잡도**: $O(M)$, 변환된 정수 리스트 저장 공간입니다.
