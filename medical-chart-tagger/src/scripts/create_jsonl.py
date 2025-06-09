import json

def create_sample_dataset():
    """Create sample medical chart entries in JSONL format"""
    samples = [
        {
            "text": "Patient prescribed Metformin 1000mg instead of 100mg. Blood sugar levels elevated.",
            "labels": [[19, 35, "MED"]]  # [start, end, label]
        },
        {
            "text": "Missing vital signs from morning rounds. Patient status unclear.",
            "labels": [[0, 32, "DOC"]]
        },
        {
            "text": "Delayed CT scan order resulting in late diagnosis of appendicitis.",
            "labels": [[0, 18, "PROC"], [33, 47, "DX"]]
        }
    ]
    
    # Write to JSONL file
    output_file = "../data/medical_charts.jsonl"
    with open(output_file, "w") as f:
        for sample in samples:
            f.write(json.dumps(sample) + "\n")

if __name__ == "__main__":
    create_sample_dataset()