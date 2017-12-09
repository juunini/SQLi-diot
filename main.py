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
		icon = QIcon()
		icon.addFile('icon.png', QSize(16, 16))
		icon.addFile('icon.png', QSize(24, 24))
		icon.addFile('icon.png', QSize(32, 32))
		icon.addFile('icon.png', QSize(48, 48))
		icon.addFile('icon.png', QSize(256, 256))
		self.setWindowIcon(icon)

		#메뉴바
		menubar = self.menuBar()
		menubar.setStyleSheet("""
			QMenuBar{
				padding: 6px 30px;
				background: qlineargradient(x1:0 y1:0 x2:0 y2:1, stop:0 #23282e, stop:1 #1c1f24);
				font-size: 28px;
				font-weight: light;
				color: #fff;
			}
			QMenuBar::item{background: none;}
		""")
		menu = menubar.addMenu('Menu')

		save = menu.addAction("Save")
		exit = menu.addAction("Exit")

		save.setShortcut("Ctrl+S")
		save.setStatusTip("Save Process")

		exit.setShortcut("Ctrl+Q")
		exit.setStatusTip("Exit Application")
		exit.triggered.connect(quit)

		self.setMenuBar(menubar)

		#폰트
		QFontDatabase.addApplicationFont("Sansita-Regular.ttf")
		QFontDatabase.addApplicationFont("NanumGothic.ttf")

if __name__ == "__main__":
	app = QApplication(sys.argv)
	do = Main()
	sys.exit(app.exec_())
