# 베스트앨범

## 문제 설명
장르별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시합니다.
수록 기준:
1. 속한 노래가 많이 재생된 장르를 먼저 수록.
2. 장르 내에서 많이 재생된 노래를 먼저 수록.
3. 재생 횟수가 같으면 고유 번호가 낮은 노래를 먼저 수록.

## 문제 해결 전략

**해시(Hash Map)와 정렬(Sorting)**을 사용합니다.
1. 장르별 총 재생 횟수 계산 (`genre_total`).
2. 장르별 노래 리스트 저장 (`genre_songs`). 노래는 `(plays, id)` 형태.
3. `genre_total`을 기준으로 장르 정렬 (내림차순).
4. 각 장르에 대해 `genre_songs`를 정렬 (재생 횟수 내림차순, ID 오름차순) 후 상위 2개 선택.

## Python 코드

```python
from collections import defaultdict

def solution(genres, plays):
    genre_total = defaultdict(int)
    genre_songs = defaultdict(list)
    
    for i, (g, p) in enumerate(zip(genres, plays)):
        genre_total[g] += p
        genre_songs[g].append((p, i))
        
    # 장르별 정렬 (재생 수 내림차순, ID 오름차순 - 파이썬 sort는 stable하므로 play 내림차순 후 id 오름차순 고려 필요)
    # (-p, i)로 정렬하면 play 내림차순, id 오름차순 한 번에 됨.
    for g in genre_songs:
        genre_songs[g].sort(key=lambda x: (-x[0], x[1]))
        
    # 장르 순서 결정 (총 재생 수 내림차순)
    sorted_genres = sorted(genre_total.keys(), key=lambda g: genre_total[g], reverse=True)
    
    answer = []
    for g in sorted_genres:
        # 상위 2개
        for song in genre_songs[g][:2]:
            answer.append(song[1])
            
    return answer
```
