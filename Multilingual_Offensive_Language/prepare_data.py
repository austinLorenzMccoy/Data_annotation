#!/usr/bin/env python
import os
import json
import pandas as pd
from pathlib import Path

def convert_to_label_studio_format(input_file, output_file):
    """
    Convert raw data to Label Studio compatible format.
    
    Args:
        input_file (str): Path to the input JSON file
        output_file (str): Path to save the converted data
    """
    try:
        # Read the input data
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Convert to Label Studio format
        label_studio_data = []
        for item in data:
            # Create the Label Studio compatible item
            ls_item = {
                "id": item["id"],
                "data": {
                    "text": item["text"],
                    "meta": {
                        "language": item["language"],
                        "translation": item["translation"]
                    }
                }
            }
            label_studio_data.append(ls_item)
        
        # Create the directory if it doesn't exist
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        # Save the converted data
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(label_studio_data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Successfully converted {len(data)} items to Label Studio format")
        print(f"✅ Saved to: {output_file}")
        return True
    
    except Exception as e:
        print(f"❌ Error converting data: {str(e)}")
        return False

def create_csv_version(input_file, output_file):
    """
    Create a CSV version of the data for easier viewing.
    
    Args:
        input_file (str): Path to the input JSON file
        output_file (str): Path to save the CSV file
    """
    try:
        # Read the input data
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Convert to DataFrame
        df = pd.DataFrame(data)
        
        # Create the directory if it doesn't exist
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        # Save as CSV
        df.to_csv(output_file, index=False)
        
        print(f"✅ Created CSV version at: {output_file}")
        return True
    
    except Exception as e:
        print(f"❌ Error creating CSV: {str(e)}")
        return False

def main():
    """Main function to prepare data for Label Studio."""
    print("🔄 Preparing data for Label Studio...")
    
    # Define file paths
    raw_data_path = "data/raw/sample_data.json"
    ls_data_path = "data/imports/sample_data_labelstudio.json"
    csv_data_path = "data/processed/sample_data.csv"
    
    # Check if raw data exists
    if not os.path.exists(raw_data_path):
        print(f"❌ Raw data not found at: {raw_data_path}")
        return
    
    # Convert to Label Studio format
    convert_to_label_studio_format(raw_data_path, ls_data_path)
    
    # Create CSV version
    create_csv_version(raw_data_path, csv_data_path)
    
    print("\n✅ Data preparation complete!")
    print("You can now import the data into Label Studio from:")
    print(f"  {os.path.abspath(ls_data_path)}")

if __name__ == "__main__":
    main()
