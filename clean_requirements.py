
import re

def clean_requirements(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Define a regex pattern to match lines with local file paths
    pattern = re.compile(r'^\s*[\w\-.]+ @ file://')

    with open(file_path, 'w') as file:
        for line in lines:
            if not pattern.match(line):
                file.write(line)

# Path to your requirements.txt file
requirements_path = 'requirements.txt'
clean_requirements(requirements_path)
