# string 의 maketrans 함수
**`table = str.maketrans("()", ")(")`**
- 변환 규칙 테이블을 생성합니다.
- 첫 번째 인자의 문자들을 두 번째 인자의 문자들로 1:1 매핑합니다.
- 즉, `(` $\rightarrow$ `)`, `)` $\rightarrow$ `(` 로 매핑됩니다.

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

