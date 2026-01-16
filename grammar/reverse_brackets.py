s1 = "((()))"
s2 = "(()())"
s3 = "()()()()"
s4 = "(()(()))"


table = str.maketrans("()", ")(")
print(s1.translate(table))
print(s2.translate(table))
print(s3.translate(table))
print(s4.translate(table))
