import re

def extract_name(line):
    match = re.search(r'^[A-Z][a-z]+\s[A-Z][a-z]*+', line)
    if match:
        return match.group(0)
    return None

with open('regex_test.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(extract_name(line.strip()))