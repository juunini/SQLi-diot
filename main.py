import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Main(QMainWindow):
	def __init__(self):
		super().__init__()

		main = QVBoxLayout()
		main.setContentsMargins(50, 50, 50, 50)

		import layout
		for i in range(0, 6):
			main.addWidget(layout.wrap[i])

		import style

		window = QWidget()
		window.setStyleSheet("background: #000;")
		window.setLayout(main)
		self.setCentralWidget(window)

		#크기 설정
		self.setGeometry(300,100,800,0)
		#제목 설정
		self.setWindowTitle("SQLi-diot");
		self.show()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	do = Main()
	sys.exit(app.exec_())
