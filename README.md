# Passenger Management System

## Overview

This Python application allows users to manage passenger data stored in a CSV file. Users can add, remove, search for, and modify passenger details, including name, gender, PNR number, source and destination stations, contact information, fare, and seat number. The application utilizes a simple graphical interface for file selection and operates through a console-based menu system.

## Features

- Choose a CSV file containing passenger data using a graphical interface.
- Add new passengers to the CSV file.
- Remove passengers from the CSV file.
- Search for passengers using their PNR number.
- View the total number of passengers in the file.
- Update specific information of existing passengers.

## Requirements

- Python 3.x
- Pandas library
- Tkinter (comes with Python standard library)

## Installation

1. Clone the repository or download the code files.
2. Install the required libraries using pip:

   ```bash
   pip install pandas
   ```

## Usage

1. Run the application:

   ```bash
   python passenger_management.py
   ```

2. A window will appear prompting you to select a CSV file containing passenger data.
3. Once the file is selected, a menu will display options to manage passenger data:
   - **1**: Add a Passenger
   - **2**: Remove a Passenger
   - **3**: Find a Passenger using PNR Number
   - **4**: Find Total Number of Passengers
   - **5**: Change Passenger Information

4. Follow the prompts in the console to perform the desired actions.

## Example CSV Format

The CSV file should have the following headers:

```csv
Name,Gender,PNR,Source_Station,Destination_Station,Contact,Fare,Seat
```

### Sample Data:

```csv
John Doe,Male,123456,Station A,Station B,9876543210,100,1A
Jane Smith,Female,123457,Station B,Station C,9876543211,150,2B
```

## Important Notes

- Ensure that the CSV file has the correct format and headers.
- Make backups of your CSV file to prevent accidental data loss.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the developers of the Pandas library for providing powerful data manipulation tools.
- Tkinter for enabling a simple GUI for file selection.
