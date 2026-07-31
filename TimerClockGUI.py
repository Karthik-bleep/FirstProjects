import sys
from PyQt5.QtCore import Qt,QTimer,QTime
from PyQt5.QtWidgets import QLabel,QWidget,QVBoxLayout,QApplication


class TimeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.timerclock = QLabel(self)
        self.timer = QTimer(self)
        self.ui()
    def ui(self):
        self.setWindowTitle("TimerClock")
        self.setGeometry(600,400,300,100)
        vb = QVBoxLayout()
        vb.addWidget(self.timerclock)
        self.setLayout(vb)
        self.timerclock.setAlignment(Qt.AlignCenter)
        self.timerclock.setStyleSheet("font-size: 80;" "font-family: Arial;")
        self.timer.timeout.connect(self.updatetime)
        self.timer.start(1000)
        self.updatetime()

    def updatetime(self):
        ct=QTime.currentTime().toString("hh:mm:ss AP")
        self.timerclock.setText(ct)




def main():
    app = QApplication(sys.argv)
    window=TimeWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ =="__main__":
    main()
