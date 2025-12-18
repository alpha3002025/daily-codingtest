A = [0,1,2,3,4,5]
## 에러
# s = "".join(A).lstrip("0")
# print(s)

## 정상코드
s = "".join(map(str, A)).lstrip("0")
print(s)