 # Data Annotation Projects Collection 🏷️

A comprehensive suite of data annotation projects for medical, toxicity, and multilingual content annotation using Label Studio and custom tagging interfaces.

## Projects Overview 📊

### 1. [Medical Chart Tagger](medical-chart-tagger)
Specialized tool for clinical document annotation:
- Entity Types: Diagnoses, Medications, Procedures, Lab Values
- Relation Types: Has-Indication, Has-Dosage, Has-Duration
- Temporal Expression Tagging
- SNOMED-CT Integration
- HL7/FHIR Compatible Exports

### 2. [Humor Classification](humor_classification)
Multi-category humor content classification:
- Categories: Funny, Not_Funny, Dark_Humor, Offensive
- Python-based data processing
- Conda environment management
- Automated dataset validation

### 3. [Medical NER](medical_NER)
Named Entity Recognition for medical text:
- Entity Types: Disease, Drug, Symptom, Procedure, Anatomy
- Doccano-based annotation interface
- UMLS terminology mapping
- BioMedical ontology integration

### 4. [Toxicity & Bias Detection](toxicity_bias_project)
Multi-label classification of toxic content:
- Labels: Toxic/Non-toxic
- Bias Categories: Gender, Racial, Religious, Political
- Docker-based Doccano setup
- Real-time validation checks

### 5. [Sentiment Analysis](sentiment_project)
Multi-dimensional sentiment classification:
- Primary Labels: Positive, Neutral, Negative
- Emotional Tones: Joyful, Angry, Sad, Sarcastic
- Structured JSON output
- Cross-annotator agreement metrics

### 6. [Multilingual Offensive Language](Multilingual_Offensive_Language)
Cross-lingual offensive content detection:
- Languages: Yoruba-English, Hausa-English, Igbo-English, Pidgin, Hinglish
- Offensive level classification (not offensive, mildly offensive, offensive, very offensive)
- Bias type categorization (gender, racial, religious, political, socioeconomic)
- Target identification (individual, group, other, none)
- Streamlit-based annotation interface with real-time statistics

## Project Structure 📁

```
.
├── medical-chart-tagger/
│   ├── config/
│   ├── templates/
│   ├── data/
│   └── exports/
├── humor_classification/
│   ├── scripts/
│   ├── config/
│   └── data/
├── medical_NER/
│   ├── doccano/
│   └── data/
├── toxicity_bias_project/
│   ├── docker-compose.yml
│   └── config/
├── sentiment_project/
│   └── labeled_output/
├── Multilingual_Offensive_Language/
│   ├── app.py            # Streamlit annotation interface
│   ├── prepare_data.py   # Data preparation utilities
│   ├── run_app.sh        # Script to launch the annotation tool
│   ├── configs/          # Annotation configuration
│   ├── data/             # Raw and processed data
│   └── exports/          # Annotation exports
└── requirements.txt
```

## Setup Instructions 🛠️

1. **Environment Setup**
````bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # For Mac/Linux

# Install dependencies
pip install -r requirements.txt
```

2. **Docker Setup** (for Doccano projects)
```bash
# Start Doccano instance
docker-compose up -d
```

3. **Annotation Tools**
```bash
# For Label Studio projects
label-studio start

# For Streamlit projects (e.g., Multilingual Offensive Language)
cd Multilingual_Offensive_Language
./run_app.sh
```
## Key Features ⭐

- **Modular Architecture**: Each project is self-contained with its own configuration
- **Docker Support**: Containerized annotation environments
- **Multiple Annotation Tools**: Label Studio and Doccano integration
- **Rich Guidelines**: Detailed annotation instructions for each project
- **Quality Control**: Built-in validation and consistency checks
- **Export Capabilities**: Structured data export in multiple formats

## Annotation Guidelines 📝

Each project contains detailed guidelines:
- [Toxicity & Bias Guidelines](toxicity_bias_project/GUIDELINES.md)
- [Medical NER Guidelines](medical_NER/doccano/GUIDELINES.md)
- [Humor Classification Guidelines](humor_classification/config/guidelines.md)
- [Multilingual Guidelines](Multilingual_Offensive_Language/guidelines/annotation_guidelines.md)

## Data Formats 💾

### Input Formats
- CSV files for structured data
- JSONL for annotation imports
- Plain text for raw content

### Output Formats
- JSON for completed annotations
- JSONL for sequential data
- CSV for analysis-ready datasets

## Tools & Technologies 🔧

- **Label Studio**: Web-based annotation interface for several projects
- **Streamlit**: Interactive annotation interface for Multilingual Offensive Language
- **Doccano**: Specialized NER annotation
- **Python**: Data processing and validation
- **Docker**: Container management
- **Conda/Pip**: Environment management

## Quality Control ✔️

- Inter-annotator agreement metrics
- Validation scripts for data consistency
- Guidelines for edge cases
- Regular review processes

## Contributing 🤝

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments 🙏

- Label Studio team for the annotation platform
- Doccano project for NER capabilities
- Contributors and annotators

## Contact 📧

For questions or support, please open an issue in the repository.

## Version History 📈

- v1.0.0: Initial release with core projects
- v1.1.0: Added Multilingual support
- v1.2.0: Enhanced guidelines and validation
- v1.3.0: Migrated Multilingual Offensive Language to Streamlit (June 2025)
- v1.3.1: Improved annotation statistics and UI enhancements