import pandas as pd
from datetime import datetime

# Initialize storage
weather_data = []
unique_dates = set()

# Function to validate date
def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# Add new weather data
def add_weather_data():
    date = input("Enter date (YYYY-MM-DD): ")
    if not validate_date(date):
        print("Invalid date format. Use YYYY-MM-DD.")
        return

    if date in unique_dates:
        print("Data for this date already exists.")
        return

    try:
        temp = float(input("Enter temperature (°C): "))
        condition = input("Enter weather condition (e.g., Sunny, Rainy): ").strip()
        if not condition:
            print("Weather condition cannot be empty.")
            return
        weather_data.append({"Date": date, "Temperature": temp, "Condition": condition})
        unique_dates.add(date)
        print("Data added successfully!")
    except ValueError:
        print("Invalid temperature input.")

# View stored data
def view_weather_data():
    if not weather_data:
        print("No data available.")
        return
    for entry in weather_data:
        print(f"{entry['Date']} - {entry['Temperature']}°C - {entry['Condition']}")

# Export data to CSV
def export_to_csv():
    if not weather_data:
        print("No data to export.")
        return
    df = pd.DataFrame(weather_data)
    try:
        df.to_csv("weather_data.csv", index=False)
        print("Data exported to weather_data.csv")
    except Exception as e:
        print("Failed to export:", e)

# Show summary statistics
def show_summary():
    if not weather_data:
        print("No data available for analysis.")
        return
    df = pd.DataFrame(weather_data)
    avg_temp = df["Temperature"].mean()
    print(f"Average Temperature: {avg_temp:.2f}°C")
    print("Conditions observed:", ', '.join(df["Condition"].unique()))

# Main menu
def main():
    while True:
        print("\nWeather Data Recorder")
        print("1. Add Weather Data")
        print("2. View Weather Data")
        print("3. Export Data to CSV")
        print("4. Show Summary")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")
        if choice == '1':
            add_weather_data()
        elif choice == '2':
            view_weather_data()
        elif choice == '3':
            export_to_csv()
        elif choice == '4':
            show_summary()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please select 1-5.")

if __name__ == "__main__":
    main()