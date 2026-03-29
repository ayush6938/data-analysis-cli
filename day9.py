def count_frequency_from_file():
    frequency = {}
    with open("patterns.txt", "r") as file:
        for line in file:
            pattern = line.strip()
            if pattern in frequency:
                frequency[pattern] += 1
            else:
                frequency[pattern] = 1
    return frequency
frequency = count_frequency_from_file()
print("\nFrequency Table:")
for item in sorted (frequency, key = frequency.get, reverse = True):
    print(item, ":", frequency[item])
best_pattern = max(frequency, key = frequency.get)
print("\nMost common Pattern", best_pattern)
