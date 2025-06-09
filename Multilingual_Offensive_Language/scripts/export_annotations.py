import json
import pandas as pd
from pathlib import Path
from label_studio_sdk import Client

def export_annotations(project_id=1):
    """Export annotations from Label Studio to CSV"""
    
    # Initialize client
    ls = Client(
        url='http://localhost:8080',
        api_key='YOUR_API_KEY'  # Replace with your key
    )
    
    # Get project
    project = ls.get_project(project_id)
    
    # Export annotations
    annotations = project.export_annotations()
    
    # Convert to DataFrame
    df = pd.DataFrame(annotations)
    
    # Create exports directory if it doesn't exist
    export_path = Path('../exports')
    export_path.mkdir(exist_ok=True)
    
    # Save to CSV
    df.to_csv(export_path / 'annotations.csv', index=False)
    print(f"Exported {len(df)} annotations to CSV")

if __name__ == "__main__":
    export_annotations()