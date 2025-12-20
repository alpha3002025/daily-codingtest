## 참고 문법: `math.isqrt(n)`
> 문제 : lv2. 점 찍기

<br/>

- **기능**: 양의 정수 `n`의 **정수 제곱근(Integer Square Root)**을 반환합니다.
- **수식**: $\lfloor \sqrt{n} \rfloor$ (제곱근을 내림한 정수 값)
- **특징**: `math.sqrt()`는 부동소수점(`float`)을 반환하지만, `isqrt`는 정확한 `int`값을 반환하므로 **큰 정수 연산**에서 오차 없이 안전합니다. (Python 3.8+)
- **예시**:
    ```python
    import math
    print(math.isqrt(10)) # 3 (3*3=9 <= 10)
    print(math.isqrt(16)) # 4
    ```
