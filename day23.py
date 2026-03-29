def get_valid_number(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input! Please enter a number.")

def collect_numbers(label):
    print(f"\n__ {label} ____")
    numbers = []
    while True:
            count = get_valid_number("How many numbers: ")
            if count > 0:
                break
            print("Invalid input, Please enter a valid integer")
    for i in range(count):
        x = get_valid_number("Enter number: ")
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
    return {'score' : score, 'high' : high_outliers, 'low' : low_outliers}

def compare_scores(result1, result2):
    if result1['score'] > result2['score']:
        return("Dataset 1 is better")
    elif result2['score'] > result1['score']:
        return("Dataset 2 is better")
    else:
        return("Both are equal")

def generate_report(result1, result2):
    with open("report.txt", "w") as file:
        file.write("DATA ANALYSIS REPORT\n")
        file.write("__________\n\n")
        file.write(f"Dataset 1 Score: {result1['score']}\n")
        file.write(f"High outliers: {len(result1['high'])}\n")
        file.write(f"Low Outliers: {len(result1['low'])}\n\n")
        file.write("____________________\n")
        file.write(f"Dataset 2 Score: {result2['score']}\n")
        file.write(f"High Outliers: {len(result2['high'])}\n")
        file.write(f"Low Outliers: {len(result2['low'])}\n\n")
        if result1["score"] > result2["score"]:
            file.write("Result: Dataset 1 is better\n")
        elif result2["score"] > result1["score"]:
            file.write("Result: Dataset 2 is better\n")
        else:
            file.write:("Result: Both are equal\n")

def view_report():
    try:
        with open("report.txt", "r") as file:
            data = file.read()
            print("\n REPORT:\n")
            print(data)
    except:
        print("No report found. Run analysis first")

def main():
    numbers1 = collect_numbers("Dataset 1")
    numbers2 = collect_numbers("Dataset 2")
    result1 = analyze_data(numbers1)
    result2 = analyze_data(numbers2)
    print(f"Dataset 1 - High: {len(result1['high'])}, Low: {len(result1['low'])}")
    print(f"Dataset 2 - High: {len(result2['high'])}, Low: {len(result2['low'])}")
    print(f"\nDataset 1 Score: {result1['score']}")
    print(f"\nDataset 2 Score: {result2['score']}")
    result = compare_scores(result1, result2)
    print(result)
    generate_report(result1, result2)
    print("\nReport saved as report.txt")


def run_system():
    while True:
        print("\n___MENU___")
        print("1. Run analysis")
        print("2. Exit")
        print("3. View Report")
        choice = input("Enter choice: ")
        if choice == "1":
            main()
        elif choice == "2":
            print("Exiting program....")
            break
        elif choice == "3":
            view = input("Do you want to view report now ? (y/n)")
            if view == "y":
                view_report()
            elif view == "n":
                print("Okay")
            else:
                print("Invalid input")
        else:
            print("Invalid choice")
run_system()






