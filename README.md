# Cafe Review Flask Application

A simple Flask web application that allows users to manage a list of cafes. Users can add new cafes by filling out a form and view all cafes in a tabular format.

## Features

- **Add a New Cafe**
  - Enter the cafe name, location URL, opening/closing times, and ratings for coffee, WiFi, and power sockets.
  - Ratings use emojis to represent levels (e.g., ☕️ for coffee, 💪 for WiFi, 🔌 for power sockets).
  - Data is saved to a CSV file (`cafe-data.csv`).

- **View Cafes**
  - Displays all cafes in a table format, with details like ratings and timings.

## Technologies Used

- **Flask**: Web framework
- **Flask-WTF**: Form handling
- **Flask-Bootstrap**: Styling
- **WTForms**: Form validation
- **CSV**: Data storage

## Installation

1. Clone the repository:
    ```bash
    https://github.com/Dimplektech/Cafe-Review-Flask-Application.git
  

2. Install the required dependencies
    ```bash
    pip install -r requirements.txt

3. Run the application:
    ```bash
    python main.py

## Project Structure
       ```bash
      cafe-review/
      ├── main.py              # Main Flask application
      ├── templates/
      │   ├── index.html      # Home page template
      │   ├── add.html        # Form to add a cafe
      │   ├── cafes.html      # Displays the list of cafes
      ├── static/             # Static files (CSS, JS, etc.)
      ├── requirements.txt    # Python dependencies
      ├── cafe-data.csv       # CSV file to store cafe data
      └── README.md           # Project documentation

## CSV Data Format
The data is stored in cafe-data.csv in the following format:
  ```bash
  Cafe Name,Location URL,Opening Time,Closing Time,Coffee Rating,WiFi Rating,Power Outlet Rating

Example:
Starbucks,https://starbucks.com,8:00 AM,10:00 PM,☕️☕️☕️☕️,💪💪💪💪,🔌🔌🔌🔌






    
      


