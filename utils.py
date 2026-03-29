def get_valid_number(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("X Please enter a valid number.")

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