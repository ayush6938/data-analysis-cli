from config import GRADE_A, GRADE_B
from config import GRADE_THRESHOLDS
from config import INSIGHT_RULES
from config import HIGH_RISK_LIMIT, LOW_RISK_LIMIT
from config import MIN_SCORE_FOR_GOOD
from config_loader import load_config
print("Error happened")
config = load_config()


class Result:
    def __init__(self, score, high, low):
        self.score = score
        self.high = high
        self.low = low
    
    def high_count(self):
        return len(self.high)
    
    def low_count(self):
        return len(self.low)
    
    def summary(self):
        return f"score: {self.score}, High: {self.high_count()}, Low {self.low_count()}"
    
    def is_good(self, min_score):
        return self.score >= min_score
    
    def is_perfect(self):
        return self.high_count() == 0 and self.low_count() == 0

    def has_issues(self):
        return self.high_count() > 0 or self.low_count() > 0
    
    def status(self):
        if self.is_perfect():
            return "Perfect dataset"
        elif self.has_issues():
            return "Needs attention"
        else:
            return "Normal"
    
    def to_report_string(self, index):
        return (f"\n==========Dataset {index+1}==========\n" f"{self.summary()}\n" f"{self.status()}\n" f"Grade: {self.grade()}\n" f"Risk Level: {self.risk_level()}\n" f"Insight: {self.insight()}\n")

    def display(self, index):
        print(f"\nDataset {index+1}")
        print(self.summary())
        print(self.status())
        print(f"Grade: {self.grade()}")
        print(f"Risk Level - {self.risk_level()}")

    def grade(self):
        grade_theresholds = config["grade_theresholds"]
        if self.score >= grade_theresholds["A"]:
            return "A"
        elif self.score >= grade_theresholds["B"]:
            return "B"
        else:
            return "C"

    def risk_level(self):
        limits = config["risk_limits"]
        if self.high_count() >= limits["high"]:
            return ("High Risk")
        elif self.low_count() >= limits["low"]:
            return ("Low Risk")
        else:
            return ("Stable")

    def insight(self):
        rules = config["insight_rules"]            
        for threshold, message in INSIGHT_RULES:
                if self.score >= threshold:
                    return message
        if self.score >= MIN_SCORE_FOR_GOOD:
            print("This Dataset has passed the minimum score for being good Dataset")
    