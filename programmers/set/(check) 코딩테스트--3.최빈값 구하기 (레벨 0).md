
#programmers-lv0 

# Link
https://school.programmers.co.kr/learn/courses/30/lessons/120812



# python (my)
```python
from collections import Counter
def solution(array):
    counter = Counter(array)
    
    result = sorted(counter.items(), key = lambda x:x[1], reverse=True)
    
    answer = result[0][0]
    if len(result) > 1 and result[0][1] == result[1][1]:
        answer = -1
    
    return answer
```
<br/>

# python (my (50%))
```python
from collections import Counter

def solution(array):
    counter = Counter(array)
    occurence = set()
    
    most_frequent = 0
    for key,value in counter.items():
        if key in occurence:
            return -1
        occurence.add(value)
    
    return sorted(counter.items(), key=lambda x:x[1], reverse=True)[0][0]
```
<br/>

# python (claude)

```python
from collections import Counter

def solution(array):
    counter = Counter(array)
    
    # 최빈값들을 빈도순으로 정렬
    # most_common = counter.most_common()
    most_common = sorted(counter.items(), key=lambda x:x[1], reverse=True)
    
    # 최빈값이 여러 개인지 확인
    if len(most_common) > 1 and most_common[0][1] == most_common[1][1]:
        return -1
    
    return most_common[0][0]
```
<br/>





