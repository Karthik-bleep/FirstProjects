import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QLabel,QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QPixmap
class MainWindow(QMainWindow):
 def __init__(self):
  super().__init__()
  self.setWindowTitle("My Firsty GUI")
  self.setWindowIcon(QIcon("cute.png"))
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
  self.ui()
 def ui(self):
  self.button=QPushButton("Click me",self)
  self.button.setGeometry(150,200,200,100)
  self.button.setStyleSheet("font-size:20px")
  self.button.clicked.connect(self.pri)

 def pri(self):
  print("Button Clicked")
  self.button.setText("Button Clicked")
  self.button.setDisabled(True)

def main():
 app =QApplication(sys.argv)
 window=MainWindow()
 window.show()
 sys.exit(app.exec_())

if __name__ == "__main__":
 main()
