# Toxicity & Bias Detection Annotation Project

This project provides a Docker-based Doccano setup for multi-label classification of toxic content with bias detection.

## Features

- Multi-label classification of toxic content
- Docker-based Doccano setup for scalable annotation
- Real-time validation checks and quality control
- Support for detecting multiple dimensions of toxicity and bias
- Comprehensive annotation guidelines and training materials

## Technologies Used

- **Doccano**: Primary annotation platform
- **Docker**: Containerization for easy deployment
- **Python**: Backend processing and analysis
- **Pandas**: Data manipulation and statistics
- **scikit-learn**: Inter-annotator agreement metrics

## Annotation Schema

The toxicity and bias annotation schema includes:

1. **Toxicity Categories**:
   - Hate Speech
   - Harassment
   - Profanity
   - Threats
   - Sexual Content
   - Self-Harm
   - Violence

2. **Bias Dimensions**:
   - Gender Bias
   - Racial/Ethnic Bias
   - Religious Bias
   - Age Bias
   - Disability Bias
   - Socioeconomic Bias
   - Political Bias

3. **Severity Levels**:
   - Mild
   - Moderate
   - Severe

## Workflow

1. Content collection and pre-processing
2. Initial toxicity screening
3. Detailed multi-label annotation in Doccano
4. Bias dimension annotation
5. Quality control and agreement calculation
6. Dataset finalization and export

## Docker Setup

The project includes a Docker-based setup that provides:
- Isolated annotation environment
- Multi-user support with role-based access
- Persistent storage for annotations
- Easy deployment across different environments
- Integrated backup and version control
