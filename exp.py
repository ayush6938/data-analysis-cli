numbers = "10 20 30"
result = map(int, numbers.split())
print(result)
for rank, (i, result) in enumerate(ranked, start = 1):
        print(f"{rank}. Dataset {i+1} - Score: {result['score']}")

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

            return (f"\nDataset {index+1}\n" f"{self.summary()}\n" f"{self.status()}\n" f"Grade: {self.grade()}\n" f"Risk Level: {self.risk_level()}\n")
    def grade(self):
        if self.score >= GRADE_THRESHOLDS["A"]:
            return "A"
        elif self.score >= GRADE_THRESHOLDS["B"]:
            return "B"
        else:
            return "C"