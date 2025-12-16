# [3차] 파일명 정렬

## 문제 설명
파일명은 크게 `HEAD`, `NUMBER`, `TAIL` 세 부분으로 나뉩니다.
- **HEAD**: 숫자가 나오기 전까지의 문자 부분. 대소문자 구분 없음.
- **NUMBER**: 연속된 숫자 부분 (최대 5자리). 앞의 0은 무시됨.
- **TAIL**: 나머지 부분. 정렬 기준 아님.
파일명을 위 기준(`HEAD` 사전순 -> `NUMBER` 오름차순 -> 입력 순서 유지)으로 정렬하세요.

### 핵심 개념
1.  **정규표현식 (Regex)**: 문자열을 세 부분으로 나누는 데 가장 효율적입니다.
    - `(\D+)(\d{1,5})(.*)`
    - `\D+`: 숫자가 아닌 것 (HEAD)
    - `\d{1,5}`: 숫자 1~5개 (NUMBER)
    - `.*`: 나머지 (TAIL)
2.  **안정 정렬 (Stable Sort)**: Python의 `sort`는 기본적으로 안정 정렬입니다. 즉, 정렬 기준이 같으면 원래 순서가 유지되므로 세 번째 조건(입력 순서 유지)은 신경 쓰지 않아도 됩니다.

## Python 풀이

```python
import re

def solution(files):
    # 정렬 키 함수 정의
    def sort_key(file):
        # 정규식으로 그룹 분리
        # ([^0-9]+): 숫자가 아닌 부분 (HEAD)
        # ([0-9]+): 숫자 부분 (NUMBER) -> re는 탐욕적이므로 연속된 숫자 다 잡음
        # 하지만 NUMBER는 최대 5글자라는 조건이 있음.
        # re.match보다는 re.split이나 그냥 직접 파싱이 나을 수도 있음.
        # 가장 간단한 re: (\D+)(\d+)
        
        match = re.match(r'(\D+)(\d+)', file)
        head = match.group(1).lower() # 대소문자 구분 X
        number = int(match.group(2))  # 숫자 값 비교
        
        return (head, number)
    
    # 1. key 기준으로 정렬
    # Python sort는 stable sort이므로 HEAD, NUMBER가 같으면 원래 순서 유지됨
    files.sort(key=sort_key)
    
    return files
```

### 코드 설명
- `re.match(r'(\D+)(\d+)', file)`: 파일명의 시작부터 패턴을 찾습니다. `TAIL` 부분은 매칭 그룹에 넣지 않아도 정렬에 영향을 주지 않으므로 무시해도 됩니다. (match는 문자열 처음부터 매칭하므로 뒤에 남는 건 상관없음)
- `group(1).lower()`: HEAD는 대소문자를 구분하지 않으므로 소문자로 변환하여 비교합니다.
- `int(group(2))`: NUMBER는 숫자 크기로 비교해야 하므로 `int`로 변환합니다. `010`과 `10`은 같은 값으로 취급됩니다.
- `files.sort(...)`: 원본 리스트를 정렬합니다. Python의 Timsort는 안정 정렬을 보장합니다.
