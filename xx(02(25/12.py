# exp1
import re
from collections import Counter

def word_frequency(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words)

# exp2
import re


def extract_data(input_file, output_file):
    with open(input_file, 'r') as file:
        content = file.read()
    dates = re.findall(r'\d{1,2}/\d{1,2}/\d{4}', content)
    phones = re.findall(r'\+\d{1,3} \d{1,4}-\d{3}-\d{4}', content)
    emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', content)

    with open(output_file, 'w') as out_file:
        for item in dates + phones + emails:
            out_file.write(item + '\n')

# exp3
def print_last_three_chars(sentence):
    words = sentence.split()
    for word in words:
        print(word[-3:])

# exp4
def analyze_text(text):
    words = re.findall(r'\b\w+\b', text.lower())
    unique_words = set(words)
    print("Унікальні слова:", unique_words)
    print("Загальна кількість слів:", len(words))
    print("Кількість унікальних слів:", len(unique_words))

# exp5
import re


def extract_information(input_string):
    pattern = r'(?P<surname>\w+) (?P<name>\w+), (?P<birth_date>\d{1,2}/\d{1,2}/\d{4}), (?P<email>[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}), (?P<feedback>.+)'
    match = re.match(pattern, input_string)

    if match:
        return match.groupdict()
    return {}
