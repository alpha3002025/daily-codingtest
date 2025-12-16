# 전화번호 목록

## 문제 설명
전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어(Prefix)인 경우가 있는지 확인합니다. 있으면 `false`, 없으면 `true`를 반환합니다.

### 핵심 개념
1.  **정렬 (Sorting)**: 문자열을 정렬하면 비슷한(접두어가 될 가능성이 있는) 번호끼리 인접하게 됩니다.
    - 예: `["119", "97674223", "1195524421"]` -> 정렬 -> `["119", "1195524421", "97674223"]`
    - 바로 뒷 번호(`i+1`)가 앞 번호(`i`)로 시작하는지만 확인하면 됩니다. $O(N \log N)$.
2.  **해시 (Hash)**: 모든 번호를 해시 맵(딕셔너리)에 넣고, 각 번호의 접두어들이 맵에 존재하는지 확인합니다. $O(N \times Length)$.

## Python 풀이 (정렬)

```python
def solution(phone_book):
    # 1. 문자열 정렬
    phone_book.sort()
    
    # 2. 인접한 두 번호 비교
    for i in range(len(phone_book) - 1):
        # 뒷 번호(i+1)가 앞 번호(i)로 시작하면 접두어 관계
        if phone_book[i+1].startswith(phone_book[i]):
            return False
            
    return True
```

## Python 풀이 (해시)

```python
def solution(phone_book):
    # Lookup 속도를 위해 딕셔너리로 변환
    phone_map = {num: 1 for num in phone_book}
    
    for phone_number in phone_book:
        temp = ""
        # 번호의 각 글자를 더해가며 접두어를 만든다
        for digit in phone_number:
            temp += digit
            # 만든 접두어(temp)가 맵에 존재하고, 그게 자기 자신이 아니라면
            if temp in phone_map and temp != phone_number:
                return False
                
    return True
```

### 코드 설명
- **정렬 방식**: 매우 직관적이고 코드가 짧습니다. 문자열 정렬의 특성상 "12"와 "123"은 반드시 붙어있게 되므로, 인접 요소만 비교해도 충분합니다.
- **해시 방식**: 전화번호 길이가 짧다면(최대 20) 효율적입니다.
