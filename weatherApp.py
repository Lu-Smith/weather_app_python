# Weather App

#Api_key = 3273a6c7e829f1ec80c2549464a55454

import sys
from PyQt5.QtWidgets import QApplication, QWidget

class WeatherApp(QWidget):
  def __init__(self):
    super().__init__()

def main():
  app = QApplication(sys.argv)
  weather_app = WeatherApp()
  weather_app.show()
  sys.exit(app.exec_())  

if __name__ =="__main__":
  main()