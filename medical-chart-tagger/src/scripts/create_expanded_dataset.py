import json
import random

def create_expanded_dataset():
    """Create an expanded medical chart dataset with at least 10 examples"""
    
    samples = [
        {
            "text": "Patient prescribed Metformin 1000mg instead of 100mg. Blood sugar levels elevated.",
            "labels": [[19, 35, "MED"]]
        },
        {
            "text": "Missing vital signs from morning rounds. Patient status unclear.",
            "labels": [[0, 32, "DOC"]]
        },
        {
            "text": "Delayed CT scan order resulting in late diagnosis of appendicitis.",
            "labels": [[0, 18, "PROC"], [33, 47, "DX"]]
        },
        {
            "text": "Nurse administered 50mg of Warfarin instead of 5mg. Patient experiencing severe bleeding.",
            "labels": [[19, 42, "MED"]]
        },
        {
            "text": "No documentation of patient allergies in admission notes. Given penicillin despite allergy.",
            "labels": [[0, 48, "DOC"], [56, 76, "MED"]]
        },
        {
            "text": "X-ray interpreted as normal, missing obvious lung mass. Cancer diagnosis delayed by 6 months.",
            "labels": [[0, 41, "DX"], [43, 74, "DX"]]
        },
        {
            "text": "Surgery started on wrong knee due to incorrect site marking.",
            "labels": [[0, 52, "PROC"]]
        },
        {
            "text": "Patient chart mixed up with another patient. Labs ordered for wrong person.",
            "labels": [[0, 41, "DOC"], [42, 68, "PROC"]]
        },
        {
            "text": "Insulin dose calculated incorrectly, resulting in severe hypoglycemia.",
            "labels": [[0, 32, "MED"]]
        },
        {
            "text": "Missing follow-up documentation for post-operative care. Patient developed infection.",
            "labels": [[0, 47, "DOC"], [48, 71, "PROC"]]
        }
    ]
    
    # Write to JSONL file
    output_file = "../data/expanded_medical_charts.jsonl"
    with open(output_file, "w") as f:
        for sample in samples:
            f.write(json.dumps(sample) + "\n")

if __name__ == "__main__":
    create_expanded_dataset()