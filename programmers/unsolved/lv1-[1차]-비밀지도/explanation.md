# [1차] 비밀지도

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/17681)

두 개의 지도(`arr1`, `arr2`)가 암호화되어 있습니다.
- 각 숫자는 이진수로 변환했을 때 지도의 한 행(`row`)을 나타냅니다. (1: 벽 `#`, 0: 공백 ` `)
- 두 지도 중 **하나라도 벽**인 부분은 전체 지도에서도 벽(#)입니다.
- 두 지도 모두 공백인 부분만 공백( )입니다.
최종 지도를 해독하여 문자열 배열로 반환하세요.

## 해결 전략
**비트 연산(Bitwise Operation)** 문제입니다.
1. 두 수를 `OR` 연산(`|`)하면 둘 중 하나라도 1인 비트는 1이 됩니다.
    - `9 | 30` -> `01001 | 11110` -> `11111`
2. 결과값을 이진수 문자열로 변환하고, `1`은 `#`, `0`은 ` `으로 바꿉니다.
3. 자릿수(`n`)를 맞추기 위해 앞쪽에 `0`을 채워야 할 수 있습니다 (`zfill` 사용).

### 알고리즘 순서
1. `answer` = []
2. `zip(arr1, arr2)` 순회 (`n1`, `n2`):
    - `merged` = `n1 | n2` (비트 OR)
    - `bin_str` = `bin(merged)[2:]` (`0b` 제거)
    - `bin_str` = `bin_str.zfill(n)` (자릿수 맞춤)
    - `decoded` = `bin_str` replace `1`->`#`, `0`->` `
    - `answer.append(decoded)`
3. 반환.

## Python 코드

```python
def solution(n, arr1, arr2):
    answer = []
    
    for num1, num2 in zip(arr1, arr2):
        # 비트 OR 연산 (둘 중 하나라도 1이면 1)
        merged = num1 | num2
        
        # 이진수 문자열로 변환 (접두사 0b 제거)
        binary_str = bin(merged)[2:]
        
        # 자릿수 n에 맞춰 0 채우기
        binary_str = binary_str.zfill(n)
        
        # 1 -> #, 0 -> 공백 변환
        decoded_row = binary_str.replace('1', '#').replace('0', ' ')
        
        answer.append(decoded_row)
        
    return answer
```

## 배운 점 / 팁
- **비트 연산**: 지도의 겹침 표현은 비트 OR가 가장 직관적이고 빠릅니다.
- **zfill**: 문자열의 길이를 맞추기 위해 앞에 0을 채우는 메소드입니다. 이진수 변환 시 필수적입니다.
