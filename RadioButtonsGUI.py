import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QLabel,QPushButton,QCheckBox,QRadioButton,QButtonGroup
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QPixmap
class MainWindow(QMainWindow):
 def __init__(self):
  super().__init__()
  self.setWindowTitle("My Firsty GUI")
  self.setGeometry(700,300,500,500)
  self.radiobutton1=QRadioButton("MasterCard",self)
  self.radiobutton2=QRadioButton("Visa",self)
  self.radiobutton3=QRadioButton("Online",self)
  self.radiobutton4=QRadioButton("Store",self)
  
  self.ui()
 def ui(self):
  self.radiobutton1.setGeometry(0,0,300,50)
  self.radiobutton2.setGeometry(0,50,300,50)
  self.radiobutton3.setGeometry(0,100,300,50)
  self.radiobutton4.setGeometry(0,150,300,50)
  self.radiobutton1.setStyleSheet("font-size:40px;""font-family:Arial;")
  self.radiobutton2.setStyleSheet("font-size:40px;""font-family:Arial;")
  self.radiobutton3.setStyleSheet("font-size:40px;""font-family:Arial;")
  self.radiobutton4.setStyleSheet("font-size:40px;""font-family:Arial;")
  self.radiobutton1.toggled.connect(self.check)
  self.radiobutton2.toggled.connect(self.check)
  self.radiobutton3.toggled.connect(self.check)
  self.radiobutton4.toggled.connect(self.check)

 def check(self):
  radio_button=self.sender()
  if radio_button.isChecked():
    print(radio_button.text())
 
  
def main():
 app =QApplication(sys.argv)
 window=MainWindow()
 window.show()
 sys.exit(app.exec_())

if __name__ == "__main__":
 main()
