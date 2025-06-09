# Medical Chart Tagger

## Overview
The Medical Chart Tagger is an application designed for span-level annotation of medical charts using Named Entity Recognition (NER) techniques. This project leverages advanced machine learning models to assist in tagging relevant information within medical documents.

## Project Structure
```
medical-chart-tagger
├── src
│   ├── app.py                # Main entry point of the application
│   ├── models
│   │   └── tagger.py         # Class for span-level annotation
│   ├── data
│   │   └── schema.json       # Data schema definition
│   └── utils
│       ├── preprocessing.py   # Data preprocessing utilities
│       └── evaluation.py      # Model evaluation functions
├── requirements.txt          # Project dependencies
├── config.yaml               # Configuration settings
└── README.md                 # Project documentation
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   cd medical-chart-tagger
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Configure the application by editing the `config.yaml` file to set model parameters and file paths.

## Usage
To run the application, execute the following command:
```
python src/app.py
```

## Features
- Span-level annotation of medical charts
- Model training and evaluation
- Data preprocessing utilities
- Performance metrics calculation

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.