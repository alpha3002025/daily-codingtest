# Python 스택과 슬라이싱 가이드

## 1. 스택이 비어있는지 확인하기

### 가장 pythonic한 방법 (권장)
```python
stack = []

if not stack:
    print("스택이 비어있습니다")
else:
    print("스택에 요소가 있습니다")
```

### len() 함수 사용
```python
stack = []

if len(stack) == 0:
    print("스택이 비어있습니다")
else:
    print("스택에 요소가 있습니다")
```

### 실제 사용 예시
```python
stack = []

# 스택에 요소 추가
stack.append(1)
stack.append(2)
stack.append(3)

# 스택이 비어있지 않은 동안 pop
while stack:  # 또는 while len(stack) > 0:
    item = stack.pop()
    print(f"꺼낸 요소: {item}")

if not stack:
    print("모든 요소를 꺼냈습니다. 스택이 비었습니다.")
```

### 권장 사항
**추천하는 방법은 `if not stack:`입니다.** 이 방법이:
- 가장 간결하고 읽기 쉬움
- Python의 관용적인 표현(Pythonic)
- 빈 리스트는 `False`로 평가되는 Python의 특성을 활용

`len(stack) == 0`도 명확하지만, 약간 더 장황합니다.

---

## 2. 음수 인덱스와 슬라이싱

### 기본 예제
```python
array = [1, 2, 3, 4, 5]
#       -5 -4 -3 -2 -1  (음수 인덱스)
#        0  1  2  3  4  (양수 인덱스)

result = array[-4:]
print(result)  # [2, 3, 4, 5]
```

### array[-4:] 설명
- **`-4`**: 뒤에서 4번째 요소 (값 `2`)
- **`:`**: 그 위치부터 끝까지

따라서 인덱스 `-4`(값 2)부터 마지막까지 슬라이싱됩니다.

### 다양한 슬라이싱 예시
```python
array = [1, 2, 3, 4, 5]

print(array[-1])    # 5 (마지막 요소)
print(array[-2])    # 4 (뒤에서 두 번째)
print(array[-3:])   # [3, 4, 5] (뒤에서 3개)
print(array[-4:])   # [2, 3, 4, 5] (뒤에서 4개)
print(array[-5:])   # [1, 2, 3, 4, 5] (전체)
print(array[:-1])   # [1, 2, 3, 4] (마지막 제외)
print(array[:-2])   # [1, 2, 3] (마지막 2개 제외)
```

### 핵심 포인트
음수 인덱스는 뒤에서부터 세는 것이므로, `-4:`는 "뒤에서 4번째부터 끝까지"를 의미합니다!

---

## 추가 참고사항

### 슬라이싱 문법
```python
array[start:end:step]
```
- `start`: 시작 인덱스 (포함)
- `end`: 끝 인덱스 (미포함)
- `step`: 간격 (기본값 1)

### 유용한 슬라이싱 패턴
```python
array = [1, 2, 3, 4, 5]

# 처음 3개
print(array[:3])       # [1, 2, 3]

# 마지막 3개
print(array[-3:])      # [3, 4, 5]

# 역순
print(array[::-1])     # [5, 4, 3, 2, 1]

# 홀수 인덱스만
print(array[1::2])     # [2, 4]

# 짝수 인덱스만
print(array[::2])      # [1, 3, 5]
```
