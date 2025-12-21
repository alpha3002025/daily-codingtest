# 대충 만든 자판

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/160586)

휴대폰 자판(`keymap`)에 여러 문자가 할당되어 있습니다. 하나의 키를 여러 번 눌러 원하는 문자를 입력해야 합니다.
- 예: 1번 키에 "AB" 할당 -> 'A'는 1번 클릭, 'B'는 2번 클릭
`targets` 배열에 있는 각 문자열을 작성하기 위해 필요한 **최소 키 누름 횟수**의 합을 구하세요. 작성 불가능한 경우 `-1`을 반환합니다.

## 해결 전략
어떤 문자를 입력하기 위한 최소 횟수는, 그 문자가 포함된 모든 자판(`keymap`) 중 **가장 앞에 위치한 인덱스 + 1**입니다.

모든 `keymap`을 순회하며 각 알파벳을 치기 위한 최소 횟수를 미리 계산해두면 효율적입니다.

### 알고리즘 순서
1. **최소 클릭 수 저장 (`min_press`)**: 알파벳별 최소 누름 횟수를 저장할 딕셔너리를 만듭니다.
2. `keymap`을 순회하며 `min_press`를 채웁니다.
    - 각 키의 문자열을 순회하며 인덱스(`i`)를 확인.
    - `min_press[char] = min(현재 저장된 값, i + 1)`
3. `targets`의 각 문자열을 순회하며 점수를 계산합니다.
    - 각 문자가 `min_press`에 없다면 작성 불가능 -> `-1` 반환.
    - 있다면 해당 횟수를 더함.
4. 결과 배열 반환.

## Python 코드

```python
def solution(keymap, targets):
    # 각 문자별 최소 누름 횟수 저장
    min_press = {}
    
    for keys in keymap:
        for i, char in enumerate(keys):
            # 기존 값보다 더 적게 눌러도 되면 갱신 (또는 처음이면 저장)
            if char not in min_press:
                min_press[char] = i + 1
            else:
                min_press[char] = min(min_press[char], i + 1)
                
    result = []
    
    for target in targets:
        count = 0
        possible = True
        
        for char in target:
            if char not in min_press:
                possible = False
                break
            count += min_press[char]
            
        if possible:
            result.append(count)
        else:
            result.append(-1)
            
    return result
```

## 배운 점 / 팁
- **전처리(Preprocessing)**: 매번 자판을 뒤지는 것보다, 알파벳별 최소 비용을 미리 한 번만 계산(`keymap` 순회)해두고 사용하는 것이 훨씬 효율적입니다.
- **예외 처리**: 목표 문자열을 아예 만들 수 없는 경우(자판에 없는 문자 포함)를 놓치지 않아야 합니다.
