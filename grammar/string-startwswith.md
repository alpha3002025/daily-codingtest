# `startswith`
- **`str.startswith(prefix)`**: 문자열이 특정 접두사(`prefix`)로 시작하는지 (`True`/`False`) 확인합니다.
- **특징**:
  - 대소문자를 구분합니다.
  - 인자로 **튜플**을 넘기면 여러 접두사 중 하나라도 일치하면 `True`를 반환합니다.
- **예시**:
```python
s = "Hello World"
print(s.startswith("He"))      # True
print(s.startswith("world"))   # False
print(s.startswith(("Hi", "He"))) # True (Hi 또는 He로 시작하는가?)

