def analyze_system():
    error_count = 0
    with open("logs.txt", "r") as file:
        for line in file:
            log = line.strip().lower()
            if log == "error":
                error_count += 1
    return error_count
errors = analyze_system()
print("Total Errors:", errors)
if errors >= 10:
    print("System Ststus : CRITICAL")
elif errors >= 5:
    print("System Status : WARNING")
else:
    print("System Status: Normal")
