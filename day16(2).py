def collect_numbers(label):
    print(f"\n__ {label} ____")
    numbers = []
    count = int(input("How many numbers: "))
    for i in range (count):
        x = int(input("Enter number: "))
        numbers.append(x)
    return numbers

def analyze_data(numbers):
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
    score = 100
    score -= len(high_outliers) * 15
    score -= len(low_outliers) * 10
    if score < 0:
        score = 0
    return score, high_outliers, low_outliers

def compare_scores(score1, score2):
    if score1 > score2:
        return("Dataset 1 is better")
    elif score2 > score1:
        return("Dataset 2 is better")
    else:
        return("Both are equal")

def main():
    numbers1 = collect_numbers("Dataset 1")
    numbers2 = collect_numbers("Dataset 2")
    score1, high1, low1 = analyze_data(numbers1)
    score2, high2, low2 = analyze_data(numbers2)
    print(f"Dataset 1 - High: {len(high1)}, Low: {len(low1)}")
    print(f"Dataset 2 - High: {len(high2)}, Low: {len(low2)}")
    print(f"\nDataset 1 Score:", {score1})
    print(f"\nDataset 2 Score:", {score2})
    result = compare_scores(score1, score2)
    print(result)
    generate_report(score1, score2, high1, low1, high2, low2)
    print("\nReport saved as report.txt")

def generate_report(score1, score2, high1, low1, high2, low2):
    with open("report.txt", "w") as file:
        file.write("DATA ANALYSIS REPORT\n")
        file.write("__________\n\n")
        file.write(f"Dataset 1 Score: {score1}\n")
        file.write(f"High outliers: {len(high1)}\n")
        file.write(f"Low Outliers: {len(low1)}\n\n")
        file.write(f"Dataset 2 Score: {score2}\n")
        file.write(f"High Outliers: {len(high2)}\n")
        file.write(f"Low Outliers:{len(low2)}\n\n")
        if score1 > score2:
            file.write("Result: Dataset 1 is better\n")
        elif score2 > score1:
            file.write("Result: Dataset 2 is better\n")
        else:
            file.write:("Result: Both are equal\n")
main()



