from typing import List, Dict
import pandas as pd
from sklearn.metrics import precision_score, recall_score, f1_score, cohen_kappa_score
import numpy as np

def calculate_inter_annotator_agreement(annotations: List[Dict]) -> float:
    """
    Calculate inter-annotator agreement using Cohen's Kappa
    
    Args:
        annotations: List of annotation dictionaries from different annotators
    
    Returns:
        float: Kappa score
    """
    if len(annotations) != 2:
        raise ValueError("Exactly two annotators required for Cohen's Kappa")
    
    annotator1 = np.array(annotations[0]['labels'])
    annotator2 = np.array(annotations[1]['labels'])
    
    return cohen_kappa_score(annotator1, annotator2)

def evaluate_annotations(gold_standard: Dict, predictions: Dict) -> Dict:
    """
    Evaluate annotations against gold standard
    
    Args:
        gold_standard: Dictionary containing gold standard annotations
        predictions: Dictionary containing predicted annotations
    
    Returns:
        Dict containing precision, recall, and F1 scores
    """
    y_true = [ann['label'] for ann in gold_standard['annotations']]
    y_pred = [ann['label'] for ann in predictions['annotations']]
    
    return calculate_metrics(y_true, y_pred)

def calculate_metrics(y_true, y_pred):
    """
    Calculate precision, recall, and F1 score
    """
    precision = precision_score(y_true, y_pred, average='weighted')
    recall = recall_score(y_true, y_pred, average='weighted')
    f1 = f1_score(y_true, y_pred, average='weighted')

    return {
        'precision': float(precision),
        'recall': float(recall),
        'f1_score': float(f1),
        'num_samples': len(y_true)
    }