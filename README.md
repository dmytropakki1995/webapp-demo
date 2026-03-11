### webapp
This repo is used as a demo for School 
You should be able to use Python venv and pip for package installation


### 🧰 Requirements
- **python** version 3.12 or later

### 🛠 Run Python application
```sh
# Create venv
python -m venv venv

## Activate vevn
# Linux
source venv/bin/activate
# Windows
venv\Scripts\activate

# install dependencies
uv sync

# Activate .venv
source .venv/bin/activate

# Install packages
pip install -r requirements.txt

# Run application
python main.py
```