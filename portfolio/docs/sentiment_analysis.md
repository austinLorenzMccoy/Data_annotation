# Sentiment Analysis Annotation Project

This project provides tools for multi-dimensional sentiment classification with structured JSON output and cross-annotator agreement metrics using Streamlit.

## Features

- Multi-dimensional sentiment classification
- Emotional tone categorization beyond positive/negative
- Streamlit-based annotation interface
- Cross-annotator agreement metrics
- Structured JSON output for machine learning

## Technologies Used

- **Streamlit**: Interactive annotation interface
- **Python**: Backend processing and analysis
- **Pandas**: Data manipulation and statistics
- **Plotly/Matplotlib**: Visualization of sentiment distributions
- **scikit-learn**: Agreement metrics and basic ML operations

## Annotation Schema

The sentiment analysis annotation schema includes:

1. **Basic Sentiment**:
   - Positive
   - Neutral
   - Negative

2. **Emotional Dimensions**:
   - Joy/Happiness
   - Sadness
   - Anger
   - Fear
   - Surprise
   - Disgust
   - Trust
   - Anticipation

3. **Intensity Levels**:
   - Low
   - Medium
   - High

4. **Target Entity**:
   - Self
   - Others
   - Product/Service
   - Event
   - Concept

## Workflow

1. Text collection and pre-processing
2. Basic sentiment annotation
3. Emotional dimension annotation
4. Intensity and target annotation
5. Cross-annotator agreement calculation
6. Dataset finalization and export to JSON

## Streamlit Interface

The Streamlit-based annotation interface provides:
- Real-time annotation statistics
- User-friendly interface with keyboard shortcuts
- Progress tracking and completion metrics
- Annotation history and revision capabilities
- Export functionality to various formats
