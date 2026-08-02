import sys
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QLabel,QPushButton
from PyQt5.QtCore import QTime,QTimer,Qt

class MainWindow(QWidget):
 def __init__(self):
  super().__init__()
  self.setWindowTitle("Stop Watch")
  self.setGeometry(400,400,300,300)
  self.Timer_Label = QLabel("00:00:00",self)
  self.time=QTime(0,0,0)
  self.button1=QPushButton("Start",self)
  self.button2=QPushButton("Stop",self)
  self.button3=QPushButton("Reset",self)
  self.timer=QTimer()
  vbox = QVBoxLayout()
  vbox.addWidget(self.Timer_Label)
  vbox.addWidget(self.button1)
  vbox.addWidget(self.button2)
  vbox.addWidget(self.button3)
  self.setLayout(vbox)
  self.button1.clicked.connect(self.start)
  self.button2.clicked.connect(self.stop)
  self.button3.clicked.connect(self.reset)
  self.timer.timeout.connect(self.update)
 def start(self):
  self.timer.start(10)
 def stop(self):
  self.timer.stop()
 def formattime(self,time):
  hour = self.time.hour()
  minutes=self.time.minute()
  seconds=self.time.second()
  msec=self.time.msec()//10
  return f"{hour:02}:{minutes:02}:{seconds:02}:{msec:02}"

 def update(self):
   self.time= self.time.addMSecs(10)
   self.Timer_Label.setText(self.formattime(self.time))
 def reset(self):
  self.time=self.timer.stop()
  self.time=QTime(0,0,0)
  self.Timer_Label.setText(self.formattime(self.time))



def main():
 app= QApplication(sys.argv)
 window= MainWindow()
 window.show()
 sys.exit(app.exec_())

if __name__ =="__main__":
 main()

