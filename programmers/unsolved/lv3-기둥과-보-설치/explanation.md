# 기둥과 보 설치

## 문제 설명
벽면 구조물(기둥, 보)을 설치하거나 삭제합니다.
규칙:
- **기둥**: 바닥 위에 있거나, 보의 한쪽 끝 위에 있거나, 다른 기둥 위에 있어야 함.
- **보**: 한쪽 끝이 기둥 위에 있거나, 양쪽 끝이 다른 보와 연결되어 있어야 함.
작업 `[x, y, a, b]` (`a`: 0=기둥, 1=보 / `b`: 0=삭제, 1=설치)을 순서대로 수행하고 최종 구조물을 반환하세요.
(유효하지 않은 작업은 무시)

## 문제 해결 전략

$N$은 최대 100, 작업 수는 최대 1000개.
작업 수가 적으므로, **매 작업마다 전체 구조물의 유효성을 검사(O(M))**해도 시간 내에 통과합니다.
복잡하게 부분 업데이트 검사를 하기보다, 일단 설치/삭제해보고 `is_valid()` 함수로 전체를 훑어서 통과되면 유지, 아니면 롤백하는 방식이 구현 실수를 줄이는 최선입니다.

1. **상태 저장**: `set`에 `(x, y, kind)` 튜플 저장.
2. **유효성 검사 함수 `check(frames)`**:
   - 현재 frames에 있는 모든 구조물에 대해 규칙 만족 여부 확인.
   - 하나라도 불만족 시 False.
3. **작업 수행**:
   - 설치: 일단 `add`. `check` 실패하면 `remove`.
   - 삭제: 일단 `remove`. `check` 실패하면 `add`.

## Python 코드

```python
def check(frame):
    for x, y, a in frame:
        if a == 0: # 기둥
            # 조건: 바닥(y=0) or 보의 끝(x-1,y 보 or x,y 보) or 다른 기둥 위(x, y-1 기둥)
            if y == 0 or \
               (x-1, y, 1) in frame or (x, y, 1) in frame or \
               (x, y-1, 0) in frame:
                continue
            return False
        else: # 보
            # 조건: 한쪽 끝이 기둥 위(x, y-1 기둥 or x+1, y-1 기둥) or 양쪽이 보(x-1, y 보 and x+1, y 보)
            if (x, y-1, 0) in frame or (x+1, y-1, 0) in frame or \
               ((x-1, y, 1) in frame and (x+1, y, 1) in frame):
                continue
            return False
    return True

def solution(n, build_frame):
    frame = set()
    
    for x, y, a, b in build_frame:
        item = (x, y, a)
        if b == 1: # 설치
            frame.add(item)
            if not check(frame):
                frame.remove(item)
        else: # 삭제
            frame.remove(item)
            if not check(frame):
                frame.add(item)
                
    return sorted(list(frame))
```
