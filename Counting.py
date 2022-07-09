numbers = [13, 24, 25, 26, 27, 15, 35, 36, 29, 49, 41, 37, 45, 68, 75, 25, 16]
print(numbers)
n_min = min(numbers)
n_max = max(numbers)
sorted_numbers = {}
for i in range(n_min, n_max + 1):
    sorted_numbers[i] = 0
for k in sorted_numbers:
    sorted_numbers[k] = numbers.count(k)
print(sorted_numbers)
for key in range(14, len(sorted_numbers) + 1):
    sorted_numbers[key] = (sorted_numbers[key] + sorted_numbers[key - 1])
print(sorted_numbers)
sorted_list = []


