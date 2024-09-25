# Weather App
#Api_key = 3273a6c7e829f1ec80c2549464a55454

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, 
                             QLineEdit, QPushButton, QVBoxLayout,
                             QHBoxLayout)

class WeatherApp(QWidget):
  def __init__(self):
    super().__init__()
    self.city_label = QLabel("Enter city name: ", self)
    self.city_input = QLineEdit(self)
    self.get_weather_button = QPushButton("Get Weather", self)
    self.temperature_label = QLabel("70°F", self)
    self.emoji_label = QLabel("🌞", self)
    self.description_label = QLabel("Sunny", self)
    self.initUI()
    
  def initUI(self):
    self.setWindowTitle("Weather App")
    
    vbox = QVBoxLayout()
    
    vbox.addWidget(self.city_label)
    vbox.addWidget(self.city_input)
    vbox.addWidget(self.get_weather_button)
    vbox.addWidget(self.temperature_label)
    vbox.addWidget(self.emoji_label)
    vbox.addWidget(self.description_label)
    
    self.setLayout(vbox)

def main():
  app = QApplication(sys.argv)
  weather_app = WeatherApp()
  weather_app.show()
  sys.exit(app.exec_())  

if __name__ =="__main__":
  main()