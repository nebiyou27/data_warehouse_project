
# Medical Data Warehouse Project

## Business Need

As a data engineer at Kara Solutions, your task is to build a data warehouse to store and manage data on Ethiopian medical businesses, scraped from various web sources and Telegram channels. The project aims to create a robust and scalable data pipeline capable of efficiently collecting, cleaning, enriching, and storing data. Additionally, this solution will integrate object detection capabilities using YOLO (You Only Look Once) to enhance data analysis and provide valuable insights to stakeholders in the medical industry.

The objective is to centralize data from disparate sources to perform comprehensive analysis, identify trends and patterns, and help decision-makers take actionable steps based on the data. This will enable businesses to make informed decisions, optimize their strategies, and improve service offerings in the Ethiopian medical sector.

## Project Overview

The project involves several key steps to create a well-rounded data pipeline:

1. **Data Scraping & Collection**: Data will be collected from medical-related Telegram channels and websites.
2. **Data Cleaning & Transformation**: Raw data will be cleaned and transformed for use in the data warehouse.
3. **Object Detection**: YOLO (You Only Look Once) will be used for detecting objects in images.
4. **Data Warehouse Design & Implementation**: A central data warehouse will be designed and implemented to store cleaned data.
5. **Data Integration & Enrichment**: Integrating different data sources and enriching the dataset for better insights.

## Folder Structure

The project is organized into the following folder structure for efficiency and scalability:

```
.
├── data/                      # Data directory containing all raw and processed data
│   ├── raw/                   # Scraped raw data
│   ├── cleaned/               # Cleaned and transformed data
│   ├── images/                # Images collected for object detection
│   ├── detections/            # YOLO object detection results
│   └── warehouse/             # Final data warehouse (database)
├── notebooks/                 # Jupyter notebooks for various tasks
│   ├── 01_scraping.ipynb      # Data scraping and collection notebook
│   ├── 02_cleaning.ipynb      # Data cleaning and transformation notebook
│   ├── 03_yolo_detection.ipynb# YOLO object detection notebook
│   ├── 04_database.ipynb      # Database and data warehouse setup
│   └── 05_api.ipynb           # API development for data access
├── src/                       # Source code directory
│   ├── scraping.py            # Python script for scraping data from Telegram
│   ├── cleaning.py            # Python script for cleaning and transforming data
│   ├── yolo_detection.py      # Python script for YOLO object detection
│   ├── database.py            # Python script for setting up and interacting with the database
│   ├── api.py                 # FastAPI implementation for data serving
│   └── config.py              # Configuration file (e.g., database credentials)
├── models/                    # Directory for machine learning models
├── logs/                      # Log files for monitoring and debugging
├── tests/                     # Unit tests for data processing and ETL pipelines
├── docs/                      # Documentation for the project
├── README.md                  # Project overview and setup instructions
├── requirements.txt           # Python dependencies
├── .gitignore                 # Git ignore file
└── .github/                   # GitHub Actions workflow for CI/CD
    └── workflows/
        └── ci.yml             # Continuous integration configuration
```



## Installation

Follow the steps below to set up the project environment and get started:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repository-name.git
   cd your-repository-name
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **Mac/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Data Scraping**: Run the scraping notebook or script to collect data from the specified Telegram channels. Use `notebooks/01_scraping.ipynb` or `src/scraping.py`.

2. **Data Cleaning**: Clean and transform the raw data into a structured format using `notebooks/02_cleaning.ipynb` or `src/cleaning.py`.

3. **Object Detection**: Use YOLO for object detection on the images collected. This is handled in `notebooks/03_yolo_detection.ipynb` and `src/yolo_detection.py`.

4. **Data Warehouse**: Store the cleaned data in the data warehouse, either using the `notebooks/04_database.ipynb` or `src/database.py`.

5. **API Development**: Serve the data via an API for easy access and integration with other systems. This is implemented in `notebooks/05_api.ipynb` and `src/api.py`.

## CI/CD

This project uses GitHub Actions for continuous integration and deployment. The CI pipeline is defined in `.github/workflows/ci.yml`. It automatically installs dependencies, runs tests, and lints the code on every push to the repository.

## Contributing

Feel free to fork this repository, create a branch, and submit pull requests. Please ensure your changes are tested and well-documented.

---
