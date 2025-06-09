# Medical NER Project

## Overview
Named Entity Recognition project for medical text annotation using Doccano.

## Project Structure
```
medical_NER/
├── doccano/
│   ├── docker-compose.yml
│   ├── convert_to_jsonl.py
│   ├── exports/
│   │   └── annotations.jsonl
│   └── GUIDELINES.md
├── data/
│   ├── medical_ner_data.csv
│   └── medical_ner_data.jsonl
├── config/
│   └── label_config.json
└── README.md
```

## Setup Instructions

1. Start Doccano:
```bash
cd doccano
docker-compose up -d
```

2. Convert data:
```bash
python doccano/convert_to_jsonl.py
```

3. Access Doccano:
- URL: http://localhost:8001
- Username: admin
- Password: password

## Entity Types
- Disease (red) - Medical conditions and diagnoses
- Drug (blue) - Medications and treatments
- Symptom (orange) - Patient symptoms and signs
- Procedure (green) - Medical procedures and tests
- Anatomy (brown) - Body parts and regions

## Data Format
- Input: CSV with medical texts
- Output: JSONL with NER annotations

## Usage
1. Log into Doccano
2. Create new project
3. Import data from medical_ner_data.jsonl
4. Configure labels from label_config.json
5. Start annotation following GUIDELINES.md