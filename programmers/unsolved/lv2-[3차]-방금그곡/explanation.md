# [3차] 방금그곡
## 참고
**34번 Test Case Fail 증상**<br/>
Test Case 중 34번 Test Case 가 굉장히 더티했는데 Gemini 는 그걸 찾아냈다. Gemini 가 더 무서워졌다...<br/>
<br/>

해결방식<br/>
`B#`과 `E#`도 replace 함수에 포함하여 1글자로 치환되도록 수정했습니다.<br/>
- 변경 전: C#, D#, F#, G#, A#만 치환
- 변경 후: B# -> b, E# -> e 추가

<br/>
<br/>


## 문제 설명
라디오에서 들은 멜로디 `m`이 재생된 음악 중에 있는지 찾는 문제입니다.
- 각 음악은 `시작시간`, `종료시간`, `제목`, `악보` 정보를 가집니다.
- 음악은 재생 시간만큼 반복 재생되거나 잘려서 재생됩니다.
- 조건에 일치하는 음악이 여러 개라면, 재생 시간이 긴 음악 > 먼저 입력된 음악 순으로 선택합니다.
- `C#`, `D#` 등 샵(#)이 붙은 음을 주의해서 처리해야 합니다.

### 핵심 개념
1.  **전처리 (음 치환)**: `C#`, `D#` 등 두 글자짜리 음을 `c`, `d` 등 한 글자로 치환하면 처리가 훨씬 쉬워집니다.
2.  **재생 시간 계산**: `HH:MM` 형식의 시간을 분 단위 정수로 변환하여 실제 재생 분을 구합니다.
3.  **악보 늘리기/자르기**: 원본 악보를 재생 시간만큼 반복(`abc` -> `abcabc...`)하거나 앞부분만 자릅니다.
4.  **부분 문자열 확인**: `m`이 재생된 전체 악보 문자열 안에 포함되는지 확인합니다.

## Python 풀이

```python
def replace_sharp(s):
    # #이 붙은 음을 소문자로 치환하여 1글자로 만듦
    # C# -> c, D# -> d, F# -> f, G# -> g, A# -> a
    # B# -> b, E# -> e (문제 조건에는 없으나 테스트 케이스 34번 등에서 등장함)
    return s.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a').replace('B#', 'b').replace('E#', 'e')

def get_minutes(time_str):
    h, m = map(int, time_str.split(':'))
    return h * 60 + m

def solution(m, musicinfos):
    # 1. 들은 멜로디 치환
    m = replace_sharp(m)
    
    answer = "(None)"
    max_play_time = -1
    
    for info in musicinfos:
        start, end, title, sheet = info.split(',')
        
        # 2. 재생 시간 계산
        play_time = get_minutes(end) - get_minutes(start)
        
        # 3. 악보 정보 치환
        sheet = replace_sharp(sheet)
        
        # 4. 실제 재생된 멜로디 구성
        sheet_len = len(sheet)
        if play_time >= sheet_len:
            # 시간만큼 반복 + 나머지
            full_sheet = sheet * (play_time // sheet_len) + sheet[:play_time % sheet_len]
        else:
            # 시간만큼 자름
            full_sheet = sheet[:play_time]
            
        # 5. 조건 일치 확인
        if m in full_sheet:
            # 재생 시간이 더 긴 경우만 갱신 (같으면 먼저 나온 것 유지해야 하므로 > 사용)
            if play_time > max_play_time:
                max_play_time = play_time
                answer = title
                
    return answer
```

### 코드 설명
- 치환 함수(`replace_sharp`): 문자열 처리를 단순화하는 가장 중요한 단계입니다. `ABC#` 처럼 뒤에 #이 붙으면 길이가 2가 되어 인덱싱이 까다롭습니다.
- 재생된 멜로디(`full_sheet`): 악보 길이보다 재생 시간이 길면 반복하고, 짧으면 자릅니다. `divmod` 로직과 비슷합니다.
- `if m in full_sheet`: 파이썬의 `in` 연산자는 부분 문자열 검사에 매우 효율적입니다.
- 정렬 조건 처리: `play_time > max_play_time`을 사용하여, 재생 시간이 *더 길 때만* 갱신합니다. 재생 시간이 같을 때는 갱신하지 않으므로 자연스럽게 "먼저 입력된 음악"이 유지됩니다.
