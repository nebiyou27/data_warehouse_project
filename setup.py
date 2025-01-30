import os

# Define the folder structure
folders = [
    "data/raw",
    "data/cleaned",
    "data/images",
    "data/detections",
    "data/warehouse",
    "src",
    "models",
    "logs",
    "tests",
    "docs"
]

# Define the files to be created
files = {
    "src/scraping.py": "# Script for Telegram data scraping",
    "src/cleaning.py": "# Script for data cleaning and transformation",
    "src/yolo_detection.py": "# Script for YOLO object detection",
    "src/database.py": "# Script for database setup and interactions",
    "src/api.py": "# FastAPI implementation",
    "src/config.py": "# Configuration file (e.g., database credentials)",
    "README.md": "# Medical Data Warehouse Project\n\nThis project involves scraping, processing, and storing medical business data from Telegram.",
    "requirements.txt": "# List of dependencies",
    ".gitignore": "*.pyc\npycache/\ndata/raw/\nlogs/"
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
for file_path, content in files.items():
    with open(file_path, "w") as f:
        f.write(content)

print("Project folder structure created successfully!")