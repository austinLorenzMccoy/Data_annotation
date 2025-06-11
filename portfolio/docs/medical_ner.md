# Medical Named Entity Recognition (NER) Annotation Project

This project provides a Doccano-based system for medical named entity recognition with UMLS mapping and annotation guidelines.

## Features

- Named Entity Recognition for medical text using Doccano
- UMLS terminology mapping for standardized annotations
- Comprehensive annotation guidelines for medical entities
- Quality control and inter-annotator agreement metrics
- Support for clinical notes, research papers, and medical literature

## Technologies Used

- **Doccano**: Primary annotation platform
- **Python**: Backend processing and integration
- **UMLS**: Medical terminology standardization
- **spaCy**: Pre-annotation and NLP processing
- **Pandas**: Data manipulation and analysis

## Annotation Schema

The medical NER annotation schema includes:

1. **Entity Types**:
   - Diseases & Disorders
   - Medications & Drugs
   - Anatomical Structures
   - Symptoms & Signs
   - Procedures & Treatments
   - Medical Devices
   - Lab Tests & Results

2. **Entity Attributes**:
   - UMLS CUI (Concept Unique Identifier)
   - Semantic Type
   - Negation Status
   - Certainty Level
   - Temporality

## Workflow

1. Document pre-processing and segmentation
2. Automatic pre-annotation using medical NLP models
3. Manual annotation correction and completion in Doccano
4. UMLS concept mapping and standardization
5. Quality control and inter-annotator agreement calculation
6. Export to standard formats (CoNLL, BRAT, JSON)

## Annotation Guidelines

Detailed guidelines are provided for annotators covering:
- Entity boundary determination
- Handling of nested entities
- Disambiguation of similar medical concepts
- Annotation of abbreviations and acronyms
- Special cases in medical terminology
