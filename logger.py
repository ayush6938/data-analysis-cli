def log(message):
    with open ("logs.txt", "a") as file:
        file.write(message + "\n")
    
def log(message, level="INFO"):
    with open ("logs.txt", "a") as file:
        file.write(f"[{level}] {message}\n")
    