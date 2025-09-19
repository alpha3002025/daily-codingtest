import sys

S, P = map(int, sys.stdin.readline().strip().split())
secret_string = list(sys.stdin.readline().strip())

dna_counts = list(map(int, sys.stdin.readline().strip().split()))
match_cnt = 0
window = [0]*4 

def window_plus(c):
    global dna_counts, match_cnt, window

    if c == 'A':
        window[0]+=1
        if window[0] == dna_counts[0]:
            match_cnt+=1
    elif c == 'C':
        window[1]+=1
        if window[1] == dna_counts[1]:
            match_cnt+=1
    elif c == 'G':
        window[2]+=1
        if window[2] == dna_counts[2]:
            match_cnt+=1
    elif c == 'T':
        window[3]+=1
        if window[3] == dna_counts[3]:
            match_cnt+=1

def window_minus(c):
    global dna_counts, match_cnt, window

    if c == 'A':
        if window[0] == dna_counts[0]:
            match_cnt-=1
        window[0]-=1
    elif c == 'C':
        if window[1] == dna_counts[1]:
            match_cnt-=1
        window[1]-=1
    elif c == 'G':
        if window[2] == dna_counts[2]:
            match_cnt-=1
        window[2]-=1
    elif c == 'T':
        if window[3] == dna_counts[3]:
            match_cnt-=1
        window[3]-=1

result = 0

for i in range(4):
    if dna_counts[i] == 0:
        match_cnt+=1

for i in range(P):
    window_plus(secret_string[i])

if match_cnt == 4:
    result += 1

for i in range(P, S):
    j = i - P ## e.g. S=9, P=5 =>  j = 0,1,2,3
              ##                   i = 5,6,7,8
    window_plus(secret_string[i]) # + 카운트 (오른쪽 이동(i(5,6,7,8)의 이동))
    window_minus(secret_string[j]) # - 카운트 (잔여 카운트 원상복구(j(0,1,2,3)의 이동))
    if match_cnt == 4:
        result += 1

print(result)
