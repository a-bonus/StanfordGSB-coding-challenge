# Hall of Fame Inductees Analysis - Stanford GSB Coding Challenge

## Project Overview

This project aims to visualize the trends in the induction of players into the Hall of Fame from various countries over the years. The analysis focuses on understanding how different countries have contributed to the Hall of Fame and the evolution of these contributions through time.

## Data Sources

The analysis utilizes two primary data sources:

1. `HallOfFame.csv`: Contains records of players inducted into the Hall of Fame.
2. `Master.csv`: Provides detailed information about the players, including their birth countries.

## Tools and Libraries Used

- **Python:** The core programming language for the analysis.
- **Pandas:** A powerful data manipulation library in Python.
- **Matplotlib:** A Python plotting library for creating static, interactive, and animated visualizations.
- **Seaborn:** A Python data visualization library based on matplotlib that provides a high-level interface for drawing attractive and informative statistical graphics.

## Analysis Workflow

1. **Data Loading and Preprocessing:**
   - Load the data from the CSV files.
   - Filter and select relevant columns for the analysis.

2. **Data Merging:**
   - Combine data from both sources to create a comprehensive dataset.

3. **Data Aggregation:**
   - Group data by country and induction year.
   - Calculate the count of inductees for each group.

4. **Data Transformation:**
   - Fill missing combinations of country and year with zeros to maintain continuity.
   - Calculate the cumulative sum of inductees for each country over the years.

5. **Data Visualization:**
   - Create a line plot to visualize the cumulative sum of Hall of Fame inductees by country over the years.
   - Employ a logarithmic scale for the y-axis to better represent disparities.

## Results

The visualization provides insights into the trends and patterns of Hall of Fame inductions across different countries. It highlights the dominance of certain countries and the growth or decline in the number of inductees from various regions over time.

## How to Run the Analysis

To execute this analysis:

1. Ensure you have Python, Pandas, Matplotlib, and Seaborn installed.
2. Clone this repository.
3. Run the provided Python script (`hof_analysis.py`).

## From DataCamp Portfolio 
https://app.datacamp.com/workspace/w/4524f486-ea6c-41ed-adb2-6d081c042231/edit


