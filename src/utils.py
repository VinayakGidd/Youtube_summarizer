import re

def clean_text(text):
    text = re.sub(r'n', ' ', text)  # Remove newlines
    text = re.sub(r's+', ' ', text)  # Remove extra spaces
    return text.strip()