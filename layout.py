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

def Confirm(wrap, layout, titleWidget, titleLayout, title, titleText):
	wrap.setLayout(layout)
	style.Wrap(wrap, layout) #스타일 설정

	titleWidget.setLayout(titleLayout)
	layout.addWidget(titleWidget) #레이아웃에 추가

	title.setText(titleText)

	titleLayout.addWidget(title)
	titleLayout.addStretch(0) #이걸 추가해야 맨 앞으로 밀림.

	#타이틀 스타일 설정
	titleWidget.setStyleSheet("QWidget{padding: 0 30px; background: qlineargradient(x1:0 y1:0 x2:0 y2:1, stop:0 #23282e, stop:1 #1c1f24);}")
	titleWidget.setFixedHeight(90)
	titleLayout.setContentsMargins(0, 0, 0, 0)
	titleLayout.setSpacing(0)
	title.setStyleSheet("QLabel{margin-top: 14px; font-size: 16px; font-weight: 600; font-family: NanumGothic; color: #8492a1; background: none;}")

def Confirm_Button(layout, buttonWidget, buttonLayout, Prev, Next):
	buttonWidget.setLayout(buttonLayout)
	layout.addWidget(buttonWidget) #레이아웃에 추가

	buttonLayout.addStretch(0) #버튼이 화면 끝까지 안커지고 일정 크기를 유지하도록 추가
	buttonLayout.addWidget(Prev)
	buttonLayout.addWidget(Next)
	buttonLayout.addStretch(0) #버튼이 화면 끝까지 안커지고 일정 크기를 유지하도록 추가
	style.Button(Prev, Next, buttonLayout) #스타일 설정

def Confirm_Input(layout, inputWidget, inputLayout, _input, placeholder):
	inputWidget.setLayout(inputLayout)
	_input.setPlaceholderText(placeholder)
	style.Input(_input) #스타일 설정
	inputLayout.addWidget(_input)
	layout.addWidget(inputWidget) #레이아웃에 추가
	inputLayout.setContentsMargins(30, 30, 30, 30)

def Confirm_TextArea(layout, textareaWidget, textareaLayout, textarea, placeholder):
	textareaWidget.setLayout(textareaLayout)
	textarea.setPlaceholderText(placeholder)
	style.TextArea(textarea) #스타일 설정
	textareaLayout.addWidget(textarea)
	layout.addWidget(textareaWidget) #레이아웃에 추가
	textareaLayout.setContentsMargins(30, 30, 30, 0)


#------------------------------------------------------------------------

Wrap(0)
#wrap[0].hide()
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

confirm_step3_wrap = QWidget()
confirm_step3_layout = QVBoxLayout()
confirm_step3_titleWidget = QWidget()
confirm_step3_titleLayout = QHBoxLayout()
confirm_step3_title = QLabel("")
confirm_step3_buttonWidget = QWidget()
confirm_step3_buttonLayout = QHBoxLayout()
confirm_step3_prev = QPushButton("Prev")
confirm_step3_next = QPushButton("Next")
confirm_step3_inputWidget = QWidget()
confirm_step3_inputLayout = QHBoxLayout()
confirm_step3_input = QLineEdit()

Confirm(confirm_step3_wrap, confirm_step3_layout, confirm_step3_titleWidget, confirm_step3_titleLayout, confirm_step3_title, "몇 번 컬럼이 취약합니까?")
confirm_step3_wrap.hide()

Confirm_Input(confirm_step3_layout, confirm_step3_inputWidget, confirm_step3_inputLayout, confirm_step3_input, "숫자를 입력해주세요.")
Confirm_Button(confirm_step3_layout, confirm_step3_buttonWidget, confirm_step3_buttonLayout, confirm_step3_prev, confirm_step3_next)

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

confirm_step4_wrap = QWidget()
confirm_step4_layout = QVBoxLayout()
confirm_step4_titleWidget = QWidget()
confirm_step4_titleLayout = QHBoxLayout()
confirm_step4_title = QLabel("")
confirm_step4_buttonWidget = QWidget()
confirm_step4_buttonLayout = QHBoxLayout()
confirm_step4_prev = QPushButton("Prev")
confirm_step4_next = QPushButton("Next")
confirm_step4_inputWidget = QWidget()
confirm_step4_inputLayout = QHBoxLayout()
confirm_step4_input = QLineEdit()

Confirm(confirm_step4_wrap, confirm_step4_layout, confirm_step4_titleWidget, confirm_step4_titleLayout, confirm_step4_title, "서버 운영체제가 무엇입니까?")
confirm_step4_wrap.hide()

Confirm_Input(confirm_step4_layout, confirm_step4_inputWidget, confirm_step4_inputLayout, confirm_step4_input, "서버 운영체제를 입력해주세요.")
Confirm_Button(confirm_step4_layout, confirm_step4_buttonWidget, confirm_step4_buttonLayout, confirm_step4_prev, confirm_step4_next)

#----------------------------------------------------------

Wrap(5)
wrap[5].hide()
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


#--------------------------------------------------------------

confirm_step5_wrap = QWidget()
confirm_step5_layout = QVBoxLayout()
confirm_step5_titleWidget = QWidget()
confirm_step5_titleLayout = QHBoxLayout()
confirm_step5_title = QLabel("")
confirm_step5_buttonWidget = QWidget()
confirm_step5_buttonLayout = QHBoxLayout()
confirm_step5_prev = QPushButton("Prev")
confirm_step5_next = QPushButton("Next")
confirm_step5_inputWidget = QWidget()
confirm_step5_inputLayout = QHBoxLayout()
confirm_step5_input = QLineEdit()

Confirm(confirm_step5_wrap, confirm_step5_layout, confirm_step5_titleWidget, confirm_step5_titleLayout, confirm_step5_title, "DB의 이름이 무엇입니까?")
confirm_step5_wrap.hide()

Confirm_Input(confirm_step5_layout, confirm_step5_inputWidget, confirm_step5_inputLayout, confirm_step5_input, "DB이름을 입력해주세요.")
Confirm_Button(confirm_step5_layout, confirm_step5_buttonWidget, confirm_step5_buttonLayout, confirm_step5_prev, confirm_step5_next)

#---------------------------------------------------------------

Wrap(6)
wrap[6].hide()
Title("Step 6", "Table 이름 알아내기", 6)

SelectZone(6)
SettingZone(6, 0)

SetAscii(6)
AlphabetCase(6)
Comment(6)
settingLayout[6][0].addWidget(alphabetCase[6])
settingLayout[6][0].addWidget(setAscii[6])
settingLayout[6][0].addWidget(comment[6])

Url(6)
Button(6)

#--------------------------------------------------------------------

confirm_step6_wrap = QWidget()
confirm_step6_layout = QVBoxLayout()
confirm_step6_titleWidget = QWidget()
confirm_step6_titleLayout = QHBoxLayout()
confirm_step6_title = QLabel("")
confirm_step6_buttonWidget = QWidget()
confirm_step6_buttonLayout = QHBoxLayout()
confirm_step6_prev = QPushButton("Prev")
confirm_step6_next = QPushButton("Next")
confirm_step6_inputWidget = QWidget()
confirm_step6_inputLayout = QHBoxLayout()
confirm_step6_input = QLineEdit()
confirm_step6_textareaWidget = QWidget()
confirm_step6_textareaLayout = QHBoxLayout()
confirm_step6_textarea = QTextEdit()

Confirm(confirm_step6_wrap, confirm_step6_layout, confirm_step6_titleWidget, confirm_step6_titleLayout, confirm_step6_title, "알아낸 Table들을 입력해주세요.")
confirm_step6_wrap.hide()

Confirm_TextArea(confirm_step6_layout, confirm_step6_textareaWidget, confirm_step6_textareaLayout, confirm_step6_textarea, "출력된 Table이름 전체를 붙여넣기 해주세요.")
Confirm_Input(confirm_step6_layout, confirm_step6_inputWidget, confirm_step6_inputLayout, confirm_step6_input, "정보를 추출해낼 Table의 이름을 하나만 입력해주세요.")
Confirm_Button(confirm_step6_layout, confirm_step6_buttonWidget, confirm_step6_buttonLayout, confirm_step6_prev, confirm_step6_next)

#-----------------------------------------------------------------------

Wrap(7)
wrap[7].hide()
Title("Step 7", "Column 이름 알아내기", 7)

Url(7)
Button(7)

#--------------------------------------------------------------------

confirm_step7_wrap = QWidget()
confirm_step7_layout = QVBoxLayout()
confirm_step7_titleWidget = QWidget()
confirm_step7_titleLayout = QHBoxLayout()
confirm_step7_title = QLabel("")
confirm_step7_buttonWidget = QWidget()
confirm_step7_buttonLayout = QHBoxLayout()
confirm_step7_prev = QPushButton("Prev")
confirm_step7_next = QPushButton("Next")
confirm_step7_inputWidget = QWidget()
confirm_step7_inputLayout = QHBoxLayout()
confirm_step7_input = QLineEdit()
confirm_step7_textareaWidget = QWidget()
confirm_step7_textareaLayout = QHBoxLayout()
confirm_step7_textarea = QTextEdit()

Confirm(confirm_step7_wrap, confirm_step7_layout, confirm_step7_titleWidget, confirm_step7_titleLayout, confirm_step7_title, "알아낸 Column들을 입력해주세요.")
confirm_step7_wrap.hide()

Confirm_TextArea(confirm_step7_layout, confirm_step7_textareaWidget, confirm_step7_textareaLayout, confirm_step7_textarea, "출력된 Column이름 전체를 붙여넣기 해주세요.")
Confirm_Input(confirm_step7_layout, confirm_step7_inputWidget, confirm_step7_inputLayout, confirm_step7_input, "정보를 추출해낼 Column의 이름을 입력해주세요.(다수 가능. 콤마로 구분해주세요.)")
Confirm_Button(confirm_step7_layout, confirm_step7_buttonWidget, confirm_step7_buttonLayout, confirm_step7_prev, confirm_step7_next)

#------------------------------------------------------------------------

Wrap(8)
wrap[8].hide()
Title("Step 8", "Column에서 데이터 추출하기", 8)

Url(8)
Button(8)

#--------------------------------------------------------------------------

confirm_step8_wrap = QWidget()
confirm_step8_layout = QVBoxLayout()
confirm_step8_titleWidget = QWidget()
confirm_step8_titleLayout = QHBoxLayout()
confirm_step8_title = QLabel("")
confirm_step8_buttonWidget = QWidget()
confirm_step8_buttonLayout = QHBoxLayout()
confirm_step8_prev = QPushButton("Prev")
confirm_step8_next = QPushButton("Save")
confirm_step8_textareaWidget = QWidget()
confirm_step8_textareaLayout = QHBoxLayout()
confirm_step8_textarea = QTextEdit()

Confirm(confirm_step8_wrap, confirm_step8_layout, confirm_step8_titleWidget, confirm_step8_titleLayout, confirm_step8_title, "알아낸 Data들을 입력해주세요.")
confirm_step8_wrap.hide()

Confirm_TextArea(confirm_step8_layout, confirm_step8_textareaWidget, confirm_step8_textareaLayout, confirm_step8_textarea, "출력된 Data 전체를 붙여넣기 해주세요.")
Confirm_Button(confirm_step8_layout, confirm_step8_buttonWidget, confirm_step8_buttonLayout, confirm_step8_prev, confirm_step8_next)
confirm_step8_textareaLayout.setContentsMargins(30, 30, 30, 30)
