import json
import pandas as pd
from pathlib import Path

def import_to_doccano(input_file: str, output_file: str):
    """
    Convert data to Doccano import format
    """
    df = pd.read_csv(input_file)
    doccano_format = []
    
    for _, row in df.iterrows():
        item = {
            "text": row['medical_text'],
            "labels": [],
            "metadata": {}
        }
        doccano_format.append(item)
    
    with open(output_file, 'w') as f:
        json.dump(doccano_format, f, indent=2)

def export_from_doccano(input_file: str, output_file: str):
    """
    Convert Doccano export format to structured data
    """
    with open(input_file, 'r') as f:
        annotations = json.load(f)
    
    structured_data = []
    for ann in annotations:
        item = {
            "text": ann['text'],
            "annotations": ann['labels'],
            "metadata": ann.get('metadata', {})
        }
        structured_data.append(item)
    
    pd.DataFrame(structured_data).to_csv(output_file, index=False)