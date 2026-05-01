# Python Sensor Data Analysis

## Overview
This project analyzes sensor data from a smart home / embedded system using Python.

The script reads temperature, light and motion data from a CSV file, calculates important statistics, detects warning events, creates plots and generates an automated text report.

This project connects Python programming with mechatronics, sensor data and embedded systems.

## Features
- Read sensor data from a CSV file
- Analyze temperature values
- Analyze light sensor values
- Count motion detection events
- Detect high temperature warnings
- Detect low light events
- Generate temperature and light plots
- Create an automated text report

## Technologies Used
- Python
- Pandas
- Matplotlib
- CSV data handling
- Data analysis
- Automation
- Sensor data processing

## Repository Structure

```text
python-sensor-data-analysis/
│
├── README.md              # Project documentation
├── sensor_analysis.py     # Main Python analysis script
├── sensor_data.csv        # Sample sensor dataset
└── requirements.txt       # Required Python libraries
Input Data

The project uses a CSV file named:

sensor_data.csv

The CSV file contains:

Column	Description
time_s	Time in seconds
temperature_c	Temperature value in degrees Celsius
light_value	Analog light sensor value
motion_detected	Motion detection state, 0 or 1
Analysis Logic
Temperature Analysis

The script calculates:

Average temperature
Maximum temperature
Minimum temperature
Number of high temperature warnings

A warning is detected when:

temperature_c > 28.0
Light Analysis

The script calculates:

Average light value
Maximum light value
Minimum light value
Number of low light events

A low light event is detected when:

light_value < 400
Motion Analysis

The script calculates:

Number of motion events
Motion percentage during the measurement period
Generated Output

After running the script, the following files are generated:

sensor_report.txt
temperature_plot.png
light_plot.png
How to Run
1. Install required libraries
pip install -r requirements.txt
2. Run the analysis script
python sensor_analysis.py
Example Output

The program prints:

Analysis completed successfully.
Report saved as: sensor_report.txt
Plots saved as: temperature_plot.png and light_plot.png
Project Purpose

The purpose of this project is to show how Python can be used for engineering data analysis.

It demonstrates how sensor data from embedded systems can be processed, analyzed and visualized using Python.

What I Learned
Reading CSV files with Python
Using Pandas for data analysis
Creating plots with Matplotlib
Detecting warning conditions from sensor values
Generating automated reports
Connecting Python analysis with embedded systems and smart home applications
Future Improvements
Add real sensor data from Arduino
Add more sensor types
Add humidity analysis
Add live serial data reading from Arduino
Add dashboard visualization
Export reports as PDF
Add automatic email report generation
Project Status

This project was developed as a Python data analysis and automation project related to sensor data and embedded systems.
