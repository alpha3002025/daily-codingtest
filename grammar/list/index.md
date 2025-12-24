```python
l = ["A", "E", "I", "O", "U"]

i = l.index("I")
print(i)
```

<br/>
<br/>

# list 의 index() 함수
- `list.index(value)`: 리스트에서 특정 값(`value`)이 처음으로 등장하는 **인덱스(위치)**를 반환합니다.
- 값이 리스트에 없으면 `ValueError`가 발생합니다.

<br/>

### 실행 결과
위 코드의 실행 결과는 **`2`**입니다.
- 리스트 `l`은 `["A", "E", "I", "O", "U"]`입니다.
- "A"는 인덱스 0, "E"는 인덱스 1, **"I"는 인덱스 2**에 위치합니다.
- 따라서 `l.index("I")`는 `2`를 반환합니다.

<br/>
<br/>

## 값이 없을 경우에 대한 처리

**방법 1: 예외 처리**<br/>
```python
# 방법 1: 예외 처리
try:
    i = my_list.index(target)
except ValueError:
    i = -1
```
<br/>
<br/>

**방법 2: 조건문 (리스트를 두 번 훑어서 조금 비효율적일 수 있음)**<br/>
```python
# 방법 2: 조건문 (리스트를 두 번 훑어서 조금 비효율적일 수 있음)
i = my_list.index(target) if target in my_list else -1
```
<br/>
<br/>
