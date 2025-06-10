#!/bin/bash

# Check if streamlit is installed
if ! command -v streamlit &> /dev/null; then
    echo "📦 Streamlit not found. Installing required packages..."
    pip install streamlit pandas
fi

# Create necessary directories
mkdir -p data/exports
mkdir -p data/processed

echo "🚀 Starting Multilingual Offensive Language Annotation Tool..."
echo "📝 Access the interface at: http://localhost:8501"
echo ""
echo "To stop the server, press Ctrl+C"

# Run the Streamlit app
streamlit run app.py
