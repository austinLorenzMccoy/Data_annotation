# Toxicity & Bias Detection Project

## Setup Instructions

1. Start the Doccano container:
```bash
docker compose up -d
```

2. Access Doccano:
- URL: http://localhost:8002
- Username: admin
- Password: password

3. Project Configuration:
- Project Type: Multi-label Classification
- Enable overlapping: Yes
- Import labels from: config/labels.json
- Import data from: data/toxic_bias_data.jsonl

## Annotation Guidelines

### Toxicity Labels
- Toxic: Harmful, offensive, or aggressive content
- Non-toxic: Neutral or positive content

### Bias Types
- Gender Bias: Prejudice based on gender
- Racial Bias: Discrimination based on race/ethnicity
- Religious Bias: Prejudice against religious beliefs

### Annotation Process
1. Read the text carefully
2. Apply Toxicity label (required)
3. Apply Bias type labels (if applicable)
4. Document unclear cases