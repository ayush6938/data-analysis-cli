numbers = []
count = int(input("How many numbers: "))
for i in range (count):
    x = int(input("Enter number: "))
    numbers.append(x)
total = sum(numbers)
average = total / len(numbers)
highest = max(numbers)
high_outliers = []
low_outliers = []
for n in numbers:
    if n > average*2:
        high_outliers.append(n)
    if n < average / 2:
        low_outliers.append(n)
print("Numbers: ", numbers)
print("Average: ", average)
print("Highest: ", highest)
lowest = min(numbers)
range_value = highest - lowest
print("Lowest: ", lowest)
print("Range: ", range_value)
if high_outliers:
    print("High outlier detected")
if low_outliers:
    print("Low outlier detected")
print("High outliers: ", high_outliers)
print("Low outliers: ", low_outliers)
total_outliers = len(high_outliers) + len(low_outliers)
if total_outliers > len(numbers) / 2:
    print("DATA STATUS: RISKY")
    print("ACTION: Data is unstable, review needed")
else:
    print("DATA STATUS: NORMAL")
    print("ACTION: Data is stable")
if high_outliers:
    print("ACTION: Reduce impact of high values")
if low_outliers:
    print("ACTION: Improve low values")
if not high_outliers and not low_outliers:
    print("PERFECT DATA: No outliers found")
score = 100
score -=len(high_outliers) * 15
score -= len(low_outliers) * 10
if score < 0:
    score = 0
print("Score: ", score)
if score >= 80:
    print("Grade: EXCELLENT")
elif score >= 50:
    print("Grade: GOOD")
else:
    print("Grade: POOR")    

