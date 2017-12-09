import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from modules import *
import style

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

def Wrap(i): #페이지
	wrap.append(QWidget())
	layout.append(QVBoxLayout())
	wrap[i].setLayout(layout[i])
	style.Wrap(wrap[i], layout[i]) #스타일 설정

def Title(titleName, submit, i): #페이지 제목
	titleWrap.append(QWidget())
	titleLayout.append(QHBoxLayout())
	titleWrap[i].setLayout(titleLayout[i])
	layout[i].addWidget(titleWrap[i]) #레이아웃에 추가

	title.append([])
	title[i].append(QLabel(titleName))
	title[i].append(QLabel(submit))

	titleLayout[i].addWidget(title[i][0])
	titleLayout[i].addWidget(title[i][1])
	titleLayout[i].addStretch(0) #이걸 추가해야 맨 앞으로 밀림.
	style.Title(titleWrap[i], titleLayout[i], title[i]) #스타일 설정

def Url(i): #페이지에 자동으로 입력되는 URL
	urlWrap.append(QWidget())
	urlLayout.append(QHBoxLayout())
	urlWrap[i].setLayout(urlLayout[i])
	layout[i].addWidget(urlWrap[i]) #레이아웃에 추가

	url.append(QLineEdit())
	urlLayout[i].addWidget(url[i])
	style.Url(urlLayout[i], url[i]) #스타일 설정

def Button(i): #이전, 다음 버튼
	buttonWrap.append(QWidget())
	buttonLayout.append(QHBoxLayout())
	buttonWrap[i].setLayout(buttonLayout[i])
	layout[i].addWidget(buttonWrap[i]) #레이아웃에 추가

	Prev.append(QPushButton("Prev"))
	Next.append(QPushButton("Next"))
	buttonLayout[i].addStretch(0) #버튼이 화면 끝까지 안커지고 일정 크기를 유지하도록 추가
	buttonLayout[i].addWidget(Prev[i])
	buttonLayout[i].addWidget(Next[i])
	buttonLayout[i].addStretch(0) #버튼이 화면 끝까지 안커지고 일정 크기를 유지하도록 추가
	style.Button(Prev[i], Next[i], buttonLayout[i]) #스타일 설정


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
	layout[i].addWidget(selectZone[i]) #레이아웃에 추가
	style.SelectZone(selectZone[i], selectLayout[i]) #스타일 설정

def SettingZone(i, j):
	settingZone.append([])
	settingLayout.append([])
	settingZone[i].append(QWidget())
	settingLayout[i].append(QVBoxLayout())
	settingZone[i][j].setLayout(settingLayout[i][j])
	selectLayout[i].addWidget(settingZone[i][j], 0, j)
	style.SettingZone(settingZone[i][j]) #레이아웃에 추가

def SetAscii(i):
	setAscii.append(QComboBox())
	setAscii[i].addItem("(옵션)Ascii None")
	setAscii[i].addItem("(옵션)Double Ascii")
	setAscii[i].addItem("(옵션)Triple Ascii")
	setAscii[i].addItem("(옵션)All Double Ascii")
	setAscii[i].addItem("(옵션)All Triple Ascii")
	style.Select(setAscii[i])

def SlicedUrl(i):
	slicedUrl.append(QLabel(""))
	style.Text(slicedUrl[i])

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
	style.Select(alphabetCase[i]) #스타일 설정

def WhiteSpace(i):
	whiteSpace.append(QComboBox())
	whiteSpace[i].addItem("(옵션)Space = ' '")
	whiteSpace[i].addItem("(옵션)Space = Ascii")
	whiteSpace[i].addItem("(옵션)Space = Double Ascii")
	style.Select(whiteSpace[i]) #스타일 설정

def Comment(i):
	comment.append(QComboBox())
	comment[i].addItem("(옵션)주석 없음")
	comment[i].addItem("(옵션)주석 추가")
	style.Select(comment[i]) #스타일 설정


#------------------------------------------------------------------------

Wrap(0)
wrap[0].hide()
Title("Step 0.", "취약한 페이지를 찾아 입력해주세요.", 0)
Url(0)
url[0].setPlaceholderText("취약한 페이지를 찾아 입력해주세요.")
Button(0)
Prev[0].hide()

#-------------------------------------------------------------------

Wrap(1)
wrap[1].hide()
Title("Step 1.", "취약점 파악하기", 1)

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
style.Select(step1_number)

settingLayout[1][1].addStretch(0)
settingLayout[1][1].addWidget(step1_number)

SetAscii(1)

setColon = QComboBox()
setColon.addItem("'")
setColon.addItem('"')
setColon.addItem(")")
style.Select(setColon)

settingLayout[1][2].addWidget(setAscii[1])
settingLayout[1][2].addWidget(setColon)

Url(1)
Button(1)

#-------------------------------------------------

Wrap(2)
wrap[2].hide()
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
style.Select(order_by)

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
style.Input(column_amount)

lastComment = QComboBox()
lastComment.addItem("--")
lastComment.addItem("--+")
lastComment.addItem("--+-")
lastComment.addItem("-- -")
style.Select(lastComment)
settingLayout[2][2].addStretch(0)
settingLayout[2][2].addWidget(column_amount)
settingLayout[2][2].addWidget(lastComment)

Url(2)
Button(2)

#----------------------------------------------------------

Wrap(3)
wrap[3].hide()
Title("Step 3.", "취약한 컬럼 파악하기", 3)

SelectZone(3)
SettingZone(3, 0)
SettingZone(3, 1)
SettingZone(3, 2)

SlicedUrl(3)

error_factor = QComboBox()
error_factor.addItem("(옵션)에러유발인자 없음")
error_factor.addItem("(옵션)'-' 추가")
style.Select(error_factor)
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
style.Select(union_select)

settingLayout[3][1].addWidget(alphabetCase[3])
settingLayout[3][1].addWidget(setAscii[3])
settingLayout[3][1].addWidget(whiteSpace[3])
settingLayout[3][1].addWidget(comment[3])
settingLayout[3][1].addWidget(union_select)

number = QComboBox()
number.addItem("")
number.addItem("")
number.addItem("")
style.Select(number)

settingLayout[3][2].addStretch(0)
settingLayout[3][2].addWidget(number)

Url(3)
Button(3)


#------------------------------------------------------

Wrap(4)
wrap[4].hide()
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
#wrap[5].hide()
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
