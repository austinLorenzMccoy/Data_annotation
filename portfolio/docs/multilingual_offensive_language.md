# Multilingual Offensive Language Annotation Project

This project provides a setup for annotating multilingual offensive language data using Label Studio and Streamlit.

## Features

- Cross-lingual offensive content detection
- Streamlit-based annotation interface with real-time statistics
- Multi-level annotation schema for offensive language classification
- Support for multiple languages including English, Spanish, French, and Arabic
- Real-time annotation statistics and quality metrics
- Export functionality to various formats (CSV, JSON, JSONL)

## Technologies Used

- **Label Studio**: Primary annotation platform
- **Streamlit**: Interactive dashboard and annotation interface
- **Python**: Backend processing and data preparation
- **Pandas**: Data manipulation and analysis
- **Matplotlib/Seaborn**: Visualization of annotation statistics

## Annotation Schema

The annotation schema includes multiple levels:

1. **Offensive Language Detection**: Binary classification (Offensive/Not Offensive)
2. **Offense Type**: Targeted/Untargeted
3. **Target Type**: Individual/Group/Other
4. **Language Identification**: Automatic language detection with manual verification

## Workflow

1. Data collection from various sources
2. Pre-processing and normalization
3. Annotation using the Label Studio interface
4. Quality control and inter-annotator agreement calculation
5. Post-processing and dataset finalization
6. Export to standard formats for model training
