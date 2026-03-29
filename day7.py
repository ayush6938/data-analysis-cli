def collect_patterns():
    patterns = []
    total = int(input("How many pattern do you want to enter? "))
    for i in range(total):
        data = input("Enter data: ")
        patterns.append(data)
    return patterns
def count_frequency(patterns):
    frequency = {}
    for pattern in patterns:
        if pattern in frequency:
            frequency[pattern] += 1
        else:
            frequency[pattern] = 1
    return frequency
def find_best_pattern(frequency):
    best_pattern = max(frequency, key=frequency.get)
    return best_pattern
patterns = collect_patterns()
frequency = count_frequency(patterns)
print("\nPattern Frequency")
for mango in sorted(frequency, key=frequency.get, reverse=True):
    print(mango, ":", frequency[mango])
best_pattern = find_best_pattern(frequency)
print("\nMost common pattern:", best_pattern)
