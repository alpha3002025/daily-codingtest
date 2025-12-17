def solution(numbers):
    number_list = list(map(str, numbers))
    number_list.sort(key=lambda x:x*3, reverse=True)
    answer = "".join(number_list)
    ## 이걸 또 숫자로 한번 더 바꿔줘야 한다.
    ## "000" 같은 문자숫자열은 "0"으로 바꿔줘야해서다.
    return str(int(answer))