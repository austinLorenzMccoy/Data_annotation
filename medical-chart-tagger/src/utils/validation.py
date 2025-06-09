from typing import List, Dict
import re

class AnnotationValidator:
    def __init__(self):
        self.error_types = ['medication', 'diagnostic', 'documentation']
        
    def validate_spans(self, text: str, annotations: List[Dict]) -> List[str]:
        """
        Validate annotation spans
        """
        errors = []
        for ann in annotations:
            start = ann.get('start')
            end = ann.get('end')
            label = ann.get('label')
            
            if not (isinstance(start, int) and isinstance(end, int)):
                errors.append(f"Invalid span indices: {start}-{end}")
                continue
                
            if start >= end:
                errors.append(f"Invalid span range: {start}-{end}")
                
            if label not in self.error_types:
                errors.append(f"Invalid error type: {label}")
                
        return errors

    def check_overlapping_spans(self, annotations: List[Dict]) -> List[str]:
        """
        Check for overlapping annotation spans
        """
        errors = []
        sorted_anns = sorted(annotations, key=lambda x: x['start'])
        
        for i in range(len(sorted_anns)-1):
            if sorted_anns[i]['end'] > sorted_anns[i+1]['start']:
                errors.append(f"Overlapping spans found: {sorted_anns[i]} and {sorted_anns[i+1]}")
                
        return errors