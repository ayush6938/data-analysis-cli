numbers = []
count = int(input(" How many numbers do you want to enter: "))
for i in range(count):
    x = int(input("Enter number:"))
    numbers.append(x)
total = 0
for n in numbers:
    total += n
average = total / len(numbers)
print("Numbers", numbers)
print("Total", total)
print("Average", average)
if average >=  80:
    print("Status: HIGH")
elif average >= 50:
    print("Status: MEDIUM")
else:
    print("Status: LOW")
highest = max(numbers)
lowest = min(numbers)
print("Highest: ", highest)
print("Lowest: ", lowest)
print("Range: ", highest - lowest)