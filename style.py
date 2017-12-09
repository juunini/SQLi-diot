import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from main import Main
import layout

def Style(entity, style):
	entity.setStyleSheet(style)

def Wrap(i):
	Style(layout.wrap[i], "background: #22282e; color: #747a81;")
	layout.layout[i].setContentsMargins(0, 0, 0, 40)
	layout.layout[i].setSpacing(0)
	#Main.setGeometry(300,100,800,0)

def Title(i):
	Style(layout.titleWrap[i], "padding: 0 30px; background: qlineargradient(x1:0 y1:0 x2:0 y2:1, stop:0 #23282e, stop:1 #1c1f24);")
	layout.titleWrap[i].setFixedHeight(90)
	layout.titleLayout[i].setContentsMargins(0, 0, 0, 0)
	layout.titleLayout[i].setSpacing(0)
	Style(layout.title[i][0], "font-size: 28px; font-weight: light; color: #fff; background: none;")
	Style(layout.title[i][1], "margin-top: 14px; font-size: 16px; font-weight: 600; color: #8492a1; background: none;")

def Input(entity):
	Style(entity, """
		height: 30px;
		padding: 0 20px;
		font-size: 14px;
		color: #747a81;
		border-top: 2px solid #101315;
		border-left: 2px solid #101315;
		border-right: 2px solid #242a2f;
		border-bottom: 2px solid #2b3136;
		background: #15181b;
	""")

def Text(entity):
	Style(entity, """
		height: 30px;
		font-size: 14px;
		color: #747a81;
	""")

def Url(i):
	layout.urlLayout[i].setContentsMargins(40, 40, 40, 40)
	Style(layout.url[i], """
		height: 60px;
		padding: 0 20px;
		font-size: 14px;
		color: #747a81;
		border-top: 2px solid #101315;
		border-left: 2px solid #101315;
		border-right: 2px solid #242a2f;
		border-bottom: 2px solid #2b3136;
		background: #15181b;
	""")

def Button(i):
	Style(layout.Prev[i], """
		min-width: 180px;
		min-height: 70px;
		color: #fff;
		font-size: 18px;
		font-weight: bold;
		background: #ce70ff;
	""")

	Style(layout.Next[i], """
		min-width: 180px;
		min-height: 70px;
		color: #fff;
		font-size: 18px;
		font-weight: bold;
		background: #11beff;
	""")

	layout.buttonLayout[i].setContentsMargins(0, 0, 0, 0)

def Select(entity):
	Style(entity, """
		QComboBox{
			height: 30px;
			padding: 0 20px;
			font-size: 14px;
			color: #747a81;
			border-top: 2px solid #101315;
			border-left: 2px solid #101315;
			border-right: 2px solid #242a2f;
			border-bottom: 2px solid #2b3136;
			background: #15181b;
		}
		QComboBox::drop-down{
			border: none;
		}
		QComboBox::down-arrow{
			width: 0;
			height: 0;
			margin-top: 4px;
			margin-right: 10px;
			border: 5px solid #15181b;
			border-top: 5px solid #747a81;
		}
		QComboBox QAbstractItemView{
			border: 2px solid #101315;
		}
	""")

def SelectZone(i):
	layout.selectZone[i].setStyleSheet("background: #000")
	layout.selectLayout[i].setContentsMargins(0, 8, 0, 8)

def SettingZone(i, j):
	layout.settingZone[i][j].setStyleSheet("background: #22282e")

def Press_Next0():
	layout.wrap[0].hide()
	layout.wrap[1].show()


def Press_Prev1():
	layout.wrap[1].hide()
	layout.wrap[0].show()

def Press_Next1():
	layout.wrap[1].hide()
	layout.wrap[2].show()

def Press_Prev2():
	layout.wrap[2].hide()
	layout.wrap[1].show()

def Press_Next2():
	layout.wrap[2].hide()
	layout.wrap[3].show()

def Press_Next3():
	layout.wrap[3].hide()
	layout.wrap[4].show()

def Press_Next4():
	layout.wrap[4].hide()
	layout.wrap[5].show()

Wrap(0)
layout.wrap[0].setFixedHeight(360)
Title(0)
Url(0)
Button(0)
layout.Next[0].clicked.connect(Press_Next0)

Wrap(1)
layout.wrap[1].setFixedHeight(454)
layout.wrap[1].hide()
Title(1)
Url(1)
Button(1)
Text(layout.slicedUrl[1])
layout.Prev[1].clicked.connect(Press_Prev1)
layout.Next[1].clicked.connect(Press_Next1)

SelectZone(1)
SettingZone(1, 0)
SettingZone(1, 1)
SettingZone(1, 2)

Select(layout.step1_number)
Select(layout.setColon)
Select(layout.setAscii[1])

Wrap(2)
layout.wrap[2].hide()
Title(2)
Url(2)
Button(2)
Text(layout.slicedUrl[2])
layout.Next[2].clicked.connect(Press_Next2)

SelectZone(2)
SettingZone(2, 0)
SettingZone(2, 1)
SettingZone(2, 2)

Select(layout.alphabetCase[2])
Select(layout.setAscii[2])
Select(layout.whiteSpace[2])
Select(layout.comment[2])
Select(layout.order_by)
Input(layout.column_amount)
Select(layout.lastComment)


Wrap(3)
layout.wrap[3].hide()
Title(3)
Url(3)
Button(3)

SelectZone(3)
SettingZone(3, 0)
SettingZone(3, 1)
SettingZone(3, 2)

Select(layout.alphabetCase[3])
Select(layout.setAscii[3])
Select(layout.whiteSpace[3])
Select(layout.comment[3])
Select(layout.union_select)
Select(layout.error_factor)
Select(layout.number)
Text(layout.slicedUrl[3])
layout.Next[3].clicked.connect(Press_Next3)


Wrap(4)
layout.wrap[4].hide()
Title(4)
Url(4)
Button(4)
SelectZone(4)
SettingZone(4, 0)
Select(layout.alphabetCase[4])
Select(layout.setAscii[4])
Select(layout.comment[4])
layout.Next[4].clicked.connect(Press_Next4)


Wrap(5)
layout.wrap[5].hide()
Title(5)
Url(5)
Button(5)
SelectZone(5)
SettingZone(5, 0)
Select(layout.alphabetCase[5])
Select(layout.setAscii[5])
Select(layout.comment[5])
