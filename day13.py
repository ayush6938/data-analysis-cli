numbers = []
for i in range (5):
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
if average >=  80:
    print("Insight: Strong Performance")
elif average >= 50:
    print("Insight: Moderate Performance")
else:
    print("Insight: Needs improvement")