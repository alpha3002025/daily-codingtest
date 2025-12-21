# 신고 결과 받기

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/92334)

유저들이 서로를 신고합니다.
- 한 유저가 같은 유저를 여러 번 신고해도 1회로 처리됩니다.
- `k`번 이상 신고된 유저는 정지되며, 그를 신고한 모든 유저에게 메일이 발송됩니다.
각 유저가 받은 처리 결과 메일의 개수를 순서대로 반환하세요.

## 해결 전략
데이터의 흐름을 잘 파악해야 합니다.
1. **누가 누구를 신고했는지** (중복 제거)
2. **각 유저가 몇 번 신고당했는지** (정지 기준 판단용)
3. **각 유저가 받을 메일 수** (결과)

### 알고리즘 순서
1. `report`의 중복을 제거합니다 (`set`).
2. `reported_count` 딕셔너리(신고당한 횟수)를 만듭니다.
    - `report`를 순회하며 `target`의 카운트를 증가 (`split` 사용).
3. `user_report_logs` 딕셔너리(유저별 신고한 사람 목록)를 만듭니다(또는 `report` 세트를 다시 순회해도 됨).
    - `reporter` -> `list of targets`
4. `id_list` 순서대로 결과 배열을 만듭니다.
    - 해당 유저(`id`)가 신고한 사람들 중, `reported_count >= k`인 사람이 몇 명인지 셉니다.
    - 그 수를 `answer`에 추가.

## Python 코드

```python
def solution(id_list, report, k):
    # 중복 신고 제거
    unique_report = set(report)
    
    # 신고 당한 횟수 저장
    reported_cnt = {id: 0 for id in id_list}
    
    # 누가 누구를 신고했는지 저장 (Reporter -> Targets)
    reporter_logs = {id: [] for id in id_list}
    
    for r in unique_report:
        pusher, target = r.split()
        reported_cnt[target] += 1
        reporter_logs[pusher].append(target)
        
    # 정지된 유저 목록 (최적화를 위해 set으로 관리하거나, 그냥 로직 내에서 판단)
    # 여기서는 각 유저별로 순회하며 확인
    
    answer = []
    for user_id in id_list:
        mail_count = 0
        # 내가 신고한 사람들의 목록
        targets = reporter_logs[user_id]
        
        for t in targets:
            # 그 사람이 정지 기준(k)을 넘었는지 확인
            if reported_cnt[t] >= k:
                mail_count += 1
                
        answer.append(mail_count)
        
    return answer
```

## 배운 점 / 팁
- **Dictionary Key-Value 설계**: "누가 신고했는지"와 "누가 신고 당했는지" 두 가지 관점의 데이터가 모두 필요합니다.
- **Set 활용**: "동일 유저에 대한 신고 횟수는 1회로 처리"라는 조건은 `set(report)` 한 줄로 깔끔하게 해결됩니다.
