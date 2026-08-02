import requests
import sys
from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QPushButton,QLineEdit
from PyQt5.QtCore import Qt
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather App")
        self.apikey ="38e14e516536985249b10e2b6bba3fad"
        self.city_input =QLineEdit(self)
        self.status=QLabel("Status",self)
        self.status.setGeometry(200,120,80,50)

        self.city_input.setGeometry(30,55,250,35)
        self.weathertruth=QLabel("Weather",self)
        self.weathertruth.setGeometry(200,100,80,50)    
        self.button1= QPushButton("SUBMIT",self)
        self.button1.setGeometry(100,100,80,50)
        self.button1.clicked.connect(self.apiconnect)

        self.label = QLabel("Enter your city name: ",self)
        self.label.setGeometry(30,20,200,30)
       # self.html =f"https://history.openweathermap.org/data/2.5/aggregated/year?q={self.city_input}&appid={self.apikey}"

    def apiconnect(self):
        city = self.city_input.text().strip()
        self.html =f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.apikey}"
        response = requests.get(self.html)
        file = response.json()
        #print(file)
        tempink =file['main']['temp']
        state =file['weather'][0]['description']
        tempinc = str(round(tempink-273.15)) + "°C"
        print(tempinc)
        self.weathertruth.setText(str(tempinc))
        self.status.setText(state)

def main():
  app=QApplication(sys.argv)
  window=MainWindow()
  window.show()
  sys.exit(app.exec_())


if __name__=="__main__":
   main()

 

