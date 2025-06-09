# Medical Chart Error Annotation Guidelines

## Error Types and Tags
1. **Medication Error** `[MED]`
   - Wrong dosage
   - Incorrect medication name
   - Missing prescription details

2. **Diagnostic Error** `[DX]`
   - Missed diagnosis
   - Delayed diagnosis
   - Wrong diagnosis

3. **Documentation Error** `[DOC]`
   - Missing patient information
   - Incorrect dates
   - Incomplete records

4. **Procedural Error** `[PROC]`
   - Wrong procedure
   - Incorrect procedure timing
   - Missing procedure documentation

## Annotation Process
1. Highlight the error span
2. Select appropriate error type using tags
3. Add notes if necessary

## Examples
```
Patient prescribed [Metformin 1000mg]{tag="MED"} instead of 100mg
[Missing vital signs from morning rounds]{tag="DOC"}
[Delayed CT scan order]{tag="PROC"} resulting in late diagnosis
```