numbers = [6, 10, 2]
numbers_str = list(map(str, numbers))
print(f"before = {numbers_str}")
numbers_str.sort(key=lambda x: x*3, reverse=True)
print(f"after = {numbers_str}")

