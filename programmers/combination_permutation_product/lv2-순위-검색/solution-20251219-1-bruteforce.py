"""
실패한데!!!
"""
from collections import defaultdict

def solution(info, query):
    people = defaultdict(list)
    for id, data in enumerate(info):
        lang, job, level, food, score = data.split()
        person = {
            'lang': lang,
            'job': job,
            'level': level,
            'food': food,
            'score': int(score)
        }
        people[id] = person
    
    answer = []
    
    for querystr in query:
        lang,job,level,food,score = querystr.replace(' and ', ' ').split(' ')
        candidates = []
        for id, person in people.items():
            if (lang in ['-', person['lang']] and
                job in ['-', person['job']] and 
                level in ['-', person['level']] and
                food in ['-', person['food']] and
                person['score'] >= int(score)):
                    candidates.append(id)
        answer.append(len(candidates))
        
    return answer