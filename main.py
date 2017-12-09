import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Main(QMainWindow):
	def __init__(self):
		super().__init__()

		main = QVBoxLayout()
		main.setContentsMargins(50, 50, 50, 50)

		import layout

		for i in range(0, 9):
			main.addWidget(layout.wrap[i])
		main.addWidget(layout.confirm_step3_wrap)
		main.addWidget(layout.confirm_step4_wrap)
		main.addWidget(layout.confirm_step5_wrap)
		main.addWidget(layout.confirm_step6_wrap)
		main.addWidget(layout.confirm_step7_wrap)
		main.addWidget(layout.confirm_step8_wrap)

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

		#아이콘
		self.setWindowIcon(QIcon('icon.png'))

		#메뉴바
		menubar = self.menuBar()
		menu = menubar.addMenu('Menu')

		save = menu.addAction("Save")
		exit = menu.addAction("Exit")

		exit.setShortcut("Ctrl+Q")
		exit.setStatusTip("Exit Application")
		exit.triggered.connect(quit)

		self.setMenuBar(menubar)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	do = Main()
	sys.exit(app.exec_())
