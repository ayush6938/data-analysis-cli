from result import Result
from config import HIGH_PENALTY, LOW_PENALTY
from logger import log

def process_dataset(label):
    numbers = collect_numbers(label)
    result = analyze_data(numbers)
    return result

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
    score -= len(high_outliers) * HIGH_PENALTY
    score -= len(low_outliers) * LOW_PENALTY
    if score < 0:
        score = 0
    return Result(score, high_outliers, low_outliers)

def generate_results(datasets):
    results = []
    for numbers in datasets:
        results.append(analyze_data(numbers))
    return results

def find_best(results):
    best_index = 0
    for i in range(1, len(results)):
        if results[i].score > results[best_index].score:
            best_index = i
    return best_index

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
    except ValueError:
        print("X Invalid data in file")
    return datasets

def filter_datasets(results, min_score):
    filtered = []
    for i, result in enumerate(results):
        if result.is_good(min_score):
            filtered.append((i, result))
    return filtered

def rank_datasets(results):
    ranked = sorted(enumerate(results), key = lambda x: x[1].score)
    return ranked

def save_results(results):
    with open("results.txt", "w") as file:
        for result in results:
            line = (f"{result.score} | {result.high_count()} | {result.low_count()}\n")
            file.write(line)

def load_resluts():
    results = []
    try:
        with open("results.txt", "r") as file:
            for line in file:
                score, high, low = map(int, line.strip().split("|"))
                result = Result(score, [0]* high, [0]* low)
                results.append(result)
    except ValueError:
        print("X Corrupted data in results file")
    except FileNotFoundError:
        print("No saved results found")
    return results

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

def run_analysis():
    log("Analysis startrd")
    datasets = read_database_from_file()
    if not datasets:
        print("No datasets available")
        return None, None, None
    results = generate_results(datasets)
    best_index = find_best(results)
    log("Analysis completed")
    return datasets, results, best_index

def automation_pipeline():
    datasets, results, best_index = run_analysis()
    if not results:
        print("No data to process")
        return
    return datasets, results, best_index

def overall_insight(results):
    avg_score = sum(r.score for r in results) / len(results)
    if avg_score >= 90:
        return "Overall system performance is strong."
    elif avg_score >= 75:
        return "System performance is moderate."
    elif avg_score >= 50:
        return "Warning: Critical datasets detected"
    else:
        "System needs improvement."


def generate_report(results, best_index):
    with open("report.txt", "w") as file:
        file.write("===DATA ANALYSIS REPORT===\n")
        file.write("__________\n\n")
        for i, result in enumerate(results):
            file.write(result.to_report_string(i))
            file.write("\n===SUMMARY===\n")
            file.write(f"Total datasets: {len(results)}\n")
            file.write(f"Best sataset: {best_index+1}\n")