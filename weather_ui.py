from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QDesktopWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import requests

class WeatherApp(QWidget):
  def __init__(self):
    super().__init__()
    self.city_label = QLabel("Enter city name: ", self)
    self.city_input = QLineEdit(self)
    self.get_weather_button = QPushButton("Get Weather", self)
    self.temperature_label = QLabel(self)
    self.emoji_label = QLabel(self)
    self.description_label = QLabel(self)
    self.initUI()
    
  def initUI(self):
    self.setWindowTitle("Weather App")
    self.setWindowIcon(QIcon("sun.png"))
    self.resize(300, 500)
    
    #center
    self.center()
    
    #layout
    vbox = QVBoxLayout()
    
    vbox.addWidget(self.city_label)
    vbox.addWidget(self.city_input)
    vbox.addWidget(self.get_weather_button)
    vbox.addWidget(self.temperature_label)
    vbox.addWidget(self.emoji_label)
    vbox.addWidget(self.description_label)
    
    self.setLayout(vbox)
    
    self.city_label.setAlignment(Qt.AlignCenter)
    self.city_input.setAlignment(Qt.AlignCenter)
    self.temperature_label.setAlignment(Qt.AlignCenter)
    self.emoji_label.setAlignment(Qt.AlignCenter)
    self.description_label.setAlignment(Qt.AlignCenter)
    
    #styling
    self.city_label.setObjectName("city_label")
    self.city_input.setObjectName("city_input")
    self.get_weather_button.setObjectName("get_weather_button")
    self.temperature_label.setObjectName("temperature_label")
    self.emoji_label.setObjectName("emoji_label")
    self.description_label.setObjectName("description_label")
    
    self.setStyleSheet("""
      QLabel, QPushButton{
        font-family: calibri;
      }   
      QLabel#city_label{
        font-size: 20px;
        font-style: italic;
      } 
      QLineEdit#city_input{
        font-size: 25px;
      }              
      QPushButton#get_weather_button{
        font-size: 20px;
        font-weight: bold;
        padding: 10px;
      }
      QLabel#temperature_label{
        font-size: 75px;
      }
      QLabel#emoji_label{
        font-size: 100px;
        font-family: Sagoe UI emoji; 
      }
      QLabel#description_label{
        font-size: 20px;
      }
    """)
    
    #connect
    self.get_weather_button.clicked.connect(self.get_weather)
    
  def center(self):
    screen = QDesktopWidget().availableGeometry().center()
    frame = self.frameGeometry()
    frame.moveCenter(screen)
    
  def get_weather(self):
    api_key = "3273a6c7e829f1ec80c2549464a55454"
    city = self.city_input.text()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
  
    try:
      response = requests.get(url)
      response.raise_for_status()
      data = response.json()
    
      if data["cod"] == 200:
        self.display_weather(data)
    except requests.exceptions.HTTPError as http_error:
      match response.status_code:
        case 400:
          self.display_error("Bad Request:\nPlease check your input.")
        case 400:
          self.display_error("Unauthorized:\nInvalid API key.")
        case 401:
          self.display_error("Forbidden:\nAccess is denied.")
        case 402:
          self.display_error("Internal Server Error:\nPlease try again later.")
        case 404:
          self.display_error("Not found:\nCity is not found.")
        case 500:
          self.display_error("Bad Gateway:\nInvalid response from the server.")
        case 502:
          self.display_error("Service Unavailable:\nServer is down.")
        case 503:
          self.display_error("Gateway Timout:\nNot response from the server.")
        case _:
          self.display_error(f"HTTP error occured:\n{http_error}")
    except requests.exceptions.ConnectionError:
      self.display_error("Connection Error:\nCheck your internet connection.")
    except requests.exceptions.Timeout:
      self.display_error("Timout Error:\nThe request timed out.")
    except requests.exceptions.TooManyRedirects:
      self.display_error("To many Redirects:\nCheck the URL.")
    except requests.exceptions.RequestException as req_error:
      self.display_error(f"Requesst Error:\n{req_error}")

  def display_weather(self, data):
    #temperature
    self.temperature_label.setStyleSheet("font-size: 75px; color: black")
    temperature_k = data["main"]["temp"]
    temperature_c = temperature_k - 273.15
    temperature_f = (temperature_k * 9/5) - 459.67
    self.temperature_label.setText(f"{temperature_f:.0f}°F")
    #emoji
    weather_id = data["weather"][0]["id"]
    self.emoji_label.setText(self.get_weather_emoji(weather_id))
    #descritpion
    weather_description = data["weather"][0]["description"]
    self.description_label.setText(f"{weather_description}")
    
  def display_error(self, message):
    self.temperature_label.setStyleSheet("font-size: 15px; color: #8c2220")
    self.temperature_label.setText(message)
    self.emoji_label.clear()
    self.description_label.clear()
    
  @staticmethod
  def get_weather_emoji(weather_id):
    if 200 <= weather_id <= 232:
      return "⛈️"
    elif 300 <= weather_id <= 321:
      return "🌥️"
    elif 500 <= weather_id <= 531:
      return "🌧️"
    elif 600 <= weather_id <= 622:
      return "🌨️"
    elif 701 <= weather_id <= 741:
      return "🌫️"
    elif weather_id == 762:
      return "🌋"
    elif weather_id == 771:
      return "🍃"
    elif weather_id == 781:
      return "🌪️"
    elif weather_id == 800:
      return "🌞"
    elif 801 <= weather_id <= 804:
      return "☁️"
    else: 
      return ""
  