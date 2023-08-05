
---

# Real Estate Investment Analysis

This project is a real estate investment analysis tool that calculates financial metrics for different properties based on their data. The project includes both a console application and a graphical user interface (GUI) version.

## Project Structure

```
real_estate_investment/
│   main.py
│   requirements.txt
│   README.md
│
└───models/
│   │   property.py
│
└───utils/
│   │   calculator.py
│
└───data/
│   │   properties.csv
│
└───interfaces/
│   │   gui.py
│
└───assets/
    │   icon.png
```

## Prerequisites

To run this project, you need to have Python (version 3.6 or higher) installed on your system.

## Setup

1. Clone or download the project to your local machine.

2. Open a terminal or command prompt and navigate to the project directory.

3. Create a virtual environment (recommended but optional):
   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

5. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Console Application

To run the console application:

1. Navigate to the project directory in the terminal.

2. Run the following command:
   ```bash
   python main.py
   ```

The console application will load property data from `data/properties.csv`, perform analysis, and display the results.

## Running the GUI Application

To run the GUI application:

1. Navigate to the project directory in the terminal.

2. Run the following command:
   ```bash
   python main.py
   ```

The console application will run first, displaying the analysis results in the terminal. After that, the GUI interface will launch, allowing you to interact with the application using a graphical interface.

## Project Customization

- You can customize property data by editing the `data/properties.csv` file.
- You can modify the calculation functions or add new financial metrics in the `utils/calculator.py` file.
- For GUI customization, you can update the `interfaces/gui.py` file to enhance the user interface.

---
