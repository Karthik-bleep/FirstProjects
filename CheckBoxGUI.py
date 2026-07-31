import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QLabel,QPushButton,QCheckBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QPixmap
class MainWindow(QMainWindow):
 def __init__(self):
  super().__init__()
  self.setWindowTitle("My Firsty GUI")
 
  self.setGeometry(700,300,500,500)
  label= QLabel("KARTHIK",self)
  label.setFont(QFont("arial",30))
  label.setGeometry(0,0,500,100)
  label.setAlignment(Qt.AlignCenter)
  label = QLabel(self)
  label.setGeometry(0,0,250,250)
  pixmap=QPixmap("cute.png")
  label.setPixmap(pixmap)
  label.setScaledContents(True)
  self.checkbox=QCheckBox("Are you Karthik?",self)
  self.ui()
 def ui(self):

  self.checkbox.setStyleSheet("font-size: 20px;""font-family: Arial;")
  self.checkbox.setGeometry(100,300,200,100)
  self.checkbox.stateChanged.connect(self.pro)
  


 def pro(self,state):
   if state==2:
    print("Checkbox checked")
   else:
    print("Not checked")
  
def main():
 app =QApplication(sys.argv)
 window=MainWindow()
 window.show()
 sys.exit(app.exec_())

if __name__ == "__main__":
 main()
