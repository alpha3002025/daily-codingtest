**`s.translate(table)`**
- 문자열 `s`에 위 `table`의 규칙을 적용하여 반환합니다.
- `replace`를 여러 번 사용하는 것보다 훨씬 효율적이고 간결하게 문자 교체가 가능합니다.

<br/>

참고문제
- lv2 '괄호 변환'

<br/>

e.g.
```python
text = "Hello World"
# H -> h, W -> w 로 변환
table = str.maketrans("HW", "hw")
return s.translate(table)
# "hello world"
```

<br/>
