import time

# Replace 'your_file.txt' with the path to your text file
# file_path = './scholar_dialog.py'
file_path = './test_dialog.txt'

def print_slow(text):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.02)  # Adjust the delay time (in seconds) as needed

def create_tree_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            paragraphs = content.split('|')  # Split paragraphs by commas

            print(paragraphs, "\n")
            
            i = 1
            # Create tree nodes for each paragraph
            for paragraph in paragraphs:
                print_slow(paragraph)
            



    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None
    

create_tree_from_file(file_path)
