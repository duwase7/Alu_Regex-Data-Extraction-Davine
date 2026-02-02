__version__ = "1.1.0"
import re
import json

def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def mask_credit_cards(card_list):
    masked = []
    for card in card_list:
    
        masked_card = re.sub(r'(\d{4}[- ]\d{4})[- ]\d{4}[- ]\d{4}', r'\1-****-****', card)
        masked.append(masked_card)
    return masked

def extract_data(text, patterns_dict):
    results = {}
    for data_type, regex in patterns_dict.items():
        matches_found = re.findall(regex, text)

        if data_type == "credit_cards":
            matches_found = mask_credit_cards(matches_found)

        results[data_type] = matches_found
    return results

patterns = {
    "emails": r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b",
    "urls": r"https?://(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s.,]*)?",
    "phones": r"\(\d{3}\)\s?\d{3}[-\u2011]\d{4}",
    "credit_cards": r"\b(?:\d{4}[- ]?){3}\d{4}\b",
    "times": r"\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APap][Mm])?\b",
    "html_tags": r"<\/?[a-zA-Z][^>]*>",
    "hashtags": r"#\w+",
    "currency": r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?"
}


if __name__ == "__main__":
    print("Starting data extraction for Inyange Industries input...")
    input_text = load_text("sample_input.txt")
    extracted_results = extract_data(input_text, patterns)

    print("=== Extracted Data from Inyange Industries Text ===")
    print(json.dumps(extracted_results, indent=4)) 
