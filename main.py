import sys
from PyQt5.QtWidgets import QApplication
from weather_ui import WeatherApp

def main():
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())  

if __name__ == "__main__":
    main()