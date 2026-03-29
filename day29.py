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

def process_dataset(label):
    numbers = collect_numbers(label)
    result = analyze_data(numbers)
    return result

def display_all_results(results):
    for i, result in enumerate(results):
        print(f"\nDataset {i+1}")
        print(f"High: {len(result['high'])}, Low: {len(result['low'])}")
        print(f"Score: {result['score']}")

def find_best(results):
    best_index = 0
    for i in range(1, len(results)):
        if results[i]['score'] > results[best_index]['score']:
            best_index = i
    return best_index

def generate_report(results, best_index):
    with open("report.txt", "w") as file:
        file.write("DATA ANALYSIS REPORT\n")
        file.write("__________\n\n")
        for i, result in enumerate(results):
            file.write(f"\nDataset {i+1} Score: {result['score']}")
            file.write(f"\nHigh outliers: {len(result['high'])}\n")
            file.write(f"Low Outliers: {len(result['low'])}\n\n")
        file.write(f"\nDataset {best_index+1} is best\n")

def view_report():
    try:
        with open("report.txt", "r") as file:
            data = file.read()
            print("\n REPORT:\n")
            print(data)
    except:
        print("No report found. Run analysis first")

def read_database_from_file():
    datasets = []
    try:
        with open("data.txt", "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                try: 
                    numbers = list(map(int, line.split()))
                    datasets.append(numbers)
                except ValueError:
                    print(f"Skipping invalid line: {line}")
    except FileNotFoundError:
        print("Error: data.txt file not found")
        print("No data available. Please add data.txt")
    return datasets

def filter_datasets(results, min_score):
    filtered = []
    for i, result in enumerate(results):
        if result["score"] >= min_score:
            filtered.append((i, result))
    return filtered

def display_filtered(filtered):
    if not filtered:
        print("No datasets found matching criteria")
        return
    for i, result in filtered:
        print(f"\nDataset {i+1}")
        print(f"Score: {result['score']}")
        print(f"High: {len(result['high'])}, Low: {len(result['low'])}")

def rank_datasets(results):
    ranked = sorted(enumerate(results), key = lambda x: x[1]["score"])
    return ranked

def main():
    datasets = read_database_from_file()
    if not datasets:
        print("No Dataset found")
        return
    results = []
    for numbers in datasets:
        result = analyze_data(numbers)
        results.append(result)
    display_all_results(results)
    best_index = find_best(results)
    generate_report(results, best_index)
    print(f"\nTotal Datasets loaded : {len(datasets)}")
    print(f"\nDataset {best_index+1} is best")
    print("\nReport saved as report.txt")

def run_system():
    while True:
        print("\n___MENU___")
        print("1. Run analysis")
        print("2. Exit")
        print("3. View Report")
        print("4. Filter Datasets by Score")
        print("5. Filter Datasets by zero low")
        print("6. Show Ranking")
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
        elif choice == '4':
            min_score = get_valid_number("Enter minimum score: ")
            datasets = read_database_from_file()
            if not datasets:
                print("No data available")
                continue
            results = []
            for numbers in datasets:
                results.append(analyze_data(numbers))

            filtered = filter_datasets(results, min_score)
            display_filtered(filtered)
        elif choice == '5':
            datasets = read_database_from_file()
            if not datasets:
                print("No data available")
            results = []
            for numbers in datasets:
                results.append(analyze_data(numbers))
            lz =[]
            for i, result in enumerate(results):
                if len(result["low"]) == 0:
                    lz.append((i, result))
            if not lz:
                print("No dataset with zero low outliers")
            for y, n in lz:
                print(f"Dataset : {y+1} has no low outliers.")
        elif choice == '6':
            datasets = read_database_from_file()
            if not datasets:
                print("No data available")
                continue
            results = []
            for numbers in datasets:
                results.append(analyze_data(numbers))
            n = get_valid_number("How many datasets you want to see? ")
            ranked = rank_datasets(results)
            print("\n=== DATASET RANKING ===")
            for i, (index, result) in enumerate(ranked[:n]):
                print(f"{i+1}. Dataset {index+1} - Score: {result['score']}")

        else:
            print("Invalid choice")

run_system()






