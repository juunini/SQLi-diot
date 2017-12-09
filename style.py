import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

def Style(entity, style):
	entity.setStyleSheet(style)

def Wrap(entity, entity2):
	Style(entity, "background: #22282e; color: #747a81;")
	entity2.setContentsMargins(0, 0, 0, 40)
	entity2.setSpacing(0)
	#Main.setGeometry(300,100,800,0)

def Title(entity, entity2, entity3):
	Style(entity, "padding: 0 30px; background: qlineargradient(x1:0 y1:0 x2:0 y2:1, stop:0 #23282e, stop:1 #1c1f24);")
	entity.setFixedHeight(90)
	entity2.setContentsMargins(0, 0, 0, 0)
	entity2.setSpacing(0)
	Style(entity3[0], "font-size: 28px; font-weight: light; color: #fff; background: none;")
	Style(entity3[1], "margin-top: 14px; font-size: 16px; font-weight: 600; color: #8492a1; background: none;")

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

def Url(entity, entity2):
	entity.setContentsMargins(40, 40, 40, 40)
	Style(entity2, """
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

def Button(entity1, entity2, entity3):
	Style(entity1, """
		min-width: 180px;
		min-height: 70px;
		color: #fff;
		font-size: 18px;
		font-weight: bold;
		background: #ce70ff;
	""")

	Style(entity2, """
		min-width: 180px;
		min-height: 70px;
		color: #fff;
		font-size: 18px;
		font-weight: bold;
		background: #11beff;
	""")

	entity3.setContentsMargins(0, 0, 0, 0)

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

def SelectZone(entity1, entity2):
	entity1.setStyleSheet("background: #000")
	entity2.setContentsMargins(0, 8, 0, 8)

def SettingZone(entity):
	entity.setStyleSheet("background: #22282e")
