arr = [1, 2, 3, 2, 4, 5]
seen = set()

for i, num in enumerate(arr):
    if num in seen:
        print(f"First repeating element: {num}, second occurrence index: {i}")
        break
    seen.add(num)
