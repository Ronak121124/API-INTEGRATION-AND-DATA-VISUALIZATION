# Name: Ronak Manoj Maheshwari
# Topic : TO FETCH DATA FROM A PUBLIC API (E.G., OPENWEATHERMAP) AND CREATE VISUALIZATIONS
# Software : Visual Studio Code
# Language : Python


import requests
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import pandas as pd

# ✅ API setup
API_KEY = "a2755c5c8b98da657bda9ea39b7d2e56"  
CITY = "Mumbai"
BASE_URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# 🌐 Fetch weather data
def get_weather_data():
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

#  Process data
def process_weather_data(data):
    if not data:
        return None
    
    dates = []
    temperatures = []
    humidities = []
    
    for entry in data['list'][:24]:  # Next 24 hours (3-hour intervals)
        dates.append(datetime.fromtimestamp(entry['dt']))
        temperatures.append(entry['main']['temp'])
        humidities.append(entry['main']['humidity'])
    
    return pd.DataFrame({
        'Date': dates,
        'Temperature (°C)': temperatures,
        'Humidity (%)': humidities
    })

# 📊 Create visualizations
def create_visualizations(df):
    if df is None:
        print("No data to visualize")
        return
    
    sns.set_style("whitegrid")
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
    
    # Temperature plot
    sns.lineplot(data=df, x='Date', y='Temperature (°C)', ax=ax1, color='red', marker='o')
    ax1.set_title(f'Temperature Forecast for {CITY}')
    ax1.set_xlabel('Date and Time')
    ax1.set_ylabel('Temperature (°C)')
    ax1.tick_params(axis='x', rotation=45)
    
    # Humidity plot
    sns.lineplot(data=df, x='Date', y='Humidity (%)', ax=ax2, color='blue', marker='o')
    ax2.set_title(f'Humidity Forecast for {CITY}')
    ax2.set_xlabel('Date and Time')
    ax2.set_ylabel('Humidity (%)')
    ax2.tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.savefig('weather_forecast.png')
    plt.show()

# 🚀 Main function
def main():
    weather_data = get_weather_data()
    df = process_weather_data(weather_data)
    create_visualizations(df)

if __name__ == "__main__":
    main()
    
#Explaination : 
# This Python script is a weather forecasting tool that fetches real-time data from the OpenWeatherMap API.
# It visualizes temperature and humidity trends for the next 24 hours in Mumbai using data science libraries.
# The script begins by setting up the API key and constructing a URL with metric units for clarity.
# The get_weather_data() function sends a GET request to the API and returns the JSON response if successful.
# If the request fails, it prints an error message to help users debug connectivity or API issues.
# The process_weather_data() function extracts timestamps, temperatures, and humidity levels from the first 24 forecast entries.
# These entries represent 3-hour intervals, covering a full day of weather predictions in a structured format.
# The extracted data is converted into a Pandas DataFrame, enabling easy manipulation and analysis of trends.
# This structured format allows for efficient plotting and statistical operations using Python’s data science ecosystem.
# The create_visualizations() function uses Seaborn and Matplotlib to generate two line plots for clarity and insight.
# One plot shows temperature trends, and the other visualizes humidity levels, both plotted against time intervals.
# The plots are styled with gridlines, labeled axes, and rotated x-ticks to enhance readability and presentation.
# Each visualization is saved as a PNG image before being displayed, making it easy to share or archive.
# The entire script is wrapped in a main() function that orchestrates the data fetching, processing, and plotting.
# It runs only when executed directly, ensuring modularity and preventing unintended execution during imports or testing.
# When the script is run, it produces clean and informative visualizations of Mumbai’s weather for the next 24 hours.
# This allows users to quickly understand temperature and humidity patterns and plan their day accordingly.
# The modular design makes it easy to adapt the script for other cities or add new weather metrics.
# You could extend it to include wind speed, precipitation, or even air quality using additional API endpoints.
# Overall, the script demonstrates how to integrate API data with Python’s data science libraries effectively.
# It’s a great example of building a useful and visually appealing real-world application with minimal complexity.
# For someone like you, Ronak, who blends technical skill with creative storytelling, this tool is a perfect showcase.
# You could enhance it by adding interactive dashboards using Plotly or deploying it as a web app with Flask.
# Embedding logos, customizing color palettes, or exporting reports as PDFs would add polish and professional appeal.
# This kind of project is ideal for internships, academic submissions, or startup demos where clarity matters most.
# It highlights your ability to turn raw data into actionable insights with clean code and thoughtful design.
# Whether you're presenting to a client, refining your portfolio, or just practicing Python, this tool stands out.
# It’s practical, impressive, and a strong foundation for more advanced weather analytics or data-driven storytelling.
