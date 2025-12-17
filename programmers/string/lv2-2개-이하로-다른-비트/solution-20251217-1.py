def solution(numbers):
    answer = []
    
    # print(f"bin(2) = {bin(2)}") ## "0b10"
    
    for number in numbers:
        if number % 2 == 0:
            ## 짝수는 마지막 비트가 0 이므로 마지막 비트 하나만 1로 바꾸면 된다.
            answer.append(number+1)
        else:
            ## 가장 낮은 자리의 0을 1로 바꾸기 + 그 자리의 오른쪽의 1을 0으로 변경
            bin_str = '0' + bin(number)[2:]
            ## 오른쪽(가장 낮은자리)의 '0' 의 인덱스 찾기
            idx = bin_str.rfind('0')
            
            ## 해당 위치의 index 의 비트는 1로 변경, index+1 의 위치는 0으로 변경
            binary_list = list(bin_str)
            binary_list[idx] = '1'
            binary_list[idx+1] = '0'
            
            ## 정수로 변환
            answer.append(int("".join(binary_list),2))
    
    return answer