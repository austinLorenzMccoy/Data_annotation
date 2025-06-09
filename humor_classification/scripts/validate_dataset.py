import pandas as pd
import json

def validate_dataset():
    # Read JSONL file
    jsonl_data = []
    with open('../data/raw/jokes.jsonl', 'r') as f:
        for line in f:
            jsonl_data.append(json.loads(line))
    
    # Read CSV file
    csv_data = pd.read_csv('../data/raw/jokes.csv')
    
    # Validation checks
    print("Dataset Validation Report")
    print("-----------------------")
    
    # Check number of samples
    print(f"Total samples: {len(jsonl_data)}")
    print(f"Samples per format:")
    print(f"- JSONL: {len(jsonl_data)}")
    print(f"- CSV: {len(csv_data)}")
    
    # Check category distribution
    categories = {}
    for item in jsonl_data:
        cat = item['metadata']['category']
        categories[cat] = categories.get(cat, 0) + 1
    
    print("\nCategory distribution:")
    for cat, count in categories.items():
        print(f"- {cat}: {count} samples ({count/len(jsonl_data)*100:.1f}%)")
    
    # Check for duplicates
    texts = [item['text'] for item in jsonl_data]
    duplicates = len(texts) - len(set(texts))
    print(f"\nDuplicate entries: {duplicates}")
    
    # Check for empty or invalid entries
    empty = sum(1 for item in jsonl_data if not item['text'].strip())
    print(f"Empty text entries: {empty}")
    
    print("\nValidation complete!")

if __name__ == "__main__":
    validate_dataset()