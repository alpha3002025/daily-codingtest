from collections import defaultdict

# 1. defaultdict 생성 (기본값: int -> 0, list -> [])
# 예: 단어 빈도수 세기
word_counts = defaultdict(int)
words = ["apple", "banana", "apple", "cherry", "banana", "banana"]

for word in words:
    word_counts[word] += 1

print("--- 1. items() 순회 ---")
for key, value in word_counts.items():
    print(f"{key}: {value}")

print("\n--- 2. keys() 순회 ---")
for key in word_counts.keys(): # .keys() 생략 가능 (for key in word_counts:)
    print(f"{key}의 개수: {word_counts[key]}")

print("\n--- 3. values() 순회 ---")
for value in word_counts.values():
    print(f"개수: {value}")


# 2. 리스트를 값으로 갖는 defaultdict
# 예: 카테고리별 아이템 묶기
print("\n--- 4. List as value ---")
items_by_category = defaultdict(list)
items = [("Fruit", "Apple"), ("Fruit", "Banana"), ("Veggie", "Carrot")]

for category, item in items:
    items_by_category[category].append(item)

for category, item_list in items_by_category.items():
    print(f"Category [{category}]: {item_list}")

"""
[출력 결과]
--- 1. items() 순회 ---
apple: 2
banana: 3
cherry: 1

--- 2. keys() 순회 ---
apple의 개수: 2
banana의 개수: 3
cherry의 개수: 1

--- 3. values() 순회 ---
개수: 2
개수: 3
개수: 1

--- 4. List as value ---
Category [Fruit]: ['Apple', 'Banana']
Category [Veggie]: ['Carrot']
"""
