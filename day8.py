def read_patterns():
    patterns = []
    file = open("patterns.txt", "r")
    for line in file:
        clean_line = line.strip()
        patterns.append(clean_line)
    file.close()
    return patterns
patterns = read_patterns()
print(patterns)
def count_frequency(patterns):
    frequency = {}
    for pattern in patterns:
        if pattern in frequency:
            frequency[pattern] += 1
        else:
            frequency[pattern] = 1
    return frequency
def find_best_pattern(frequency):
    best_pattern = max(frequency, key = frequency.get)
    return best_pattern
patterns = read_patterns()
frequency = count_frequency(patterns)
print("\nPattern Frequency:")
for pattern in sorted(frequency, key = frequency.get, reverse=True):
    print(pattern, ":", frequency[pattern])
best_pattern = find_best_pattern(frequency)
print("\nMost Common Pattern:", best_pattern)