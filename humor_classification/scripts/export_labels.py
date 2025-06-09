import json
import pandas as pd
from label_studio_sdk import Client

def export_annotations():
    ls = Client(url='http://localhost:8080', api_key='your_api_key')
    project = ls.get_project(id=1)
    
    # Export annotations
    annotations = project.export_annotations()
    
    # Save raw annotations
    with open('../data/processed/annotations_raw.json', 'w') as f:
        json.dump(annotations, f, indent=2)
    
    # Process into DataFrame
    processed_data = []
    for item in annotations:
        text = item['data']['text']
        humor_type = item['annotations'][0]['result'][0]['value']['choices'][0]
        processed_data.append({
            'text': text,
            'humor_type': humor_type
        })
    
    df = pd.DataFrame(processed_data)
    df.to_csv('../data/processed/humor_annotations.csv', index=False)
    print(f"Exported {len(df)} annotations")

if __name__ == "__main__":
    export_annotations()