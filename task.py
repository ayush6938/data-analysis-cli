def collect_numbers() :
    numbers = []
    total = int(input("How many numbers you want to enter: "))
    for i in range(total):
        apple = int(input("Send Numbers: "))
        numbers.append(apple)
    return numbers
def count_frequency(numbers):
    frequency = {}
    for lid in numbers:
        if lid in frequency:
            frequency[lid] += 1
        else:
            frequency[lid] = 1
    return frequency
def find_best_pattern(frequency):
    best_pattern = max(frequency, key=frequency.get)
    return best_pattern
numbers = collect_numbers()
frequency = count_frequency(numbers)
print("\nTotal numbers entered: ", len(numbers))
print("Unique numbers: ", len(frequency))
print("\nFrequency Table:")
for pattern in frequency:
    print(pattern, ":", frequency[pattern])
print("\nTop numbers: ")
order = sorted(frequency, key = frequency.get, reverse=True)
for mango in order[:2]:
    print(mango, ":", frequency[mango])
best_pattern = find_best_pattern(frequency)
print("\nMost commom pattern", best_pattern)