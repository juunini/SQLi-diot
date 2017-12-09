import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from modules import *

wrap = []
layout = []
titleWrap = []
titleLayout = []
title = []
urlWrap = []
urlLayout = []
url = []
buttonWrap = []
buttonLayout = []
Prev = []
Next = []

def Wrap(i):
	wrap.append(QWidget())
	layout.append(QVBoxLayout())
	wrap[i].setLayout(layout[i])

def Title(titleName, submit, i):
	titleWrap.append(QWidget())
	titleLayout.append(QHBoxLayout())
	titleWrap[i].setLayout(titleLayout[i])
	layout[i].addWidget(titleWrap[i])

	title.append([])
	title[i].append(QLabel(titleName))
	title[i].append(QLabel(submit))

	titleLayout[i].addWidget(title[i][0])
	titleLayout[i].addWidget(title[i][1])
	titleLayout[i].addStretch(0)

def Url(i):
	urlWrap.append(QWidget())
	urlLayout.append(QHBoxLayout())
	urlWrap[i].setLayout(urlLayout[i])
	layout[i].addWidget(urlWrap[i])

	url.append(QLineEdit())
	urlLayout[i].addWidget(url[i])

def Button(i):
	buttonWrap.append(QWidget())
	buttonLayout.append(QHBoxLayout())
	buttonWrap[i].setLayout(buttonLayout[i])
	layout[i].addWidget(buttonWrap[i])

	Prev.append(QPushButton("Prev"))
	Next.append(QPushButton("Next"))
	buttonLayout[i].addStretch(0)
	buttonLayout[i].addWidget(Prev[i])
	buttonLayout[i].addWidget(Next[i])
	buttonLayout[i].addStretch(0)

Wrap(0)
Title("Step 0.", "취약한 페이지를 찾아 입력해주세요.", 0)
Url(0)
url[0].setPlaceholderText("취약한 페이지를 찾아 입력해주세요.")
Button(0)
Prev[0].hide()

#-------------------------------------------------------------------

Wrap(1)
Title("Step 1.", "취약점 파악하기", 1)

selectZone = []
selectLayout = []
settingZone = []
settingLayout = []
settingZone.append([])
settingLayout.append([])
selectZone.append(QWidget())
selectLayout.append(QGridLayout())
setting = []
setting.append([])
slicedUrl = []
slicedUrl.append(QLabel())
setAscii = []
setAscii.append(QComboBox())


def SelectZone(i):
	selectZone.append(QWidget())
	selectLayout.append(QGridLayout())
	selectZone[i].setLayout(selectLayout[i])
	layout[i].addWidget(selectZone[i])

def SettingZone(i, j):
	settingZone.append([])
	settingLayout.append([])
	settingZone[i].append(QWidget())
	settingLayout[i].append(QVBoxLayout())
	settingZone[i][j].setLayout(settingLayout[i][j])
	selectLayout[i].addWidget(settingZone[i][j], 0, j)

def SetAscii(i):
	setAscii.append(QComboBox())
	setAscii[i].addItem("(옵션)Ascii None")
	setAscii[i].addItem("(옵션)Double Ascii")
	setAscii[i].addItem("(옵션)Triple Ascii")
	setAscii[i].addItem("(옵션)All Double Ascii")
	setAscii[i].addItem("(옵션)All Triple Ascii")

def SlicedUrl(i):
	slicedUrl.append(QLabel(""))

SelectZone(1)
SettingZone(1, 0)
SettingZone(1, 1)
SettingZone(1, 2)

SlicedUrl(1)
settingLayout[1][0].addStretch(0)
settingLayout[1][0].addWidget(slicedUrl[1])

step1_number = QComboBox()
step1_number.addItem("")
step1_number.addItem("99999")
step1_number.addItem("null")

settingLayout[1][1].addStretch(0)
settingLayout[1][1].addWidget(step1_number)

SetAscii(1)

setColon = QComboBox()
setColon.addItem("'")
setColon.addItem('"')
setColon.addItem(")")

settingLayout[1][2].addWidget(setAscii[1])
settingLayout[1][2].addWidget(setColon)

Url(1)
Button(1)

#-------------------------------------------------

alphabetCase = []
alphabetCase.append([])
alphabetCase.append([])
whiteSpace = []
whiteSpace.append([])
whiteSpace.append([])
comment = []
comment.append([])
comment.append([])

def AlphabetCase(i):
	alphabetCase.append(QComboBox())
	alphabetCase[i].addItem("(옵션)Lower Case")
	alphabetCase[i].addItem("(옵션)Upper Case")
	alphabetCase[i].addItem("(옵션)Random Case")
	alphabetCase[i].addItem("(옵션)Double Case")

def WhiteSpace(i):
	whiteSpace.append(QComboBox())
	whiteSpace[i].addItem("(옵션)Space = ' '")
	whiteSpace[i].addItem("(옵션)Space = Ascii")
	whiteSpace[i].addItem("(옵션)Space = Double Ascii")

def Comment(i):
	comment.append(QComboBox())
	comment[i].addItem("(옵션)주석 없음")
	comment[i].addItem("(옵션)주석 추가")

Wrap(2)
Title("Step 2.", "컬럼 갯수 알아내기", 2)

SelectZone(2)
SettingZone(2, 0)
SettingZone(2, 1)
SettingZone(2, 2)

SlicedUrl(2)
settingLayout[2][0].addStretch(0)
settingLayout[2][0].addWidget(slicedUrl[2])


order_by = QComboBox()
order_by.addItem(" order by ")
order_by.addItem(" group by ")

SetAscii(2)
AlphabetCase(2)
WhiteSpace(2)
Comment(2)
settingLayout[2][1].addWidget(alphabetCase[2])
settingLayout[2][1].addWidget(setAscii[2])
settingLayout[2][1].addWidget(whiteSpace[2])
settingLayout[2][1].addWidget(comment[2])
settingLayout[2][1].addWidget(order_by)

column_amount = QLineEdit()
column_amount.setPlaceholderText("숫자를 입력해주세요.")

lastComment = QComboBox()
lastComment.addItem("--")
lastComment.addItem("--+")
lastComment.addItem("--+-")
lastComment.addItem("-- -")
settingLayout[2][2].addStretch(0)
settingLayout[2][2].addWidget(column_amount)
settingLayout[2][2].addWidget(lastComment)

Url(2)
Button(2)

#----------------------------------------------------------

Wrap(3)
Title("Step 3.", "취약한 컬럼 파악하기", 3)

SelectZone(3)
SettingZone(3, 0)
SettingZone(3, 1)
SettingZone(3, 2)

SlicedUrl(3)

error_factor = QComboBox()
error_factor.addItem("(옵션)에러유발인자 없음")
error_factor.addItem("(옵션)'-' 추가")
settingLayout[3][0].addStretch(0)
settingLayout[3][0].addWidget(error_factor)
settingLayout[3][0].addWidget(slicedUrl[3])

SetAscii(3)
AlphabetCase(3)
WhiteSpace(3)
Comment(3)

union_select = QComboBox()
union_select.addItem(" union select ")
union_select.addItem(" union all select ")

settingLayout[3][1].addWidget(alphabetCase[3])
settingLayout[3][1].addWidget(setAscii[3])
settingLayout[3][1].addWidget(whiteSpace[3])
settingLayout[3][1].addWidget(comment[3])
settingLayout[3][1].addWidget(union_select)

number = QComboBox()
number.addItem("")
number.addItem("")
number.addItem("")

settingLayout[3][2].addStretch(0)
settingLayout[3][2].addWidget(number)

Url(3)
Button(3)


#------------------------------------------------------

Wrap(4)
Title("Step 4", "서버 운영체제 파악하기", 4)

SelectZone(4)
SettingZone(4, 0)

SetAscii(4)
AlphabetCase(4)
Comment(4)
settingLayout[4][0].addWidget(alphabetCase[4])
settingLayout[4][0].addWidget(setAscii[4])
settingLayout[4][0].addWidget(comment[4])

Url(4)
Button(4)

#----------------------------------------------------------


Wrap(5)
Title("Step 5", "DB 이름 파악하기", 5)

SelectZone(5)
SettingZone(5, 0)

SetAscii(5)
AlphabetCase(5)
Comment(5)
settingLayout[5][0].addWidget(alphabetCase[5])
settingLayout[5][0].addWidget(setAscii[5])
settingLayout[5][0].addWidget(comment[5])

Url(5)
Button(5)
