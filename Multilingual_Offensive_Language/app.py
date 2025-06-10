import streamlit as st
import json
import os
import pandas as pd
from pathlib import Path

# Set page configuration
st.set_page_config(
    page_title="Multilingual Offensive Language Annotation",
    page_icon="🔤",
    layout="wide"
)

# Create necessary directories
def create_directories():
    dirs = ["data/processed", "data/exports", "data/imports"]
    for dir_path in dirs:
        Path(dir_path).mkdir(parents=True, exist_ok=True)

# Load data
def load_data():
    data_path = "data/raw/sample_data.json"
    if not os.path.exists(data_path):
        st.error(f"Data file not found: {data_path}")
        return []
    
    try:
        with open(data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return []

# Save annotations
def save_annotations(annotations):
    export_dir = "data/exports"
    os.makedirs(export_dir, exist_ok=True)
    
    export_path = os.path.join(export_dir, "annotations.json")
    with open(export_path, 'w', encoding='utf-8') as f:
        json.dump(annotations, f, indent=2, ensure_ascii=False)
    
    st.success(f"Annotations saved to {export_path}")

# Main app
def main():
    create_directories()
    
    # App title and description
    st.title("Multilingual Offensive Language Annotation")
    st.markdown("""
    This tool helps annotate multilingual text for offensive content.
    Select a text from the sidebar and annotate it using the form below.
    """)
    
    # Load data
    data = load_data()
    if not data:
        st.warning("No data available for annotation.")
        return
    
    # Initialize session state for annotations
    if 'annotations' not in st.session_state:
        # Try to load existing annotations if available
        export_path = "data/exports/annotations.json"
        if os.path.exists(export_path):
            try:
                with open(export_path, 'r', encoding='utf-8') as f:
                    st.session_state.annotations = json.load(f)
            except:
                st.session_state.annotations = {}
        else:
            st.session_state.annotations = {}
    
    if 'current_index' not in st.session_state:
        st.session_state.current_index = 0
    
    # Sidebar for navigation
    with st.sidebar:
        st.header("Navigation")
        
        # Text selection
        text_options = [f"{item['id']}: {item['text'][:30]}..." for item in data]
        selected_text = st.selectbox(
            "Select text to annotate:",
            options=range(len(text_options)),
            format_func=lambda x: text_options[x],
            index=st.session_state.current_index
        )
        st.session_state.current_index = selected_text
        
        # Progress tracking
        annotated_count = len(st.session_state.annotations)
        total_count = len(data)
        st.progress(annotated_count / total_count)
        st.text(f"Annotated: {annotated_count}/{total_count}")
        
        # Save button
        if st.button("💾 Save All Annotations"):
            save_annotations(st.session_state.annotations)
    
    # Main content - annotation interface
    current_item = data[st.session_state.current_index]
    item_id = str(current_item['id'])
    
    # Display text to annotate
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Text to Annotate")
        st.info(current_item['text'])
        st.caption(f"Language: {current_item['language']}")
    
    with col2:
        st.subheader("Translation")
        # Only show translation if it's different from the original text
        if current_item['language'] != 'english' and current_item['text'] != current_item['translation']:
            st.success(current_item['translation'])
        else:
            st.success("[Standard English - No translation needed]")
            st.caption("This is standard English text that doesn't require translation.")
    
    # Annotation form
    with st.form(key=f"annotation_form_{item_id}"):
        st.subheader("Annotation")
        
        # Get existing annotation if available
        existing = st.session_state.annotations.get(item_id, {})
        
        # Offensive level
        offensive_level = st.radio(
            "1. Offensive Level:",
            options=["not_offensive", "mildly_offensive", "offensive", "very_offensive"],
            index=["not_offensive", "mildly_offensive", "offensive", "very_offensive"].index(existing.get("offensive_level", "not_offensive"))
        )
        
        # Bias type
        st.write("2. Bias Type (if applicable):")
        bias_types = ["gender", "racial", "religious", "political", "socioeconomic", "other"]
        bias_selections = {}
        
        existing_bias = existing.get("bias_type", [])
        for bias in bias_types:
            bias_selections[bias] = st.checkbox(
                bias, 
                value=bias in existing_bias,
                key=f"bias_{item_id}_{bias}"
            )
        
        # Target of offensive content
        st.write("3. Target of Offensive Content:")
        target_types = ["individual", "group", "other", "none"]
        target_selections = {}
        
        existing_targets = existing.get("target", [])
        for target in target_types:
            target_selections[target] = st.checkbox(
                target, 
                value=target in existing_targets,
                key=f"target_{item_id}_{target}"
            )
        
        # Notes
        notes = st.text_area(
            "5. Notes:",
            value=existing.get("notes", ""),
            height=100
        )
        
        # Submit button
        submitted = st.form_submit_button("Save Annotation")
        
        if submitted:
            # Collect selected bias types and targets
            selected_bias = [bias for bias, selected in bias_selections.items() if selected]
            selected_targets = [target for target, selected in target_selections.items() if selected]
            
            # Save annotation
            st.session_state.annotations[item_id] = {
                "offensive_level": offensive_level,
                "bias_type": selected_bias,
                "target": selected_targets,
                "notes": notes,
                "text": current_item['text'],
                "language": current_item['language']
            }
            
            st.success("Annotation saved!")
            
            # Auto-advance to next item if not the last one
            if st.session_state.current_index < len(data) - 1:
                st.session_state.current_index += 1
                st.experimental_rerun()
    
    # Navigation buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Previous") and st.session_state.current_index > 0:
            st.session_state.current_index -= 1
            st.experimental_rerun()
    
    with col2:
        if st.button("➡️ Next") and st.session_state.current_index < len(data) - 1:
            st.session_state.current_index += 1
            st.experimental_rerun()
    
    # Display annotation statistics
    if st.session_state.annotations:
        st.subheader("Annotation Statistics")
        
        # Convert annotations to DataFrame for analysis
        annotations_df = pd.DataFrame.from_dict(st.session_state.annotations, orient='index')
        
        # Display statistics
        col1, col2 = st.columns(2)
        
        with col1:
            if 'offensive_level' in annotations_df:
                st.write("Offensive Level Distribution:")
                offensive_counts = annotations_df['offensive_level'].value_counts()
                st.bar_chart(offensive_counts)
        
        with col2:
            if 'language' in annotations_df:
                st.write("Language Distribution:")
                language_counts = annotations_df['language'].value_counts()
                st.bar_chart(language_counts)

if __name__ == "__main__":
    main()
