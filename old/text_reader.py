import time

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.02)  # Adjust the delay time (in seconds) as needed

# Replace 'your_file.txt' with the path to your text file
file_path = './intro.txt'

try:
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            print_slow(line)
except FileNotFoundError:
    print(f"File '{file_path}' not found.")