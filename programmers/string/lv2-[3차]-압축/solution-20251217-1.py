def solution(msg):
    # chr(65) == 'A'
    # print(chr(65))
    
    ## 1 ~ 26 까지의 코드로 변환
    dictionary = {chr(65+i): i+1 for i in range(26)}
    # print(f"dictionary = {dictionary}")
    
    answer = []
    w = ""
    idx = 0
    next_code = 27 ## 사전에 없는 단어를 어디부터 추가할지에 대한 index
    
    i=0
    while i < len(msg):
        w = msg[i]
        length = 1
        ## (1) 현재 사전 검색할 단어의 길이 i+length 가 len(msg)를 넘지 않을때
        ## (2) 사전 내에 msg[i:i+length+1] 이 있는지 검사 (e.g. 'KA', 'KAO')
        while i+length < len(msg) and (msg[i:i+length+1] in dictionary):
            length+=1
            w = msg[i:i+length] ## 마지막으로 찾은 단어
        
        answer.append(dictionary[w])
        
        ## 그 다음 단어를 사전에 등록 (문제 설명의 3번절차의 마지막 프로세스)
        if i+length < len(msg):
            c = msg[i+length]
            dictionary[w+c] = next_code
            next_code+=1
        
        i+=length
        
    return answer