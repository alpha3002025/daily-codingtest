# string 의 find 함수들

파이썬 문자열(`str`) 자료형에서 특정 문자열을 찾을 때 사용하는 함수들입니다.

## 1. `find(sub)` / `rfind(sub)`
찾는 문자열이 없으면 **`-1`을 반환**합니다. (에러가 발생하지 않음)

- **`find(sub)`**: 앞에서부터(왼쪽) 검색하여 처음 발견된 인덱스 반환
- **`rfind(sub)`**: 뒤에서부터(오른쪽) 검색하여 처음 발견된 인덱스 반환

```python
s = "apple application"

print(s.find("app"))   # 0  (맨 앞의 app)
print(s.rfind("app"))  # 6  (application의 app)
print(s.find("banana"))# -1 (없음)
```

<br/>
<br/>

## 2. `index(sub)` / `rindex(sub)`
기능은 `find`와 동일하지만, 찾는 문자열이 없으면 **`ValueError`를 발생**시킵니다.
(`list.index()`와 동작 방식이 유사함)

- **`index(sub)`**: 앞에서부터 검색
- **`rindex(sub)`**: 뒤에서부터 검색

```python
s = "apple application"

print(s.index("app"))  # 0
# print(s.index("banana"))  # ValueError: substring not found
```
