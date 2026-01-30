import re
import json

with open("sample_input.txt", "r") as file:
    text = file.read()

patterns = {
    "emails": r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b",
    "urls": r"https?://(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?",
    "phones": r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}",
    "credit_cards": r"\b(?:\d{4}[- ]?){3}\d{4}\b",
    "times": r"\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APap][Mm])?\b",
    "html_tags": r"<\/?[a-zA-Z][^>]*>",
    "hashtags": r"#\w+",
    "currency": r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?"
}

extracted_data = {}

for key, pattern in patterns.items():
    matches = re.findall(pattern, text)
    
    if key == "credit_cards":
        matches = [re.sub(r'(\d{4}[- ]\d{4})[- ]\d{4}[- ]\d{4}', r'\1-****-****', m) for m in matches]
    
    extracted_data[key] = matches

print("=== Extracted Data ===")
print(json.dumps(extracted_data, indent=4))
