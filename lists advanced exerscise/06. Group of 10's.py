
numbers = list(map(int, input().split(', ')))

group = 10
while len(numbers) > 0:
    filtered = [x for x in numbers if x <= group]
    numbers = [x for x in numbers if x > group]
    print(f"Group of {group}'s: {filtered}")
    group += 10



