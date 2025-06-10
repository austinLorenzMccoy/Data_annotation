# Multilingual Offensive Language Annotation Project

This project provides a setup for annotating multilingual offensive language data using Label Studio.

## Setup Instructions

1. **Activate the Conda Environment**

   ```bash
   source activate_env.bash
   ```

2. **Prepare Your Data**

   Run the data preparation script to convert your raw data to Label Studio format:

   ```bash
   python prepare_data.py
   ```

3. **Run Label Studio**

   Start the Label Studio server:

   ```bash
   python run_labelstudio.py
   ```

   This will:
   - Start Label Studio on http://localhost:8080
   - Open your browser automatically
   - Configure the login credentials

## Project Structure

- `configs/` - Contains XML configuration files for Label Studio
- `data/` - Contains all data files
  - `raw/` - Original data files
  - `imports/` - Files formatted for Label Studio import
  - `exports/` - Annotation exports from Label Studio
  - `processed/` - Processed data files
- `scripts/` - Utility scripts
- `models/` - For storing trained models
- `notebooks/` - Jupyter notebooks for analysis

## Annotation Guidelines

When annotating texts:

1. **Offensive Level**
   - `not_offensive`: No offensive content
   - `mildly_offensive`: Slightly offensive but not severe
   - `offensive`: Clearly offensive content
   - `very_offensive`: Extremely offensive content

2. **Bias Type**
   - `gender`: Gender-based bias
   - `racial`: Racial or ethnic bias
   - `religious`: Religious bias
   - `political`: Political bias
   - `socioeconomic`: Class or economic status bias
   - `other`: Other forms of bias

3. **Target**
   - `individual`: Targeted at a specific person
   - `group`: Targeted at a group of people
   - `other`: Other targets
   - `none`: No specific target

4. **Language**
   - `hausa_english`: Hausa-English code-mixed text
   - `yoruba_english`: Yoruba-English code-mixed text
   - `igbo_english`: Igbo-English code-mixed text
   - `pidgin`: Nigerian Pidgin
   - `hinglish`: Hindi-English code-mixed text

## Importing Data

1. Start Label Studio
2. Create a new project
3. In the project, go to Settings > Labeling Interface
4. Copy and paste the content from `configs/improved_config.xml`
5. Save the configuration
6. Go to Import > Import from file
7. Select the file from `data/imports/sample_data_labelstudio.json`

## Exporting Annotations

1. In your Label Studio project, go to Export
2. Choose the export format (JSON is recommended)
3. Download the file and save it to `data/exports/`

## Additional Scripts

- `setup.py`: Sets up the project directory structure
- `prepare_data.py`: Converts raw data to Label Studio format
- `run_labelstudio.py`: Starts the Label Studio server
