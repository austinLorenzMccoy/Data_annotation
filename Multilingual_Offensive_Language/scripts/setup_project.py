import json
import os
import sys
import subprocess
from pathlib import Path

def get_conda_prefix():
    """Get the conda installation prefix"""
    try:
        result = subprocess.run(['conda', 'info', '--json'], 
                              capture_output=True, text=True, check=True)
        info = json.loads(result.stdout)
        return info['conda_prefix']
    except Exception as e:
        print(f"❌ Failed to get conda prefix: {e}")
        sys.exit(1)

def check_conda():
    try:
        result = subprocess.run(['conda', '--version'], check=True, capture_output=True, text=True)
        print(f"✅ Found conda: {result.stdout.strip()}")
        return True
    except:
        print("❌ Conda is not installed or not in PATH. Please install Anaconda or Miniconda first.")
        sys.exit(1)

def setup_conda_environment():
    try:
        # Remove existing environment if it exists
        try:
            subprocess.run(['conda', 'env', 'remove', '-n', 'offensive_lang', '-y'], 
                         check=False, capture_output=True)
            print("Removed existing environment")
        except:
            pass
        
        print("Creating new conda environment...")
        # Create base environment with Python 3.10
        subprocess.run(['conda', 'create', '-n', 'offensive_lang', 
                      'python=3.10', 'pip', 'pandas', 'scikit-learn', 'pyyaml',
                      '-y', '-c', 'conda-forge'], check=True)
        
        # Install compatible package versions - fixed dependency conflicts
        pip_packages = [
            'label-studio==1.7.3',
            'django==3.2.16',
            'django-cors-headers==3.6.0',  # Match label-studio requirement
            'django-filter==2.4.0',
            'djangorestframework==3.12.0',
            'label-studio-sdk==0.0.23'
        ]
        
        print("Installing pip packages...")
        for package in pip_packages:
            print(f"Installing {package}...")
            cmd = ['conda', 'run', '-n', 'offensive_lang', 'pip', 'install', package]
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode != 0:
                print(f"Warning: Failed to install {package}")
                print(f"Error: {result.stderr}")
        
        # Create activation script for different shells
        activation_scripts = {
            'activate_env.bash': f'''#!/bin/bash
eval "$(conda shell.bash hook)"
conda activate offensive_lang
export PYTHONPATH={os.getcwd()}
echo "✅ Environment activated. Label Studio should be available."
''',
            'activate_env.zsh': f'''#!/bin/zsh
eval "$(conda shell.zsh hook)"
conda activate offensive_lang
export PYTHONPATH={os.getcwd()}
echo "✅ Environment activated. Label Studio should be available."
''',
            'activate_env.fish': f'''#!/usr/bin/env fish
conda activate offensive_lang
set -x PYTHONPATH {os.getcwd()}
echo "✅ Environment activated. Label Studio should be available."
'''
        }
        
        for script_name, content in activation_scripts.items():
            with open(script_name, 'w') as f:
                f.write(content)
            os.chmod(script_name, 0o755)
        
        print("✅ Conda environment created successfully")
        print("\nTo activate the environment:")
        print("  For bash: source activate_env.bash")
        print("  For zsh:  source activate_env.zsh") 
        print("  For fish: source activate_env.fish")
        print("  Or manually: conda activate offensive_lang")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to create Conda environment: {e}")
        if e.stderr:
            print(f"Error details: {e.stderr.decode()}")
        sys.exit(1)

def create_project_structure():
    """Create the complete project directory structure"""
    directories = [
        'configs',
        'data/raw',
        'data/processed', 
        'data/imports',
        'scripts',
        'exports',
        'guidelines',
        'models',
        'notebooks',
        'tests'
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        
    # Create .gitignore
    gitignore_content = '''# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
venv/
ENV/
env/
.venv/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Data
*.csv
*.json
*.txt
!sample_data.json
!requirements.txt

# Exports
exports/
*.sqlite3

# Label Studio
.label_studio/
label_studio.log
'''
    
    with open('.gitignore', 'w') as f:
        f.write(gitignore_content)
    
    print("✅ Project structure created")

def create_label_studio_config():
    """Create Label Studio configuration file"""
    config_content = '''<View>
  <Text name="text" value="$text"/>
  <Header value="Language: $language"/>
  
  <Choices name="offensive_level" toName="text" choice="single-radio">
    <Choice value="not_offensive" alias="1 - Not Offensive"/>
    <Choice value="mildly_offensive" alias="2 - Mildly Offensive"/>
    <Choice value="offensive" alias="3 - Offensive"/>
  </Choices>
  
  <Choices name="bias_type" toName="text" choice="multiple">
    <Choice value="gender" alias="Gender Bias"/>
    <Choice value="racial" alias="Racial Bias"/>
    <Choice value="religious" alias="Religious Bias"/>
    <Choice value="political" alias="Political Bias"/>
    <Choice value="other" alias="Other Bias"/>
  </Choices>
  
  <TextArea name="notes" toName="text" 
           placeholder="Additional notes about context, cultural nuances, etc."
           maxSubmissions="1"/>
</View>'''
    
    os.makedirs('configs', exist_ok=True)
    with open('configs/labeling_config.xml', 'w') as f:
        f.write(config_content)
    
    print("✅ Label Studio configuration created")

def create_start_script():
    """Create a script to start Label Studio easily"""
    start_script = '''#!/bin/bash

# Check if conda environment is activated
if [[ "$CONDA_DEFAULT_ENV" != "offensive_lang" ]]; then
    echo "❌ Please activate the conda environment first:"
    echo "   source activate_env.bash"
    exit 1
fi

# Create data directory if it doesn't exist
mkdir -p data/imports

# Start Label Studio
echo "🚀 Starting Label Studio..."
echo "📝 Access the interface at: http://localhost:8080"
echo "📊 Login with: chibuezeaugustine23@gmail.com"
echo "🔑 Password: Constantlabelstudio35$"
echo ""
echo "To stop the server, press Ctrl+C"

label-studio start --host localhost --port 8080
'''
    
    with open('start_labelstudio.sh', 'w') as f:
        f.write(start_script)
    os.chmod('start_labelstudio.sh', 0o755)
    
    print("✅ Start script created: ./start_labelstudio.sh")

if __name__ == "__main__":
    print("🚀 Setting up Multilingual Offensive Language Annotation Project")
    print("=" * 60)
    
    check_conda()
    create_project_structure()
    setup_conda_environment()
    create_label_studio_config()
    create_start_script()
    
    print("\n" + "=" * 60)
    print("✅ Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Activate environment: source activate_env.zsh  # or activate_env.bash")
    print("2. Start Label Studio: ./start_labelstudio.sh")
    print("3. Go to http://localhost:8080")
    print("4. Login with chibuezeaugustine23@gmail.com")
    print("5. Create a new project and import your data")
    print("\n📁 Your sample data is in sample_data.json")
    print("📖 Annotation guidelines are in annotation_guidelines.md")