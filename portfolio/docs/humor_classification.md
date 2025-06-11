# Humor Classification Annotation Project

This project provides tools and interfaces for annotating humor content with multi-category classification.

## Features

- Multi-category humor content classification
- Python-based data processing and automated dataset validation
- Support for annotating humor types, targets, and intensity levels
- Inter-annotator agreement metrics and quality control
- Customizable annotation schema for different humor research needs

## Technologies Used

- **Python**: Core processing and data handling
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical operations and statistics
- **Scikit-learn**: Basic ML operations and metrics
- **Matplotlib/Seaborn**: Visualization of annotation distributions

## Annotation Schema

The humor annotation schema includes:

1. **Humor Detection**: Binary classification (Humorous/Not Humorous)
2. **Humor Type**: Sarcasm, Irony, Wordplay, Absurdist, Parody, etc.
3. **Humor Target**: Self, Others, Situation, Society, etc.
4. **Humor Intensity**: Scale from 1-5 measuring perceived humor strength
5. **Cultural Context**: Tags for culture-specific humor elements

## Workflow

1. Data collection from diverse sources
2. Pre-processing and normalization
3. First-pass annotation with humor detection
4. Second-pass annotation with detailed humor categorization
5. Quality control and agreement calculation
6. Dataset finalization and export for model training

## Data Processing Scripts

The project includes scripts for:
- Data preparation and cleaning
- Converting between annotation formats
- Calculating inter-annotator agreement
- Generating annotation statistics and visualizations
- Exporting to standardized formats
