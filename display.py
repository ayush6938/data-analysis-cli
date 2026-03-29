from utils import get_valid_number
from logic import rank_datasets
from logic import overall_insight

def display_all_results(results):
    for i, result in enumerate(results):
        print(result.to_report_string(i))
    
def display_filtered(filtered):
    if not filtered:
        print("No datasets found matching criteria")
        return
    for i, result in filtered:
        print(result.to_report_string(i))

def show_ranking(results):
    n = get_valid_number("How many datasets you want to see? ")
    ranked = rank_datasets(results)
    print("\n=== DATASET RANKING ===")
    for i, (index, result) in enumerate(ranked[:n]):
        print(f"{i+1}. Dataset {index+1} - Score: {result.score}")
    
def process_result(results, datasets, best_index):
    display_all_results(results)
    print("\nOverall Insight:")
    print(overall_insight(results))
    print(f"\nTotal Datasets loaded : {len(datasets)}")
    print(f"\nDataset {best_index+1} is best")
    print("\nReport saved as report.txt")

def view_report():
    try:
        with open("report.txt", "r") as file:
            data = file.read()
            print("\n REPORT:\n")
            print(data)
    except FileNotFoundError:
        print("X Report file not found")