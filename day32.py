class Result:
    def __init__(self, score, high, low):
        self.score = score
        self.high = high
        self.low = low
    
    def summary(self):
        return f"score: {self.score}, High: {len(self.high)}, Low {len(self.low)}"
    
    def is_good(self, min_score):
        return self.score >= min_score
    
    def is_perfect(self):
        return len(self.high) == 0 and len(self.low) == 0

    def display(self, index):
        print(f"\nDataset {index+1}")
        print(self.summary())

    def grade(self):
        if self.score >= 90:
            return "A"
        elif self.score >= 75:
            return "B"
        else:
            return "C"    
        
    def has_issues(self):
        return len(self.high) > 0 or len(self.low) > 0
    
        
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
    return Result(score, high_outliers, low_outliers)


def process_dataset(label):
    numbers = collect_numbers(label)
    result = analyze_data(numbers)
    return result

def display_all_results(results):
    for i, result in enumerate(results):
        result.display(i)
        if result.is_perfect():
            print("Perfect dataset")
        print(f"Grade: {result.grade()}")
        if result.has_issues():
            print("Needs attention")

def find_best(results):
    best_index = 0
    for i in range(1, len(results)):
        if results[i].score > results[best_index].score:
            best_index = i
    return best_index

def generate_report(results, best_index):
    with open("report.txt", "w") as file:
        file.write("DATA ANALYSIS REPORT\n")
        file.write("__________\n\n")
        for i, result in enumerate(results):
            file.write(f"\nDataset {i+1} Score: {result.score}")
            file.write(f"\nHigh outliers: {len(result.high)}\n")
            file.write(f"Low Outliers: {len(result.low)}\n\n")
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
        if result.is_good(min_score):
            filtered.append((i, result))
    return filtered

def display_filtered(filtered):
    if not filtered:
        print("No datasets found matching criteria")
        return
    for i, result in filtered:
        result.display(i)

def rank_datasets(results):
    ranked = sorted(enumerate(results), key = lambda x: x[1].score)
    return ranked

def save_results(results):
    with open("results.txt", "w") as file:
        for result in results:
            line = (f"{result.score} | {len(result.high)} | {len(result.low)}\n")
            file.write(line)

def load_resluts():
    results = []
    try:
        with open("results.txt", "r") as file:
            for line in file:
                score, high, low = map(int, line.strip().split("|"))
                result = Result(score, [0]* high, [0]* low)
                results.append(result)
    except FileNotFoundError:
        print("No saved results found")
    return results

def generate_results(datasets):
    results = []
    for numbers in datasets:
        results.append(analyze_data(numbers))
    return results

def show_ranking(results):
    n = get_valid_number("How many datasets you want to see? ")
    ranked = rank_datasets(results)
    print("\n=== DATASET RANKING ===")
    for i, (index, result) in enumerate(ranked[:n]):
        print(f"{i+1}. Dataset {index+1} - Score: {result.score}")


def main():
    datasets = read_database_from_file()
    if not datasets:
        print("No Dataset found")
        return
    results = generate_results(datasets)
    display_all_results(results)
    best_index = find_best(results)
    generate_report(results, best_index)
    save_results(results)
    print(f"\nTotal Datasets loaded : {len(datasets)}")
    print(f"\nDataset {best_index+1} is best")
    print("\nReport saved as report.txt")

def run_system():
    datasets = read_database_from_file()
    while True:
        print("\n___MENU___")
        print("1. Run analysis")
        print("2. Exit")
        print("3. View Report")
        print("4. Filter Datasets by Score")
        print("5. Filter Datasets by zero low")
        print("6. Show Ranking")
        print("7. Load Previous results")
        print("8. Load Previous results + Show Ranking directly")
        print("9. Data Refresh")
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
            if not datasets:
                print("No data available")
                continue
            results = generate_results(datasets)
            filtered = filter_datasets(results, min_score)
            display_filtered(filtered)
        elif choice == '5':
            if not datasets:
                print("No data available")
            results = generate_results(datasets)
            lz =[]
            for i, result in enumerate(results):
                if len(result.low) == 0:
                    lz.append((i, result))
            if not lz:
                print("No dataset with zero low outliers")
            for y, n in lz:
                print(f"Dataset : {y+1} has no low outliers.")
        elif choice == '6':
            if not datasets:
                print("No data available")
                continue
            results = generate_results(datasets)
            show_ranking(results)
        elif choice == '7':
            results = load_resluts()
            if not results:
                print("No previous results")
            else:
                display_all_results(results)
        elif choice == '8':
            results = load_resluts()
            if not results:
                print("No previous results")
            else:
                display_all_results(results)
                show_ranking(results)
        elif choice == '9':
            datasets = read_database_from_file()
            print("Data Refreshed!")
        else:
            print("Invalid choice")

run_system()






