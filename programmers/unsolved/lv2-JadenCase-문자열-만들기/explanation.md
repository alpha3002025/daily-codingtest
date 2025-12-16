# JadenCase 문자열 만들기

## 문제 설명
JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다. 문자열 `s`가 주어졌을 때 JadenCase로 바꾼 문자열을 리턴하세요.
예: "3people unFollowed me" -> "3people Unfollowed Me"

### 핵심 개념
1.  **공백 유지**: 단순히 `split()`을 쓰면 **연속된 공백**이 하나로 합쳐져 버립니다. 문제에서는 "공백문자가 연속해서 나올 수 있습니다"라고 했으므로, 공백을 그대로 유지해야 합니다.
2.  **문자 변환**: `upper()`, `lower()`를 사용합니다.
3.  **구현**:
    - `split(' ')`을 사용하면 공백을 기준으로 빈 문자열(`''`)을 포함해 리스트가 만들어집니다. 이를 이용해 원래 공백 개수를 유지할 수 있습니다.
    - `capitalize()` 함수를 써도 편합니다.

## Python 풀이

```python
def solution(s):
    # 공백을 기준으로 분리 (연속된 공백도 빈 문자열로 리스트에 들어감)
    # 예: "a   b" -> ["a", "", "", "b"]
    words = s.split(' ')
    
    new_words = []
    for word in words:
        if word:
            # 첫 글자는 대문자, 나머지는 소문자
            # capitalize()는 숫자가 앞에 오면 그대로 두고 뒤만 소문자로 바꿔주므로 완벽함
            new_words.append(word.capitalize())
        else:
            # 빈 문자열(원래 공백이었던 자리)은 그대로
            new_words.append(word)
            
    # 다시 공백으로 연결
    return " ".join(new_words)
```

### 코드 설명
- `capitalize()`: 첫 글자만 대문자로, 나머지는 소문자로 바꿉니다. 숫자로 시작하면 숫자 그대로, 뒤는 소문자로 바꿉니다. 문제 요구사항("3people")에 딱 맞습니다.
- `split(' ')`: 인자를 주지 않은 `split()`은 공백을 모두 제거하지만, `' '`를 주면 공백 하나하나를 구분자로 인식해 보존합니다.
