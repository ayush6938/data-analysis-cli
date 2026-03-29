def collect_patterns():
    patterns = []
    for i in range(5):
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
best_pattern = find_best_pattern(frequency)
print("Most common pattern:", best_pattern)
