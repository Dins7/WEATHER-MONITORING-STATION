**Weather Monitoring Station using IoT and Machine Learning**

Project Overview:

     This project is a Weather Monitoring Station that utilizes IoT technologies, specifically a Raspberry Pi, to monitor various environmental parameters such as temperature, humidity, atmospheric pressure, and rainfall. The data is collected using sensors, processed by a Python script, and transmitted to the ThingSpeak cloud platform for storage and real-time analysis. Additionally, a machine learning model is integrated to predict weather conditions based on historical data. A web application is provided for visualizing sensor data and predictions.

Purpose: 

The Weather Monitoring System integrates IoT, Raspberry Pi, and various sensors to track and predict real-time weather conditions. Through precise data collection and machine learning algorithms, it enables informed decision-making, safety alerts, and offers insights into weather patterns for research purposes. This comprehensive solution enhances safety measures during extreme weather events and facilitates analysis of weather trends.

Requirements:

System Management : The system should be able to be monitored remotely.
Data Analysis : Should be done locally on the system using a machine learning model.
Application Deployment : Should be developed locally on the system, but with the ability to access them remotely.
Security : The system should have a basic authentication capability with user id and password.
System: The system should be able to identify users (i.e) basic authentication capability
           
Features:

•	Real-time Environmental Monitoring: Tracks temperature, humidity, atmospheric pressure, and rainfall.
•	Cloud Integration: Stores and analyzes data on ThingSpeak for remote access.
•	Machine Learning Predictions: Utilizes a trained ML model to predict weather conditions (e.g., sunny, rainy, cloudy).
•	Web Application: Provides an interface for real-time data visualization and weather prediction.

DOMAIN LEVEL SPECIFICATION:

Physical Entity: Environment 
Virtual Entity : Environment, ML model
Device: Raspberry Pi
Sensors: Temperature, Rain drop sensor, Anemometer, Barometric Pressure Sensor, Light sensor 

Sensor information:

Temperature and Humidity Sensor:This sensor measures both temperature and humidity levels in the surrounding environment. Example: DHT11 or DHT22 sensor.
Barometric Pressure Sensor:Measures atmospheric pressure, which can help in predicting weather changes. Example: BMP180 or BMP280 sensor.
Anemometer (Wind Speed Sensor):Measures wind speed, which is crucial for weather monitoring, especially for predicting storms or strong winds. Example: Anemometer with a pulse output or an ultrasonic anemometer.
Rain Drop Sensor: Detects rainfall or the presence of water droplets, which is essential for monitoring precipitation. Example: Raindrop sensor module.
Light Sensor: Measures the intensity of light in the surrounding environment, which is useful for understanding daylight conditions and variations in natural light. Example: TSL2561 or BH1750 sensor.

Key Technologies:

•	Hardware: Raspberry Pi 4B, BMP180 sensor, Raindrop sensor.
•	Programming Language: Python
•	IoT Platform: ThingSpeak
•	Machine Learning: Random Forest Classifier
•	Web Development: Flask, HTML, CSS

Installation and Setup:
Pre-requisites
•	Raspberry Pi with Raspbian OS installed.
•	Python 3.7 or later.
•	Sensors: BMP180 for pressure, Raindrop sensor for rain detection.
•	An active ThingSpeak account.


Installation Steps
1. Clone the Repository:

git clone https://github.com/yourusername/weather-monitoring-station.git
cd weather-monitoring-station

2. Install Python Dependencies:

pip install -r requirements.txt

3. Set up Raspberry Pi:

-Connect BMP180 and Raindrop sensor to the Raspberry Pi.
-Install necessary Python libraries for sensor interaction.

4. Configure ThingSpeak:

-Create channels on ThingSpeak for temperature, pressure, and rainfall data.
-Update the api_key and channel_id in the Python script with your ThingSpeak credentials.

5. Run the Weather Monitoring System:

python weather_monitor.py

6. Start the Web Application:

python app.py


Usage: 
-Run the weather_monitor.py script to start collecting sensor data and uploading it to ThingSpeak.
-Access the web application via http://localhost:5000 to view real-time data and weather predictions.

Folder Structure:

├── weather_monitor.py          # Main script for sensor data collection and transmission
├── ml_model.py                 # Script for training and saving the machine learning model
├── app.py                      # Flask web application
├── templates/
│   └── weather_app.html        # HTML template for the web interface
├── static/
│   ├── css/
│   └── js/
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation

Future Enhancements:
*Add more sensors (e.g., wind speed, UV index) for comprehensive monitoring.
*Improve the accuracy of the ML model with larger datasets.
*Develop mobile app integration for remote monitoring.

License:
This project is licensed under the MIT License - see the LICENSE file for details.

Contributing:
Contributions are welcome! Please feel free to submit a Pull Request.

Acknowledgments:
Special thanks to the open-source community for providing tools and resources.
ThingSpeak for providing an easy-to-use IoT cloud platform.



