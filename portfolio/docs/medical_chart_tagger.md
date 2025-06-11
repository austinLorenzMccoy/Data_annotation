# Medical Chart Tagger Annotation Project

This project provides specialized tools for clinical document annotation with entity and relation tagging using Label Studio.

## Features

- Clinical entity and relation tagging
- HL7/FHIR export capabilities
- Support for annotating medical charts, clinical notes, and discharge summaries
- Integration with medical terminology standards
- Quality control mechanisms for medical annotation

## Technologies Used

- **Label Studio**: Primary annotation platform
- **Python**: Backend processing and data handling
- **UMLS**: Medical terminology integration
- **HL7/FHIR**: Healthcare data standards for export

## Annotation Schema

The medical chart annotation schema includes:

1. **Clinical Entities**:
   - Diagnoses
   - Medications
   - Procedures
   - Lab Results
   - Vital Signs
   - Allergies
   - Medical History

2. **Relations**:
   - Medication-Condition
   - Procedure-Diagnosis
   - Lab-Diagnosis
   - Temporal Relations
   - Causal Relations

3. **Attributes**:
   - Certainty (Confirmed, Suspected, Ruled Out)
   - Temporality (Current, Historical, Future)
   - Experiencer (Patient, Family Member)

## Workflow

1. Medical document pre-processing
2. First-pass entity annotation
3. Second-pass relation annotation
4. Quality review by medical professionals
5. Export to HL7/FHIR formats
6. Integration with medical knowledge bases

## Integration

The annotation system integrates with:
- UMLS for medical terminology standardization
- HL7/FHIR for healthcare data exchange
- Medical NLP systems for pre-annotation
