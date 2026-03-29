patterns = []
for i in range(5):
    pattern = input("Enter pattern: ")
    patterns.append(pattern)
frequency = {}
for mango in patterns:
    if mango in frequency:
        frequency[mango] += 1
    else :
        frequency[mango] = 1
most_common = max(frequency, key=frequency.get)
print("Most common pattern:", most_common)
