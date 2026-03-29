from logic import read_database_from_file
from logic import generate_results, find_best
from logic import generate_report
from display import view_report
from display import process_result
from display import display_all_results
from logic import save_results
from logic import filter_datasets
from display import display_filtered
from display import show_ranking
from utils import get_valid_number
from logic import load_resluts
from config import MIN_SCORE_FILTER
from logic import automation_pipeline
from config_loader import load_config
from result import Result
from logger import log

def main():
    log("System started")
    print("\n Welcome to Data Analysis system")
    config = load_config()
    if config is None:
        print("System cannot without config")
        return
    datasets, results, best_index = automation_pipeline()
    if results is None:
        return
    if results:
        process_result(results, datasets, best_index)
        generate_report(results, best_index)
        save_results(results)
        
def run_system():
    datasets = read_database_from_file()
    while True:
        print("\n========== MENU ==========")
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
        print("10. Run Full Automation")
        print("====================")
        choice = input("Enter choice: ")
        if choice == "1":
            main()
        elif choice == "2":
            print("Exiting System. Thank you!")
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
            min_score = MIN_SCORE_FILTER
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
        elif choice == '10':
            datasets, results, best_index = automation_pipeline()
            if results is None:
                return
            if results:
                process_result(results, datasets, best_index)
                generate_report(results, best_index)
                save_results(results)    
        else:
            print("Invalid choice")

run_system()

