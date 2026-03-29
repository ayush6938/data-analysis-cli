def analyzer_logs():
    frequency = {}
    total_logs = 0
    with open("logs.txt", "r") as file:
        for line in file:
            log = line.strip().lower()
            total_logs += 1
            if log in frequency:
                frequency[log] += 1
            else:
                frequency[log] = 1
    return frequency, total_logs
def save_report(frequency, total_logs):
    with open("report.txt", "w") as report:
        report.write("Log Summary\n")
        report.write("________\n")
        report.write("\nTotal logs:" + str(total_logs))
        report.write("\nUnique log types:" + str(len(frequency)))
        report.write("\n\nFrequency Table\n")
        for log in sorted(frequency, key = frequency.get, reverse = True):
            report.write(log + " : " + str(frequency[log]) + "\n")
        most_common = max(frequency, key = frequency.get)
        report.write("\nMost Common log: " + most_common)
frequency, total_logs = analyzer_logs()
print("\nLog Summary")
print("__________")
print("\nTotal logs: ", total_logs)
print("\nUnique log types: ", len(frequency))
print("\nFrequency Table")
for log in sorted(frequency, key = frequency.get, reverse = True):
    print(log, ":", frequency[log])
most_common = max(frequency, key = frequency.get)
print("\nMost Common log:", most_common)
save_report(frequency, total_logs)