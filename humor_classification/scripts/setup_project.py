import os
import json
from label_studio_sdk import Client

def setup_project():
    # Initialize Label Studio client
    ls = Client(url='http://localhost:8080', api_key='your_api_key')
    
    # Create project
    project = ls.create_project(
        title='Humor Classification',
        description='Classify text based on humor type'
    )
    
    # Load label config
    with open('../config/label_config.xml', 'r') as f:
        label_config = f.read()
    project.set_label_config(label_config)
    
    # Import data
    data_path = '../data/raw/jokes.jsonl'
    project.import_tasks(data_path)
    
    print(f"Project created: {project.title}")

if __name__ == "__main__":
    setup_project()