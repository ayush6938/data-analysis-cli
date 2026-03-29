score = int(input("Enter risk score:"))
print("Analyzing...")
if score >= 80:
    print("HIGH RISK")
elif score >= 50:
    print("MEDIUM RISK")
else:
    print("LOW RISK")
