import csv
import json
import os

def convert_csv_to_jsonl():
    # Use absolute paths
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(current_dir, '..', 'data', 'medical_ner_data.csv')
    output_file = os.path.join(current_dir, '..', 'data', 'medical_ner_data.jsonl')
    
    # Create directories if they don't exist
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    with open(input_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        with open(output_file, 'w') as jsonlfile:
            for row in reader:
                json_record = {"text": row['text']}
                jsonlfile.write(json.dumps(json_record) + '\n')

if __name__ == '__main__':
    convert_csv_to_jsonl()