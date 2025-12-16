# 매칭 점수

## 문제 설명
웹페이지의 HTML이 주어집니다.
- **기본 점수**: 검색어(`word`)가 등장한 횟수 (대소문자 무시).
- **외부 링크 수**: 해당 페이지에서 다른 페이지로 걸린 링크 수.
- **링크 점수**: 해당 페이지로 링크를 건 다른 페이지들의 (그 페이지의 기본 점수 / 그 페이지의 외부 링크 수)의 합.
- **매칭 점수**: 기본 점수 + 링크 점수.
매칭 점수가 가장 높은 페이지의 인덱스를 구하세요.

## 문제 해결 전략

**문자열 파싱 (Regex)**이 핵심입니다.
1. `meta` 태그에서 자신의 URL 추출.
2. `a` 태그에서 외부 링크 URL 추출.
3. 본문(`body`)에서 검색어 등장 횟수 카운트 (알파벳이 아닌 문자로 구분됨).
4. 각 페이지별 점수 계산 후 링크 점수 합산.

## Python 코드

```python
import re

def solution(word, pages):
    word = word.lower()
    page_info = {} # url : {index, basic_score, out_links, link_score}
    
    # 1. 파싱
    for i, page in enumerate(pages):
        page_lower = page.lower()
        
        # URL 추출
        url_match = re.search(r'<meta property="og:url" content="(\S+)"', page)
        my_url = url_match.group(1)
        
        # 기본 점수 (단어 단위 매칭)
        # 알파벳이 아닌 문자로 구분 -> [a-z]+ 찾아서 비교
        # 혹은 re.split([^a-z])
        tokens = re.findall(r'[a-z]+', page_lower)
        basic_score = tokens.count(word)
        
        # 외부 링크 추출
        out_links = re.findall(r'<a href="(\S+)"', page)
        
        page_info[my_url] = {
            'index': i,
            'basic': basic_score,
            'out_count': len(out_links),
            'outs': out_links,
            'link_score': 0
        }
        
    # 2. 링크 점수 계산
    for url in page_info:
        data = page_info[url]
        if data['out_count'] > 0:
            score_to_give = data['basic'] / data['out_count']
            for out_url in data['outs']:
                if out_url in page_info:
                    page_info[out_url]['link_score'] += score_to_give
                    
    # 3. 최대 점수 찾기
    result = []
    for url in page_info:
        data = page_info[url]
        total = data['basic'] + data['link_score']
        result.append((total, data['index']))
        
    # 점수 내림차순, 인덱스 오름차순
    result.sort(key=lambda x: (-x[0], x[1]))
    
    return result[0][1]
```
