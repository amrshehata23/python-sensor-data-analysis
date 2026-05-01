"""
Python Sensor Data Analysis

This project analyzes sensor data from a smart home / embedded system.
It reads temperature, light and motion data from a CSV file, calculates
important statistics, detects warnings and generates plots and a text report.

Project: Python Sensor Data Analysis
Language: Python
Libraries: pandas, matplotlib
"""

from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


DATA_FILE = Path("sensor_data.csv")
REPORT_FILE = Path("sensor_report.txt")

TEMPERATURE_WARNING_LIMIT = 28.0
LOW_LIGHT_LIMIT = 400


def load_sensor_data(file_path: Path) -> pd.DataFrame:
    """Load sensor data from a CSV file."""
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    data = pd.read_csv(file_path)

    required_columns = {
        "time_s",
        "temperature_c",
        "light_value",
        "motion_detected",
    }

    missing_columns = required_columns - set(data.columns)

    if missing_columns:
        raise ValueError(f"Missing columns in CSV file: {missing_columns}")

    return data


def analyze_temperature(data: pd.DataFrame) -> dict:
    """Calculate temperature statistics."""
    return {
        "average_temperature": data["temperature_c"].mean(),
        "maximum_temperature": data["temperature_c"].max(),
        "minimum_temperature": data["temperature_c"].min(),
        "temperature_warnings": int(
            (data["temperature_c"] > TEMPERATURE_WARNING_LIMIT).sum()
        ),
    }


def analyze_light(data: pd.DataFrame) -> dict:
    """Calculate light sensor statistics."""
    return {
        "average_light": data["light_value"].mean(),
        "maximum_light": data["light_value"].max(),
        "minimum_light": data["light_value"].min(),
        "low_light_events": int((data["light_value"] < LOW_LIGHT_LIMIT).sum()),
    }


def analyze_motion(data: pd.DataFrame) -> dict:
    """Calculate motion detection statistics."""
    return {
        "motion_events": int(data["motion_detected"].sum()),
        "motion_percentage": data["motion_detected"].mean() * 100,
    }


def create_plots(data: pd.DataFrame) -> None:
    """Create plots for temperature and light sensor data."""
    plt.figure()
    plt.plot(data["time_s"], data["temperature_c"], linewidth=2)
    plt.axhline(
        TEMPERATURE_WARNING_LIMIT,
        linestyle="--",
        label="Temperature warning limit",
    )
    plt.xlabel("Time [s]")
    plt.ylabel("Temperature [°C]")
    plt.title("Temperature Sensor Data")
    plt.grid(True)
    plt.legend()
    plt.savefig("temperature_plot.png", dpi=300, bbox_inches="tight")

    plt.figure()
    plt.plot(data["time_s"], data["light_value"], linewidth=2)
    plt.axhline(
        LOW_LIGHT_LIMIT,
        linestyle="--",
        label="Low light limit",
    )
    plt.xlabel("Time [s]")
    plt.ylabel("Light Sensor Value")
    plt.title("Light Sensor Data")
    plt.grid(True)
    plt.legend()
    plt.savefig("light_plot.png", dpi=300, bbox_inches="tight")


def generate_report(
    temperature_results: dict,
    light_results: dict,
    motion_results: dict,
    report_file: Path,
) -> None:
    """Generate a text report from the analysis results."""
    report_text = f"""
Sensor Data Analysis Report
===========================

Temperature Analysis
--------------------
Average temperature: {temperature_results["average_temperature"]:.2f} °C
Maximum temperature: {temperature_results["maximum_temperature"]:.2f} °C
Minimum temperature: {temperature_results["minimum_temperature"]:.2f} °C
Temperature warnings: {temperature_results["temperature_warnings"]}

Light Analysis
--------------
Average light value: {light_results["average_light"]:.2f}
Maximum light value: {light_results["maximum_light"]:.2f}
Minimum light value: {light_results["minimum_light"]:.2f}
Low light events: {light_results["low_light_events"]}

Motion Analysis
---------------
Motion events: {motion_results["motion_events"]}
Motion percentage: {motion_results["motion_percentage"]:.2f} %

Generated files
---------------
temperature_plot.png
light_plot.png
"""

    report_file.write_text(report_text, encoding="utf-8")


def main() -> None:
    """Main program function."""
    data = load_sensor_data(DATA_FILE)

    temperature_results = analyze_temperature(data)
    light_results = analyze_light(data)
    motion_results = analyze_motion(data)

    create_plots(data)

    generate_report(
        temperature_results,
        light_results,
        motion_results,
        REPORT_FILE,
    )

    print("Analysis completed successfully.")
    print(f"Report saved as: {REPORT_FILE}")
    print("Plots saved as: temperature_plot.png and light_plot.png")


if __name__ == "__main__":
    main()
