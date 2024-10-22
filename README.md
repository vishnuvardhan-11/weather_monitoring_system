# Weather Monitoring System




## Overview
The Weather Monitoring System is a Python application that fetches, processes, and visualizes weather data using the OpenWeatherMap API. This tool provides real-time weather information, aiding users in data analysis and research.

## Features
- **Real-time Weather Data**: Fetch current weather data for specified cities.
- **Data Processing**: Analyze and transform the fetched data for insights.
- **Data Aggregation**: Store and aggregate historical weather data for trend analysis.
- **User Interface**: Command-line interface for easy interaction.
- **Security Layer**: API keys and sensitive data are securely managed.
- **Performance Optimization**: Code is optimized for speed and efficiency.

```markdown
## Project Structure
rule_engine/
├── main.py
├── src/
│   ├── __init__.py
│   ├── rule_engine.py
│   ├── ast_builder.py
│   └── evaluator.py
├── requirements.txt
└── README.md


## Installation
1. **Clone the Repository**:
   ```bash
   git clone <Your-GitHub-Repository-Link>
   cd weather_monitoring_system
   ```

2. **Install Required Packages**:
   Ensure you have Python 3.11 or later, then install the necessary packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **API Key**:
   Obtain your API key from [OpenWeatherMap](https://openweathermap.org/) and store it securely in `fetch_weather.py`.

## Usage
Run the application using:
```bash
python main.py
```
Follow the prompts to fetch weather data for specific cities.

### Example
When prompted, input the city name to retrieve the weather data.

## Security Measures
- **API Key Management**: The API key is not hard-coded and is stored in a secure manner to prevent exposure in the codebase.
- **Data Validation**: Inputs are validated to prevent injection attacks and ensure proper data processing.

## Performance Optimization
- The application utilizes efficient data structures to minimize memory usage and improve speed.
- Network requests are optimized to reduce latency in fetching weather data.

## Testing
Ensure the application is running correctly before submission. Verify all functionalities work as expected by running:
```bash
python main.py
```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements.
