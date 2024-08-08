# nhc-internal-linking-analysis
Internal Linking Analysis of the nortonheatlhcare.com domain.

# NHC Internal Linking Analysis

## Project Overview
This project analyzes the internal and external linking structure of the Service Line (SL) pages on the Norton Healthcare (NHC) website. By using crawl data from Screaming Frog, the project provides insights into linking patterns, identifies the most linked pages, and understands the distribution of links across various pages.

## Setup Instructions
1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/nhc-internal-linking-analysis.git
   cd nhc-internal-linking-analysis

2. **Setup Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # For macOS/Linux
    venv\Scripts\activate.vat  # For Windows

3. **Install requirements.txt**
    ```bash
    pip install -r requirements.txt

4. **Place data files**
    
    Ensure that SL_inlinks.csv and SL_outlinks.csv are in the data directory.

5. **Run the Data Loading Script**
    ```python
    python scripts/load_data.py

6. **Run the Data Cleaning Script**
    ```python
    python scripts/clean_data.py

7. **Run the Data Combining Script**
    ```python
    python scripts/combine_data.py

8. **Run the Data Analysis Script**
    ```python
    python scripts/analyze_data.py


# Project Files
    data/: Directory containing the raw and processed data files.
    scripts/: Directory containing the scripts for data loading, cleaning, combining, and analysis.
    venv/: Virtual environment for dependencies.
    requirements.txt: List of required Python packages.
    README.md: Project overview and setup instructions.

# Analysis Results
The analysis results should include:

top_internal_linked_pages.png: Bar chart of the top 10 most linked internal pages.
top_external_linked_pages.png: Bar chart of the top 10 most linked external pages.
top_sources_internal_pages.png: Bar chart of the top sources linking to the top internal pages.
top_sources_external_pages.png: Bar chart of the top sources linking to the top external pages.

# Interpretation of Data Analysis
The visualizations provide insights into the linking structure of the NHC website. The top internal and external pages are identified, along with the most frequent sources linking to these pages. This analysis helps understand the distribution of links and potential areas for optimization in the website's internal linking strategy.

## Features
1. **Data Loading:**
   - Read two CSV data files (`SL_inlinks.csv` and `SL_outlinks.csv`).

2. **Data Cleaning and Combining:**
   - Cleaned the data by removing duplicates and dropping rows with missing targets.
   - Performed a pandas merge to combine the internal and external links data.

3. **Data Analysis:**
   - Analyzed the top 10 most linked internal pages.
   - Analyzed the top 10 most linked external pages.
   - Identified the top sources linking to the top internal pages.
   - Identified the top sources linking to the top external pages.

4. **Data Visualization:**
   - Created bar charts to display the top 10 most linked internal and external pages.
   - Created bar charts to display the top sources linking to the top internal and external pages.

5. **Best Practices:**
   - Utilized a virtual environment and provided setup instructions.
   - Included clear and concise comments in the Python scripts.

# Testing and Review
To ensure the project meets all requirements, the following steps were taken:
    Thorough testing of each script to verify functionality.
    Visualization outputs reviewed for accuracy and clarity.
    Clear instructions provided for setup and running the project.